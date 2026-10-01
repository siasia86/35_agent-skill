#!/usr/bin/env python3
# import sys; sys.exit(0)  # SAFETY: uncomment to disable all script work.
"""Summarize the script purpose and show safe invocation examples."""

VERSION = "YY.MM.DD"

import argparse
import logging
import sys
from pathlib import Path

# ── constants ──────────────────────────────────────────────────────────────
DEFAULT_LOG_LEVEL = "INFO"


# ── logging ────────────────────────────────────────────────────────────────
def configure_logging(verbose: bool) -> None:
    """Configure process-local logging without assuming a log-file path."""
    level = logging.DEBUG if verbose else getattr(logging, DEFAULT_LOG_LEVEL)
    logging.basicConfig(level=level, format="%(levelname)s: %(message)s")


# ── argument parsing ───────────────────────────────────────────────────────
def parse_args() -> argparse.Namespace:
    """Parse and validate command-line arguments."""
    parser = argparse.ArgumentParser(
        description=__doc__,
        epilog="Example: %(prog)s --input example.txt --dry-run",
    )
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("-v", "--verbose", action="store_true")
    parser.add_argument("-V", "--version", action="version", version=f"%(prog)s {VERSION}")
    args = parser.parse_args()
    if not args.input.is_file():
        parser.error(f"input is not a file: {args.input}")
    return args


# ── entry point ────────────────────────────────────────────────────────────
def main() -> int:
    """Run the requested operation and return a process status."""
    args = parse_args()
    configure_logging(args.verbose)
    logging.info("would process %s (dry_run=%s)", args.input, args.dry_run)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except KeyboardInterrupt:
        raise SystemExit(130)
