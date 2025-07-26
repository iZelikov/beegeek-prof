def greeting(name):
    print('Hello,', name)


greeting.publish = False
greeting.names = ['Timur', 'Arthur']

if greeting.publish:
    greeting('Dima')
if hasattr(greeting, 'names'):
    name = greeting.names[0]
    greeting(name)