import os
import sys

# 지금 이 파일을 실행하고 있는 파이썬이 어느 것인지 확인한다
print("실행한 파이썬 :", sys.executable)
print("sys.prefix    :", sys.prefix)
print("base_prefix   :", sys.base_prefix)
print("venv 안인가   :", sys.prefix != sys.base_prefix)
print("VIRTUAL_ENV   :", os.environ.get("VIRTUAL_ENV"))
