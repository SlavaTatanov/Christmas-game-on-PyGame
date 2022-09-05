import pygame
import config
import data.game_objects as g_ob
import game_info as gi

pygame.init()
gi.gifts_create()

base_surface = pygame.display.set_mode((config.W, config.H))
pygame.display.set_caption(config.game_name)
clock = pygame.time.Clock()  # Частота отрисовки

player = pygame.Surface((config.player_size, config.player_size))
gift = pygame.Surface((g_ob.Gift.size, g_ob.Gift.size))

while True:
    keys = pygame.key.get_pressed()  # Отслеживает нажатые клавиши
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        # Данный блок отлавливает нажатия клавиш игроком (если нажаты обе, движется в сторону последней нажатой)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                config.keys[pygame.K_LEFT] = True
                if len(config.keys) >= 2:
                    del config.keys[pygame.K_RIGHT]
            if event.key == pygame.K_RIGHT:
                config.keys[pygame.K_RIGHT] = True
                if len(config.keys) >= 2:
                    del config.keys[pygame.K_LEFT]
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                if pygame.K_LEFT in config.keys:
                    del config.keys[pygame.K_LEFT]
                if keys[pygame.K_RIGHT]:
                    config.keys[pygame.K_RIGHT] = True
            if event.key == pygame.K_RIGHT:
                if pygame.K_RIGHT in config.keys:
                    del config.keys[pygame.K_RIGHT]
                if keys[pygame.K_LEFT]:
                    config.keys[pygame.K_LEFT] = True

    # Данный блок отвечает за движения игрока и блокирует его движение за пределы экрана
    if pygame.K_LEFT in config.keys:
        if config.x_player > 0:
            config.x_player -= config.player_speed
        else:
            config.x_player = 0
    if pygame.K_RIGHT in config.keys:
        if config.x_player < (config.W - config.player_size):
            config.x_player += config.player_speed
        else:
            config.x_player = config.W - config.player_size

    # Отслеживание подарка
    for i in range(len(gi.gifts)):
        if gi.gifts[i].y == config.H - g_ob.Gift.size:
            gi.gifts[i].crash()

    # Падение подарка
    for i in range(len(gi.gifts)):
        gi.gifts[i].y += config.gift_speed

    # Отрисовка объектов

    base_surface.fill(config.color['Black'])  # Постоянно закрашивает фон
    # Игрок
    base_surface.blit(player, (config.x_player, config.H - config.player_size))  # Отрисовка поверхности игрока
    player.fill(config.color['White'])
    # Подарки
    for i in range(len(gi.gifts)):
        base_surface.blit(gift, (gi.gifts[i].x, gi.gifts[i].y))
        gift.fill(config.color['HotPink'])

    # Обновление объектов на экране
    pygame.display.update()
    clock.tick(config.FPS)
