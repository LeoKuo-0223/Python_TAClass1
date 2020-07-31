class Person:

    def __init__(self, name, weight, tall, fat_rate=1):
        self.name = name
        self.weight = weight
        self.rate = fat_rate
        self.tall = tall

    def eat(self):
        self.weight += self.rate

    def exercise(self):
        self.weight -= self.rate

    def speak(self):
        print('%s, weight: %d' % (self.name, self.weight))

    def healthcheck(self):
        return self.tall, self.weight


def bmi(tall, weight):
    value = weight / (tall / 100)**2
    return value


if __name__ == '__main__':
    p1 = Person(name='Kevin', weight=50, fat_rate=3, tall=160)
    p2 = Person(name='Leo', weight=60, fat_rate=1, tall=170)
    p3 = Person(name='Tom', weight=70, fat_rate=3, tall=165)
    p1.eat()
    p2.eat()
    p3.eat()
    p1.speak()
    p1.exercise()
    p2.speak()
    p3.exercise()
    p1.healthcheck()
