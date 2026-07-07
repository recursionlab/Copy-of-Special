from coverage import Coverage
cov = Coverage(data_file='..\\.coverage')
try:
    cov.load()
    data = cov.get_data()
    files = data.measured_files()
    print('measured files count:', len(files))
    for f in files:
        print(f)
except Exception as e:
    print('ERROR', e)
