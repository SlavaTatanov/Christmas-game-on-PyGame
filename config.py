"""
Конфигурация игрового окна, разрешение, FPS, цвета
"""
import random

W = 800  # Ширина
H = 600  # Высота

game_name = 'Игра'

FPS = 60
color = {'Black': (0, 0, 0), 'HotPink': (255, 105, 180), 'White': (255, 255, 255)}

"""
Геометрические размеры объектов
"""
# Игрок
player_size = int(W * 0.1)
player_speed = 10
x_player = 0

# Подарки
gift_size = int(W*0.09)
gift_speed = 2
x_gift = random.randint(0, W-gift_size)
y_gift = -40

"""
Разные игровые параметры
"""

keys = {}
