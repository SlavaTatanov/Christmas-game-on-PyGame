import data.game_objects as g_ob
import config as cf

# Данные перенести в main, файл сделать game tools, где просто набор инструментов для наполнения


def gifts_create(col=3, interval=600):
    res = []
    start_pos = interval
    for i in range(col):
        gift_y = start_pos - interval
        start_pos = gift_y
        gift = g_ob.Gift(gift_y, cf.color['HotPink'])
        res.append(gift)
    return res
