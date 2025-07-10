from zipfile import ZipFile


def get_size_summary(size):
    sizes = {"B": 1, "KB": 1024, "MB": 1024 ** 2, "GB": 1024 ** 3}
    for b, s in sizes.items():
        if 0 <= round(size / s) < 1024:
            return f'{round(size / s)} {b}'
    return f'{round(size / sizes["GB"])} GB'


with ZipFile('desktop.zip') as zip_file:
    for f in zip_file.infolist():
        file_name_list = f.filename.rstrip('/').split('/')
        intends = " " * (2 * (len(file_name_list) - 1))
        summary = " " + get_size_summary(f.file_size) if not f.is_dir() else ""
        print(f'{intends}{file_name_list[-1]}{summary}')
