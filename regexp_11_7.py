import re

def start_stepik():
    article = '''Stepik (до августа 2016 года Stepic) — это образовательная платформа и конструктор онлайн-курсов!

Первые образовательные материалы были выпущены на Stepik 3 сентября 2013 года.
В январе 2016 года Stepik выпустил мобильные приложения под iOS и Android. В 2017 году разработаны мобильные приложения для изучения ПДД в адаптивном режиме для iOS и Android...

На октябрь 2020 года на платформе зарегистрировано 5 миллионов пользователей!
Stepik позволяет любому зарегистрированному пользователю создавать интерактивные обучающие уроки и онлайн-курсы, используя видео, тексты и разнообразные задачи с автоматической проверкой и моментальной обратной связью. 

Проект сотрудничает как с образовательными учреждениями, так и c индивидуальными преподавателями и авторами.  
Stepik сегодня предлагает онлайн-курсы от образовательных организаций, а также индивидуальных авторов!

Система автоматизированной проверки задач Stepik была использована в ряде курсов на платформе Coursera, включая курсы по биоинформатике от Калифорнийского университета в Сан-Диего и курс по анализу данных от НИУ «Высшая школа экономики»...

Stepik также может функционировать как площадка для проведения конкурсов и олимпиад, среди проведённых мероприятий — отборочный этап Олимпиады НТИ (2016—2020) (всероссийской инженерной олимпиады школьников, в рамках программы Национальная технологическая инициатива), онлайн-этап акции Тотальный диктант в 2017 году, соревнования по информационной безопасности StepCTF-2015...'''
    print(len(re.findall(r'^Stepik', article, re.M | re.I)))
    print(len(re.findall(r'\.{3}$|!$', article, re.M)))

def find_subword():
    phrase, word = input(), input()
    print(len(re.findall(fr'\B{word}\B', phrase)))

def find_words():
    phrase, word = input(), input()
    print(len(re.findall(fr'\b{word}\b', phrase)))

def br_us():
    word, phrase = input(), input()
    print(len(re.findall(fr'\b{word[:-2]}(se|ze)\b', phrase, re.I)))

def our_or():
    word, phrase = input(), input()
    print(len(re.findall(fr'\b{word[:-3]}(our|or)\b', phrase, re.I)))

def abbreviate(phrase: str) -> str:
    result = re.findall(r'\b[a-zA-Z]|\B[A-Z]', phrase)
    return ''.join(result).upper()

def html():
    import sys
    result = re.findall(r'<a href="(.+?)">(.+?)</a>', sys.stdin.read())
    [print(*i, sep=', ') for i in result]

def html_attrs():
    import sys
    i = re.findall(r'<([a-zA-Z0-9_-]+)(.*?)>', sys.stdin.read())
    tags = {}
    for m in sorted(i):
        tag = m[0]
        attrs = re.findall(r'\s*([a-zA-Z0-9_-]+)="[^"]*"', m[1])
        tags.setdefault(tag, set()).update(set(attrs))
    [print(f'{tag}:', ", ".join(sorted(attrs))) for tag, attrs in sorted(tags.items())]