import config as cf
import game_info as gi
import random as rd
import pygame as pg


class Gift:
    """
    Класс 'Подарок', предметы, которые предстоит ловить игроку. Имеет координаты, размер и методы когда игрок поймал
    предмет или предмет упал на землю
    """
    SIZE = 0.09 * cf.W

    def __init__(self, y):
        self.x = int(rd.randint(1, cf.W - Gift.SIZE))
        self.y = y
        self.srf = pg.Surface((Gift.SIZE, Gift.SIZE))

    def move_up(self):
        self.x = int(rd.randint(1, cf.W - Gift.SIZE))
        self.y = int(0 - Gift.SIZE*1.5)

    def catch(self):
        Gift.move_up(self)
        gi.user_status['score'] += 1

    def crash(self):
        Gift.move_up(self)
        gi.user_status['health'] -= 1


class Player:
    """
    Класс игрока
    """
    SIZE = 0.1 * cf.W

    def __init__(self):
        self.x = int(rd.randint(1, cf.W - Player.SIZE))
        self.y = int(cf.H - Player.SIZE)
        self.srf = pg.Surface((Player.SIZE, Player.SIZE))
