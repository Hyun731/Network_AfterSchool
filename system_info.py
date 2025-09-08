import os
import platform
import datetime

print("=== Raspberry Pi System Info ===")
print("날짜:", datetime.datetime.now())
print("운영체제:", platform.system(), platform.release())
print("아키텍처:", platform.machine())
print("파이썬 버전:", platform.python_version())
print("현재 사용자:", os.getlogin())


