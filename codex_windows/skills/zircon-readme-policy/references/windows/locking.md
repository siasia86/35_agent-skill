# 작업 잠금 실행

`$Repo`와 `$SkillDir`은 확인한 프로젝트·스킬 절대 경로입니다. 토큰은 현재 작업에서 생성해 비공개로 유지하고 로그에 출력하지 않습니다. 아래 예시는 승인된 변경 구간을 소유하고 있을 때 사용합니다.

```powershell
$SessionToken = [guid]::NewGuid().ToString('N')
$LockTool = Join-Path $SkillDir 'scripts/lock.py'
python -X utf8 -B $LockTool acquire --root $Repo --token $SessionToken --task '현재 작업 요약'
if ($LASTEXITCODE -ne 0) { throw '잠금 획득 실패' }
try {
    python -X utf8 -B $LockTool check --root $Repo --token $SessionToken
    if ($LASTEXITCODE -ne 0) { throw '잠금 소유 확인 실패' }
    # 승인된 담당 파일 변경
} finally {
    python -X utf8 -B $LockTool release --root $Repo --token $SessionToken
    if ($LASTEXITCODE -ne 0) { throw '잠금 해제 실패: 소유와 증거 확인 필요' }
}
```

획득 0이 확인된 뒤에만 정리 구간에 들어갑니다. 명령이 실패하면 다른 도구로 강제 해제하지 않습니다. 도구는 `.kiro-lock`와 `.kiro-lock.guard`를 사용하며 16자 이상 토큰을 요구합니다. 토큰·사용자·호스트·파일 동일성 불일치와 기존 guard는 차단 조건입니다.

정상 0, 차단 1, 잘못된 인수 2, 사용자 중단 130을 구분합니다. 오래됐거나 손상된 잠금은 단순 경과 시간으로 삭제하지 않고 현재 소유·진행 작업·복구 요청을 확인합니다. 재개 또는 10분 경과 후 쓰기 전 check를 다시 실행합니다.
