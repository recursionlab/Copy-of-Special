import sys
import io
import pytest

buf = io.StringIO()
sys_stdout = sys.stdout
sys.stdout = buf
try:
    rc = pytest.main(['test_dedupe_cluster.py', '-q', '-rA'])
finally:
    sys.stdout = sys_stdout

with open('pytest_capture.txt', 'w', encoding='utf-8') as f:
    f.write(buf.getvalue())

print('WROTE pytest_capture.txt, rc=', rc)
