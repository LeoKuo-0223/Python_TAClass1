from spiderman import Spiderman
from batman import Batman


class Sb(Spiderman, Batman):  # 繼承Person功能
    def __init__(self, *args, **kwargs):  # 後面兩格要寫
        super().__init__(*args, **kwargs)  # 一定要寫


if __name__ == '__main__':
    sb = Sb(wall=99, deposit=100, name='Kevin', weight=50, fat_rate=3, tall=160)
    sb.climb()
    sb.house()
