import sys
from importlib import import_module

mod = import_module('test_dedupe_cluster')
funcs = [getattr(mod, name) for name in dir(mod) if name.startswith('test_')]
lines = []
failed = 0
for f in funcs:
    try:
        f()
        lines.append(f'PASS {f.__name__}')
    except Exception as e:
        failed += 1
        lines.append(f'FAIL {f.__name__}: {e}')

lines.append(f'FAILED_COUNT={failed}')
with open('direct_test_log.txt', 'w', encoding='utf-8') as fh:
    fh.write('\n'.join(lines))
print('WROTE direct_test_log.txt')
