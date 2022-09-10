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


class TextLabel:
    """
    Текстовые лейблы (отображение счета и прочее)
    """
    def __init__(self, font, font_size, message, coordinates, color, center=False):
        self.message = message
        self.coordinates = coordinates
        self.color = color
        self.center = center
        self.font = pg.font.SysFont(font, font_size)
        self.label_srf = None
        self.label_rect = None

    def render(self, base_surf):
        self.label_srf = self.font.render(self.message, True, self.color)
        if self.center:
            self.label_rect = self.label_srf.get_rect(center=self.coordinates)
        else:
            self.label_rect = self.label_srf.get_rect(topleft=self.coordinates)
        base_surf.blit(self.label_srf, self.label_rect)
