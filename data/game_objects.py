import config as cf
import random as rd
import pygame as pg


class GameObject:
    """
    Из него создается игрок, и он родительский для подарка
    """
    def __init__(self, y, size=0.1, img='data/img/gift.png'):
        self.size = size * cf.W
        self.img = pg.image.load(img).convert_alpha()
        self.img = pg.transform.scale(self.img, (self.size, self.size))
        self.rect = self.img.get_rect(topleft=(int(rd.randint(1, cf.W - self.size)), int(y - self.size)))

    def render(self, srf):
        srf.blit(self.img, self.rect)


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
    def __init__(self, font, font_size, coordinates, color, center=False):
        self.coordinates = coordinates
        self.color = color
        self.center = center
        self.font = pg.font.SysFont(font, font_size)
        self.label_srf = None
        self.label_rect = None

    def render(self, message, base_surf):
        self.label_srf = self.font.render(message, True, self.color)
        if self.center:
            self.label_rect = self.label_srf.get_rect(center=self.coordinates)
        else:
            self.label_rect = self.label_srf.get_rect(topleft=self.coordinates)
        base_surf.blit(self.label_srf, self.label_rect)
