def eat():
    person['weight'] += -1


def ex():
    person['weight'] -= 1


def speak():
    print(person['name'])
    print(person['weight'])


person = {'name': 'Leo', 'weight': 60}
speak()
ex()
speak()
eat()
speak()