from functools import reduce
from itertools import groupby, tee, chain, pairwise, accumulate
from collections import namedtuple


def group_by_height():
    Person = namedtuple('Person', ['name', 'age', 'height'])
    persons = [Person('Tim', 63, 193), Person('Eva', 47, 158),
               Person('Mark', 71, 172), Person('Alex', 45, 193),
               Person('Jeff', 63, 193), Person('Ryan', 41, 184),
               Person('Ariana', 28, 158), Person('Liam', 69, 193)]
    [_ for _ in map(lambda x: (print(f'{x[0]}: ', end=""), print(*sorted(p.name for p in x[1]), sep=', ')),
                    groupby(sorted(persons, key=lambda p: p.height), key=lambda p: p.height))]


def max_name():
    Student = namedtuple('Student', ['surname', 'name', 'grade'])
    students = [Student('Гагиев', 'Александр', 10), Student('Дедегкаев', 'Илья', 11), Student('Кодзаев', 'Георгий', 10),
                Student('Набокова', 'Алиса', 11), Student('Кораев', 'Артур', 10), Student('Шилин', 'Александр', 11),
                Student('Уртаева', 'Илина', 11), Student('Салбиев', 'Максим', 10), Student('Капустин', 'Илья', 11),
                Student('Гудцев', 'Таймураз', 11), Student('Перчиков', 'Максим', 10), Student('Чен', 'Илья', 11),
                Student('Елькина', 'Мария', 11), Student('Макоев', 'Руслан', 11), Student('Албегов', 'Хетаг', 11),
                Student('Щербак', 'Илья', 10), Student('Идрисов', 'Баграт', 11), Student('Гапбаев', 'Герман', 10),
                Student('Цивинская', 'Анна', 10), Student('Туткевич', 'Юрий', 11), Student('Мусиков', 'Андраник', 11),
                Student('Гадзиев', 'Георгий', 11), Student('Белов', 'Юрий', 11), Student('Акоева', 'Диана', 11),
                Student('Денисов', 'Илья', 11), Student('Букулова', 'Диана', 10), Student('Акоева', 'Лера', 11)]
    students.sort(key=lambda s: s.name)
    print(max(groupby(students, key=lambda s: s.name), key=lambda s: sum(1 for _ in s[1]))[0])


def sort_len():
    [(print(f'{k} -> ', end=''), print(*sorted(v), sep=', ')) for k, v in
     groupby(sorted(input().split(' '), key=len), key=len)]


def group_tasks():
    tasks = [('Отдых', 'поспать днем', 3),
             ('Ответы на вопросы', 'ответить на вопросы в дискорде', 1),
             ('ЕГЭ Математика', 'доделать курс по параметрам', 1),
             ('Ответы на вопросы', 'ответить на вопросы в курсах', 2),
             ('Отдых', 'погулять вечером', 4),
             ('Курс по ооп', 'обсудить темы', 1),
             ('Урок по groupby', 'добавить задачи на программирование', 3),
             ('Урок по groupby', 'написать конспект', 1),
             ('Отдых', 'погулять днем', 2),
             ('Урок по groupby', 'добавить тестовые задачи', 2),
             ('Уборка', 'убраться в ванной', 2),
             ('Уборка', 'убраться в комнате', 1),
             ('Уборка', 'убраться на кухне', 3),
             ('Отдых', 'погулять утром', 1),
             ('Курс по ооп', 'обсудить задачи', 2)]
    tasks.sort(key=lambda x: (x[0], x[2]))
    for task, parts in groupby(tasks, key=lambda x: x[0]):
        print(f'{task}:')
        for part in parts:
            print(f"\t{part[2]}. {part[1]}")
        print()


def group_anagrams(words: list[str]):
    sort_key = lambda x: sorted(x)
    yield from map(lambda x: tuple(x[1]), groupby(sorted(words, key=sort_key), key=sort_key))


def ranges(numbers: list[int]):
    result = []
    m = groupby(enumerate(numbers), key= lambda x: x[1]-x[0])
    for i in m:
        s = next(i[1])
        result.append(reduce(lambda a, b: (a[0], b[1]), i[1], (s[1], s[1])))
    return result

numbers = [1, 3, 4, 5, 7, 8, 10, 12, 14, 17, 18, 33]
print(ranges(numbers))
