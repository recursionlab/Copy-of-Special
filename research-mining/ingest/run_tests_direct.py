"""Fallback test runner: import test module and run functions directly if pytest discovery behaves oddly."""
from importlib import import_module

mod = import_module('test_dedupe_cluster')

funcs = [getattr(mod, name) for name in dir(mod) if name.startswith('test_')]
print(f"Found {len(funcs)} test functions")
failed = 0
for f in funcs:
    try:
        f()
        print(f"PASS {f.__name__}")
    except Exception as e:
        failed += 1
        print(f"FAIL {f.__name__}: {e}")

print('Failed:', failed)

if failed:
    raise SystemExit(1)
