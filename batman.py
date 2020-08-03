from person_c import Person


class Batman(Person):  # 繼承Person功能
    def __init__(self, deposit, *args, **kwargs):  # 後面兩格要寫
        super().__init__(*args, **kwargs)  # 一定要寫
        self.deposit = deposit

    def house(self):
        print('buy house')

if __name__ == '__main__':
    b = Batman(deposit=10000, name='Kevin', weight=50, fat_rate=3, tall=160)
