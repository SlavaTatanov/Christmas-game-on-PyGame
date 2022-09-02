import pygame
import config
import random

pygame.init()

base_surface = pygame.display.set_mode((config.W, config.H))
pygame.display.set_caption(config.game_name)
clock = pygame.time.Clock()  # Частота отрисовки

player = pygame.Surface((config.player_size, config.player_size))
gift = pygame.Surface((config.gift_size, config.gift_size))

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
    if config.y_gift == config.H - config.gift_size:
        config.y_gift = -40
        config.x_gift = random.randint(0, config.W-config.gift_size)

    # Падение подарка
    config.y_gift += config.gift_speed

    # Отрисовка объектов

    base_surface.fill(config.color['Black'])  # Постоянно закрашивает фон
    # Игрок
    base_surface.blit(player, (config.x_player, config.H - config.player_size))  # Отрисовка поверхности игрока
    player.fill(config.color['White'])
    # Подарок 1
    base_surface.blit(gift, (config.x_gift, config.y_gift))
    gift.fill(config.color['HotPink'])

    # Обновление объектов на экране
    pygame.display.update()
    clock.tick(config.FPS)
