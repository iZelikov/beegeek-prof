def likes():
    blog_posts = [{'Photos': 3, 'Likes': 21, 'Comments': 2},
                  {'Likes': 13, 'Comments': 2, 'Shares': 1},
                  {'Photos': 5, 'Likes': 33, 'Comments': 8, 'Shares': 3},
                  {'Comments': 4, 'Shares': 2},
                  {'Photos': 8, 'Comments': 1, 'Shares': 1},
                  {'Photos': 3, 'Likes': 19, 'Comments': 3}]
    total_likes = 0
    for post in blog_posts:
        try:
            total_likes += post['Likes']
        except KeyError:
            total_likes -= 1
    print(total_likes)


def fifth_letters():
    food = ['chocolate', 'chicken', 'corn', 'sandwich', 'soup', 'potatoes', 'beef', 'lox', 'lemonade']
    fifth = []
    for x in food:
        try:
            fifth.append(x[4])
        except IndexError:
            fifth.append('_')
    print(fifth)


def zero_pass():
    numbers = [6, 0, 36, 8, 2, 36, 0, 12, 60, 0, 45, 0, 3, 23]
    remainders = []
    for number in numbers:
        try:
            remainders.append(36 % number)
        except ZeroDivisionError:
            pass
    print(remainders)


