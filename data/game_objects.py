import config as cf
import random as rd
import pygame as pg


class Gift:
    """
    Класс 'Подарок', предметы, которые предстоит ловить игроку. Имеет координаты, размер и методы когда игрок поймал
    предмет или предмет упал на землю
    """
    SIZE = 0.09 * cf.W

    def __init__(self, y):
        self.srf = pg.Surface((Gift.SIZE, Gift.SIZE))
        self.rect = self.srf.get_rect(topleft=(int(rd.randint(1, cf.W - Gift.SIZE)), y))

    def move_up(self):
        self.rect.x = int(rd.randint(1, cf.W - Gift.SIZE))
        self.rect.y = int(0 - Gift.SIZE*1.5)

    def catch(self, info):
        Gift.move_up(self)
        info['score'] += 1

    def crash(self, info):
        Gift.move_up(self)
        info['health'] -= 1


class Player:
    """
    Класс игрока
    """
    SIZE = 0.1 * cf.W

    def __init__(self):
        self.srf = pg.Surface((Player.SIZE, Player.SIZE))
        self.rect = self.srf.get_rect(topleft=(int(rd.randint(1, cf.W - Player.SIZE)), int(cf.H - Player.SIZE)))
