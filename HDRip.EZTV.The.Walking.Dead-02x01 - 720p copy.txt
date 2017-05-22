file_size = os.path.getsize(file_path)
file_size_str = str(file_size) + ' B'
if file_size >= 1000 and file_size < 1000000 :
    file_size_str = str(file_size / 1000) + ' KB'
elif file_size >= 1000000 and file_size < 1000000000 :
    file_size_str = str(file_size / 1000000) + ' MB'
elif file_size >= 1000000000 :
    file_size_str = str(file_size / 1000000000) + ' GB'
print('File ' + file_path + ", size " + file_size_str)