import pygame
import config
import game_info as gi
import data.game_objects as g_ob

pygame.init()

base_surface = pygame.display.set_mode((config.W, config.H))
pygame.display.set_caption(config.game_name)
clock = pygame.time.Clock()  # Частота кадров


def final_score_display(final_score):
    base_surface.fill(config.color['Black'])
    score_result = g_ob.TextLabel('arial', 40, (config.W//2, config.H//2), config.color['White'], True)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game()
        # Отрисовка финального счета
        score_result.render(f'Финальный счет: {final_score["score"]}', base_surface)
        # Общее обновление экрана
        pygame.display.update()
        clock.tick(config.FPS)


def game():
    move_direction = {'LEFT': False, 'RIGHT': False}  # Контролирует нажатую клавишу
    user_status = {'score': 0, 'health': 3, 'gift_speed': 2, 'player_speed': 12, 'rank': 10}
    gifts = gi.gifts_create()
    player = g_ob.GameObject(config.H)
    score_label = g_ob.TextLabel('arial', 17, (10, 10), config.color['White'])
    objects = gifts + [player]  # Общий список объектов для рендера
    while True:
        keys = pygame.key.get_pressed()  # Отслеживает нажатые клавиши
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            # Данный блок отлавливает нажатия клавиш игроком (если нажаты обе, движется в сторону последней нажатой)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    move_direction['LEFT'] = True
                    # Если во время нажатия <- уже зажата -> все равно переключает движение на - влево
                    if move_direction['RIGHT']:
                        move_direction['RIGHT'] = False
                if event.key == pygame.K_RIGHT:
                    move_direction['RIGHT'] = True
                    # Если во время нажатия -> уже зажата <- все равно переключает движение на - вправо
                    if move_direction['LEFT']:
                        move_direction['LEFT'] = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    if move_direction['LEFT']:
                        move_direction['LEFT'] = False
                    # Контроль уже зажатой клавиши
                    if keys[pygame.K_RIGHT]:
                        move_direction['RIGHT'] = True
                if event.key == pygame.K_RIGHT:
                    if move_direction['RIGHT']:
                        move_direction['RIGHT'] = False
                    # Контроль уже зажатой клавиши
                    if keys[pygame.K_LEFT]:
                        move_direction['LEFT'] = True

        # Данный блок отвечает за движения игрока и блокирует его движение за пределы экрана
        if move_direction['LEFT']:
            if player.rect.x > 0:
                player.rect.x -= user_status['player_speed']
            else:
                player.rect.x = 0
        if move_direction['RIGHT']:
            if player.rect.x < (config.W - player.size):
                player.rect.x += user_status['player_speed']
            else:
                player.rect.x = config.W - player.size

        # Отслеживание подарка
        for i in gifts:
            # Проверка падения
            if i.rect.y > config.H:
                i.crash(user_status)
            # Проверка поимки подарка игроком
            if pygame.Rect.colliderect(i.rect, player.rect):
                i.catch(user_status)

        # Падение подарка
        for i in gifts:
            i.rect.y += user_status['gift_speed']
        # Проверки
        if user_status['health'] <= 0:
            final_score_display(user_status)
        # Регулировка скорости
        if user_status['score'] > user_status['rank']:
            user_status['rank'] += 10
            user_status['gift_speed'] += 1

        # Отрисовка объектов
        base_surface.fill(config.color['Black'])  # Постоянно закрашивает фон
        # Отрисовка игрока и подарков (оба класса имеют один метод)
        for i in objects:
            i.render(base_surface)
        # Отрисовка счета
        score_label.render(f'Счет: {user_status["score"]} Здоровье: {user_status["health"]}', base_surface)
        # Обновление объектов на экране
        pygame.display.update()
        clock.tick(config.FPS)


game()
