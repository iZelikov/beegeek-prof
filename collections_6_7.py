from collections import Counter

def ext_counter():
    files = ['emoji_smile.jpeg', 'city-of-the-sun.mp3', 'dhook_hw.json', 'sample.xml',
             'teamspeak3.exe', 'project_module3.py', 'math_lesson3.mp4', 'old_memories.mp4',
             'spiritfarer.exe', 'backups.json', 'python_for_beg1.mp4', 'emoji_angry.jpeg',
             'exam_results.csv', 'project_main.py', 'classes.csv', 'plants.xml',
             'cant-help-myself.mp3', 'microsoft_edge.exe', 'steam.exe', 'math_lesson4.mp4',
             'city.jpeg', 'bad-disease.mp3', 'beauty.jpeg', 'hollow_knight_silksong.exe',
             'whatsapp.exe', 'photoshop.exe', 'telegram.exe', 'yandex_browser.exe',
             'math_lesson7.mp4', 'students.csv', 'emojis.zip', '7z.zip',
             'bones.mp3', 'python3.zip', 'dhook_lsns.json', 'carl_backups.json',
             'forest.jpeg', 'python_for_pro8.mp4', 'yandexdisc.exe', 'but-you.mp3',
             'project_module1.py', 'nothing.xml', 'flowers.jpeg', 'grades.csv',
             'nvidia_gf.exe', 'small_txt.zip', 'project_module2.py', 'tab.csv',
             'note.xml', 'sony_vegas11.exe', 'friends.jpeg', 'data.pkl']
    ext_count = Counter(map(lambda x: x.split('.')[-1], files))
    [print(f'{ext}: {count}') for ext, count in sorted(ext_count.items())]

def count_occurences(word: str, words: str):
    words_counter = Counter(map(str.lower, words.split()))
    return words_counter[word.lower()]

def shop_list():
    [print(f"{k}: {v}") for k, v in sorted(Counter((input().split(','))).items())]

def us_price():
    product_list = sorted(Counter((input().split(','))).items())
    longest_name = len(max(product_list, key=lambda x: len(x[0]))[0])
    for p, count in product_list:
        price = sum(ord(l) * c for l, c in Counter(p).items() if l.isalpha())
        print(f'{p:{longest_name}}: {price} UC x {count} = {price * count} UC')

def python_zen():
    with open('pythonzen.txt') as zen:
        [print(f'{l}: {c}') for l, c in sorted(Counter(zen.read().lower()).items()) if l.isalpha()]