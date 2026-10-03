<#
.SYNOPSIS
Capture selected personal Codex files in the existing home-relative layout.
.DESCRIPTION
Reads settings and whole selected skill folders without changing the source.
The update folder must contain a Git ignore rule for private/. Existing phases
are never overwritten. Authentication, sessions, plugins and system skills are
outside the selected input set. File bytes are preserved; ACLs/ADS are not copied.
#>
[CmdletBinding()]
param(
    [Parameter(Mandatory)]
    [ValidatePattern('^[A-Za-z0-9][A-Za-z0-9_-]{0,100}$')]
    [string]$UpdateId,
    [Parameter(Mandatory)]
    [ValidateSet('before', 'after')]
    [string]$Phase,
    [string]$UserDirectory = [Environment]::GetFolderPath('UserProfile'),
    [string]$UpdateDirectory = [IO.Path]::GetFullPath((Join-Path $PSScriptRoot '../..')),
    [ValidatePattern('^[a-z0-9][a-z0-9-]{0,63}$')]
    [string[]]$SkillNames = @(
        'code-review', 'debugging-and-recovery', 'git-commit-rule',
        'markdown-review', 'md-link-check', 'planning-and-breakdown', 'work-rules'
    )
)
Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

function Assert-PlainPath([string]$Path) {
    $item = Get-Item -LiteralPath $Path -Force
    while ($null -ne $item) {
        if ($item.Attributes -band [IO.FileAttributes]::ReparsePoint) {
            throw 'A selected path uses a reparse point. Snapshot stopped.'
        }
        if ($item -is [IO.FileInfo]) { $item = $item.Directory }
        else { $item = $item.Parent }
    }
}

function Get-SelectedFiles {
    $selected = [Collections.Generic.List[IO.FileInfo]]::new()
    foreach ($name in @('AGENTS.md', 'config.toml')) {
        $item = Get-Item -LiteralPath (Join-Path $UserDirectory ".codex/$name") -Force
        if ($item -isnot [IO.FileInfo]) { throw 'A required setting is not a file.' }
        Assert-PlainPath $item.FullName
        $selected.Add($item)
    }
    foreach ($name in $SkillNames) {
        $folder = Join-Path $UserDirectory ".agents/skills/$name"
        Assert-PlainPath $folder
        if (-not (Test-Path -LiteralPath (Join-Path $folder 'SKILL.md') -PathType Leaf)) {
            throw "Missing SKILL.md for selected skill: $name"
        }
        foreach ($item in Get-ChildItem -LiteralPath $folder -Force -Recurse) {
            if ($item.Attributes -band [IO.FileAttributes]::ReparsePoint) {
                throw "A selected skill uses a reparse point: $name"
            }
            if ($item -is [IO.FileInfo]) { $selected.Add($item) }
        }
    }
    $selected | Sort-Object FullName -Unique
}

if ($SkillNames.Count -eq 0 -or @($SkillNames | Select-Object -Unique).Count -ne $SkillNames.Count) {
    throw 'Select at least one skill and use unique skill names.'
}
$UserDirectory = (Get-Item -LiteralPath $UserDirectory -Force).FullName
Assert-PlainPath $PSScriptRoot
$UpdateDirectory = (Get-Item -LiteralPath $UpdateDirectory -Force).FullName
Assert-PlainPath $UpdateDirectory
$updateFolder = Join-Path $UpdateDirectory $UpdateId
Assert-PlainPath $updateFolder
$destination = Join-Path $updateFolder "private/$Phase"
if (Test-Path -LiteralPath $destination) { throw 'This phase already exists. Use a new update ID.' }
$repoRoot = & git -C $UpdateDirectory rev-parse --show-toplevel
if ($LASTEXITCODE -ne 0) { throw 'Could not identify the management Git root.' }
$probe = [IO.Path]::GetRelativePath($repoRoot, (Join-Path $destination 'probe')).Replace('\', '/')
& git -C $repoRoot check-ignore --quiet -- $probe
if ($LASTEXITCODE -ne 0) { throw 'private/ must be Git ignored before a snapshot is created.' }
if (Test-Path -LiteralPath (Join-Path $updateFolder 'private')) {
    Assert-PlainPath (Join-Path $updateFolder 'private')
}

$files = @(Get-SelectedFiles)
$captured = @()
foreach ($file in $files) {
    $relative = [IO.Path]::GetRelativePath($UserDirectory, $file.FullName).Replace('\', '/')
    $bytes = [IO.File]::ReadAllBytes($file.FullName)
    $captured += [pscustomobject]@{
        RelativePath = $relative
        Bytes = $bytes
        Sha256 = [Convert]::ToHexString([Security.Cryptography.SHA256]::HashData($bytes))
    }
}
$latest = @(Get-SelectedFiles)
if (($files.FullName -join "`n") -cne ($latest.FullName -join "`n")) {
    throw 'Selected file inventory changed during capture. Retry after the update finishes.'
}
foreach ($entry in $captured) {
    $current = (Get-FileHash -LiteralPath (Join-Path $UserDirectory $entry.RelativePath) -Algorithm SHA256).Hash
    if ($current -cne $entry.Sha256) {
        throw 'Selected bytes changed during capture. Retry after the update finishes.'
    }
}
New-Item -ItemType Directory -Path $destination | Out-Null
foreach ($entry in $captured) {
    $target = Join-Path $destination $entry.RelativePath
    New-Item -ItemType Directory -Path ([IO.Path]::GetDirectoryName($target)) -Force | Out-Null
    [IO.File]::WriteAllBytes($target, $entry.Bytes)
    if ((Get-FileHash -LiteralPath $target -Algorithm SHA256).Hash -cne $entry.Sha256) {
        throw 'Snapshot byte validation failed; no completion manifest was written.'
    }
}
$manifest = [ordered]@{
    Version = '26.10.03'
    CapturedUtc = [DateTimeOffset]::UtcNow.ToString('o')
    Phase = $Phase
    SkillNames = $SkillNames
    FileCount = $captured.Count
    Files = @($captured | ForEach-Object {
        [ordered]@{ RelativePath = $_.RelativePath; Length = $_.Bytes.Length; Sha256 = $_.Sha256 }
    })
}
$encoding = [Text.UTF8Encoding]::new($false)
[IO.File]::WriteAllText((Join-Path $destination 'manifest.json'), ($manifest | ConvertTo-Json -Depth 6) + "`n", $encoding)
[pscustomobject]@{ Phase = $Phase; Skills = $SkillNames.Count; Files = $captured.Count; Verified = $true }
