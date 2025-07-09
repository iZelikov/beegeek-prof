from zipfile import ZipFile

with ZipFile('test.zip') as z:
    # print(*z.infolist(), sep="\n")
    info = z.infolist()
    print(info[6].file_size)                # размер начального файла в байтах
    print(info[6].compress_size)            # размер сжатого файла в байтах
    print(info[6].filename)                 # имя файла
    print(info[6].date_time)                # дата изменения файла