import coverage
import pytest

cov = coverage.Coverage(data_file='.coverage', source=['research-mining/ingest'])
cov.start()
rc = pytest.main(['test_dedupe_cluster.py', '-q'])
cov.stop()
cov.save()
cov.xml_report(outfile='../coverage.xml')
print('cov rc=', rc)
