# Windows 파일·작업 잠금

잠금 기능을 구현·사용·검토할 때 읽습니다. 일반 문서 작업에 잠금이나 Kiro hook을 자동 도입하지 않습니다.

## 1. 작업 소유 잠금

- **§22 잠금:** Kiro disabled 파일·hook을 생성/삭제하지 않습니다. 현행 저장소 정책을 확인하고 동봉 Windows kiro-lock helper의 root·task token으로 acquire/check/release합니다. token은 현재 작업에서 생성해 유지하고 타인의 token을 채택하지 않습니다. R08 부분 생성 실패 정리는 실제 helper의 소유·inode 확인 범위로 검증해야 하며 손상/오래된 lock을 시간 경과만으로 삭제하지 않습니다. 참여자 공유와 일반 파일 byte lock은 별도 프로토콜입니다.

작업 잠금 helper가 필요한 경우 [kiro-lock 지침](../skills/kiro-lock.md)을 읽고 같은 폴더의 실제 scripts/lock.py를 사용합니다. help 성공은 acquire/check/release·경쟁·실패 검증이 아닙니다.

## 2. byte lock 예제

원문의 `fcntl.flock`·정상 해제 시 경로 삭제 예시는 Windows에서 실행하지 않습니다. 아래는 Windows의 프로세스 중복 실행 방지를 위한 **별도 byte-lock 패턴**입니다. 공유 경로를 유지하고 각 참여자가 같은 byte 위치를 잠급니다. OSError를 모두 “already running”으로 바꾸거나 종료 0으로 처리하지 않습니다.

```python
import msvcrt
import os
from contextlib import contextmanager


@contextmanager
def exclusive_file_lock(lock_file):
    """Hold one Windows byte lock on a persistent local path."""
    flags = os.O_RDWR | os.O_CREAT | getattr(os, 'O_BINARY', 0)
    fd = os.open(lock_file, flags, 0o600)
    with os.fdopen(fd, 'r+b') as lock_fp:
        if os.fstat(lock_fp.fileno()).st_size == 0:
            lock_fp.write(b'\x00')
            lock_fp.flush()
        lock_fp.seek(0)
        msvcrt.locking(lock_fp.fileno(), msvcrt.LK_NBLCK, 1)
        try:
            yield lock_fp
        finally:
            lock_fp.seek(0)
            msvcrt.locking(lock_fp.fileno(), msvcrt.LK_UNLCK, 1)
    # Keep the path so every cooperating process locks the same file.
```

실제 호출부는 `with exclusive_file_lock(LOCK_FILE):` 안에서 작업하고 I/O·권한·이미 잠긴 경우의 실제 실패를 로그/비정상 상태로 전달합니다. path 존재만으로 잠금 여부를 판단하지 않습니다. 이 패턴은 참여자·동일 경로·로컬 Windows byte locking 범위이며 symlink/reparse point·교체 writer·네트워크 FS·ACL·비협력 프로세스의 보장이나 동봉 kiro-lock helper와의 호환을 주장하지 않습니다. 실제 대상 적용 전 별도 정상·경쟁·예외 검증이 필요합니다.
