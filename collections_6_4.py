from collections import namedtuple


def fruit():
    Fruit = namedtuple('Fruit', ['name', 'color', 'vitamins'])


def extended_game():
    Game = namedtuple('Game', 'name developer publisher')
    ExtendedGame = namedtuple('ExtendedGame', Game._fields + ('release_date', 'price'))


def animals_list():
    import pickle
    Animal = namedtuple('Animal', ['name', 'family', 'sex', 'color'])
    with open('data.pkl', 'rb') as file:
        animals = pickle.load(file)
    for animal in animals:
        [print(f'{f}: {v}') for f, v in zip(Animal._fields, animal)]
        print()


def users_plan():
    User = namedtuple('User', ['name', 'surname', 'email', 'plan'])
    users = [User('Mary', 'Griffin', 'sonnen@yahoo.com', 'Basic'),
             User('Brenda', 'Young', 'retoh@outlook.com', 'Silver'),
             User('Kathleen', 'Lyons', 'balchen@att.net', 'Gold'),
             User('Pamela', 'Hicks', 'corrada@sbcglobal.net', 'Silver'),
             User('William', 'Townsend', 'kosact@verizon.net', 'Gold'),
             User('Clayton', 'Morris', 'berserk@yahoo.com', 'Silver'),
             User('Dorothy', 'Dennis', 'sequin@live.com', 'Gold'),
             User('Tyler', 'Walker', 'noahb@comcast.net', 'Basic'),
             User('Joseph', 'Moore', 'ylchang@sbcglobal.net', 'Silver'),
             User('Kenneth', 'Richardson', 'tbusch@me.com', 'Bronze'),
             User('Stephanie', 'Bush', 'neuffer@live.com', 'Gold'),
             User('Gregory', 'Hughes', 'juliano@att.net', 'Basic'),
             User('Tracy', 'Wallace', 'sblack@me.com', 'Silver'),
             User('Russell', 'Smith', 'isaacson@comcast.net', 'Bronze'),
             User('Megan', 'Patterson', 'hoangle@outlook.com', 'Basic')]
    plans = ['Gold', 'Silver', 'Bronze', 'Basic']
    users.sort(key=lambda x: (plans.index(x.plan), x.e))
    [print(f'{u.name} {u.surname}\n  Email: {u.email}\n  Plan: {u.plan}\n') for u in users]


def sort_friends():
    import csv
    from datetime import datetime

    d_format = '%d.%m.%Y %H:%M'
    with open('meetings.csv', encoding='utf-8') as file:
        friends = csv.DictReader(file)
        l = sorted(friends, key=lambda f: datetime.strptime(f'{f['meeting_date']} {f['meeting_time']}', d_format))
    [print(f"{f['surname']} {f['name']}") for f in l]

