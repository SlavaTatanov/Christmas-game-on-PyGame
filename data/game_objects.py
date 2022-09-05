import config as cf
import game_info as gi
import random as rd


class Gift:
    """
    Класс 'Подарок', предметы, которые предстоит ловить игроку. Имеет координаты, размер и методы когда игрок поймал
    предмет или предмет упал на землю
    """
    size = 0.09 * cf.W

    def __init__(self, y):
        self.x = int(rd.randint(1, cf.W - Gift.size))
        self.y = y

    def move_up(self):
        self.x = int(rd.randint(1, cf.W - Gift.size))
        self.y = int(0 - Gift.size*1.5)

    def catch(self):
        Gift.move_up(self)
        gi.user_status['score'] += 1

    def crash(self):
        Gift.move_up(self)
        gi.user_status['health'] -= 1


