import pygame
import config
import game_info as gi

pygame.init()
gi.gifts_create()
gi.player_create()

base_surface = pygame.display.set_mode((config.W, config.H))
pygame.display.set_caption(config.game_name)
clock = pygame.time.Clock()  # Частота отрисовки


def menu():
    base_surface.fill(config.color['Black'])
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        pygame.display.update()
        clock.tick(config.FPS)


def game():
    length_gifts = len(gi.gifts)
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
            if gi.player[0].rect.x > 0:
                gi.player[0].rect.x -= gi.user_status['player_speed']
            else:
                gi.player[0].rect.x = 0
        if pygame.K_RIGHT in config.keys:
            if gi.player[0].rect.x < (config.W - gi.player[0].SIZE):
                gi.player[0].rect.x += gi.user_status['player_speed']
            else:
                gi.player[0].rect.x = config.W - gi.player[0].SIZE

        # Отслеживание подарка
        for i in range(length_gifts):
            # Проверка падения
            if gi.gifts[i].rect.y > config.H:
                gi.gifts[i].crash()
            # Проверка поимки подарка игроком
            if pygame.Rect.colliderect(gi.gifts[i].rect, gi.player[0].rect):
                gi.gifts[i].catch()

        # Падение подарка
        for i in range(length_gifts):
            gi.gifts[i].rect.y += gi.user_status['gift_speed']
        # Проверки
        if gi.user_status['health'] <= 0:
            menu()

        if gi.user_status['score'] > gi.user_status['rank']:
            gi.user_status['rank'] += 10
            gi.user_status['gift_speed'] += 1

        # Отрисовка объектов

        base_surface.fill(config.color['Black'])  # Постоянно закрашивает фон
        # Игрок
        base_surface.blit(gi.player[0].srf, gi.player[0].rect)  # Отрисовка поверхности игрока
        gi.player[0].srf.fill(config.color['White'])
        # Подарки
        for i in range(length_gifts):
            base_surface.blit(gi.gifts[i].srf, gi.gifts[i].rect)
            gi.gifts[i].srf.fill(config.color['HotPink'])

        # Обновление объектов на экране
        pygame.display.update()
        clock.tick(config.FPS)


game()
