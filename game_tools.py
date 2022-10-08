import data.game_objects as g_ob
import random
import requests
import pygame

# Данные перенести в main, файл сделать game tools, где просто набор инструментов для наполнения


def gifts_create(col=3, interval=600):
    res = []
    start_pos = interval
    for i in range(col):
        gift_y = start_pos - interval
        start_pos = gift_y
        gift = g_ob.Gift(gift_y, img=random.choice(['data/img/gift.png', 'data/img/gift2.png']))
        res.append(gift)
    return res


def data_upd(date: dict):
    for file, url in date.items():
        with open(file, 'wb') as fl:
            download = requests.get(url)
            fl.write(download.content)


def back_music(date: dict):
    for sound in date:
        pygame.mixer.music.load(sound)
        pygame.mixer.music.play(1)
