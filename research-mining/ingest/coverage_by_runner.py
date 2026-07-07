# Run test functions under coverage and write coverage.xml to repo root
from coverage import Coverage
from importlib import import_module
import os

cov = Coverage(data_file=os.path.join(os.path.dirname(__file__), '..', '.coverage_runner'), source=[os.path.join(os.path.dirname(__file__))])
cov.start()

mod = import_module('test_dedupe_cluster')
funcs = [getattr(mod, name) for name in dir(mod) if name.startswith('test_')]
failed = 0
for f in funcs:
    try:
        f()
    except Exception as e:
        failed += 1
        print('Test failed', f.__name__, e)

cov.stop()
cov.save()
# write XML to repo root
out_xml = os.path.join(os.path.dirname(__file__), '..', 'coverage.xml')
try:
    cov.xml_report(outfile=out_xml)
    print('WROTE', out_xml)
except Exception as e:
    print('XML report error', e)

print('FAILED_COUNT=', failed)
