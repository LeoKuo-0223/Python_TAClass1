from person_c import Person


class Spiderman(Person):
    def __init__(self, wall, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.wall = wall

    def climb(self):
        self.wall += 1
        print(self.wall)



if __name__ == '__main__':
    spider = Spiderman(wall=100, name='Tom', tall=170, weight=67)
    spider.speak()
    spider.climb()
