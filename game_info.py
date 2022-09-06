import data.game_objects as g_ob

user_status = {'score': 0, 'health': 3, 'gift_speed': 2, 'player_speed': 10}
gifts = []
player = []


def gifts_create():
    gift_1 = g_ob.Gift(-100)
    gifts.append(gift_1)
    gift_2 = g_ob.Gift(-300)
    gifts.append(gift_2)
    gift_3 = g_ob.Gift(-500)
    gifts.append(gift_3)


def player_create():
    current_player = g_ob.Player()
    player.append(current_player)
