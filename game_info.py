import data.game_objects as g_ob

# Данные перенести в main, файл сделать game tools, где просто набор инструментов для наполнения
player = []  # Игрок


def gifts_create():
    res = []
    gift_1 = g_ob.Gift(-100)
    res.append(gift_1)
    gift_2 = g_ob.Gift(-300)
    res.append(gift_2)
    gift_3 = g_ob.Gift(-500)
    res.append(gift_3)
    return res


def player_create():
    current_player = g_ob.Player()
    player.append(current_player)
