import config as cf
import random as rd
import pygame as pg


class GameObject:
    """
    Из него создается игрок, и он родительский для подарка
    """
    def __init__(self, y, color, size=0.1):
        self.size = size * cf.W
        self.color = color
        self.srf = pg.Surface((self.size, self.size))
        self.rect = self.srf.get_rect(topleft=(int(rd.randint(1, cf.W - self.size)), int(y - self.size)))

    def render(self, srf):
        srf.blit(self.srf, self.rect)
        self.srf.fill(self.color)


class Gift(GameObject):
    """
    Класс 'Подарок', предметы, которые предстоит ловить игроку. Имеет координаты, размер и методы когда игрок поймал
    предмет или предмет упал на землю
    """
    def move_up(self):
        self.rect.x = int(rd.randint(1, cf.W - self.size))
        self.rect.y = int(cf.H - cf.H*1.5)

    def catch(self, info):
        Gift.move_up(self)
        info['score'] += 1

    def crash(self, info):
        Gift.move_up(self)
        info['health'] -= 1
