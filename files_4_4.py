from zipfile import ZipFile


def zip_length():
    with ZipFile('workbook.zip') as zip_file:
        print(len(list(filter(lambda f: not f.is_dir(), zip_file.infolist()))))


def compressed_size():
    with ZipFile('workbook.zip') as zip_file:
        uncompressed = 0
        compressed = 0
        for file in zip_file.infolist():
            uncompressed += file.file_size
            compressed += file.compress_size

        print(f"Объем исходных файлов: {uncompressed} байт(а)")
        print(f"Объем сжатых файлов: {compressed} байт(а)")

def best_compression():
    with ZipFile('workbook.zip') as zip_file:
        print(max(zip_file.infolist(),
                  key=lambda x: x.file_size / x.compress_size if x.compress_size > 0 else 0).filename.split('/')[-1])


def filter_date():
    from datetime import datetime
    with ZipFile('workbook.zip') as zip_file:
        f = filter(lambda x: datetime(*x.date_time) > datetime(2021, 11, 30, 14, 22, 0) and not x.is_dir(),
                   zip_file.infolist())
        print(*sorted([x.filename.split('/')[-1] for x in f]), sep="\n")


def formated_output():
    from datetime import datetime
    with ZipFile('workbook.zip') as zip_file:
        f_list = sorted(filter(lambda f: not f.is_dir(), zip_file.infolist()), key=lambda f: f.filename.split('/')[-1])
        for f in f_list:
            print(f.filename.split('/')[-1])
            print(f'  Дата модификации файла: {datetime(*f.date_time)}')
            print(f'  Объем исходного файла: {f.file_size} байт(а)')
            print(f'  Объем сжатого файла: {f.compress_size} байт(а)')
            print()


def write_zip():
    file_names = ['how to prove.pdf', 'fipi_demo_2022.pdf', 'Hollow Knight Silksong.exe',
                  'code.jpeg', 'stepik.png', 'readme.txt', 'shopping_list.txt',
                  'Alexandra Savior – Crying All the Time.mp3', 'homework.py', 'test.py']
    with ZipFile('files.zip', 'w') as zip_file:
        for f in file_names:
            zip_file.write(f)


def write_zip_100b():
    import os.path
    file_names = ['how to prove.pdf', 'fipi_demo_2022.pdf', 'Hollow Knight Silksong.exe',
                  'code.jpeg', 'stepik.png', 'readme.txt', 'shopping_list.txt',
                  'Alexandra Savior – Crying All the Time.mp3', 'homework.py', 'test.py']
    with ZipFile('files.zip', 'a') as zip_file:
        for f in file_names:
            if os.path.getsize(f) < 100:
                zip_file.write(f)

def extract_this(zip_name, *args):
    with ZipFile(zip_name) as zip_file:
        if args:
            for f in args:
                zip_file.extract(f)
        else:
            zip_file.extractall()

def arsenal_players():
    import json
    from json import JSONDecodeError
    def is_correct_json(string):
        try:
            json.loads(string)
            return True
        except JSONDecodeError:
            return False

    arsenal = []
    with ZipFile('data.zip') as zip_file:
        for file_name in zip_file.namelist():
            if file_name.split('.')[-1] == 'json':
                with zip_file.open(file_name) as file:
                    try:
                        s = file.read().decode('utf-8')
                        if is_correct_json(s):
                            f = json.loads(s)
                            arsenal.append((f["first_name"], f["last_name"])) if f['team'] == 'Arsenal' else print(end="")
                    except:
                        pass
    [print(*player) for player in sorted(arsenal)]


def hr_size(n, k = 0):
    return f"{round(n)} {['B', 'KB', 'MB', 'GB', 'TB'][k]}" if n < 1024 else hr_size(n / 1024, k + 1)


def zip_structure():
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
