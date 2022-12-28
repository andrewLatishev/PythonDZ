import pygame

pygame.init()

WIDTH = 1920
HEIGHT = 1080
FPS = 30
# Создаем игру и окно
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.SCALED | pygame.FULLSCREEN)
pygame.display.set_caption("Adventures of the Eskimo")
clock = pygame.time.Clock()

# загружаем картинку эскимоса
escimo_surf = pygame.image.load("D:\Adventures of Escimo\Escimo.png").convert_alpha()
escimo_surf.set_colorkey((0, 0, 0))
escimo_surf = escimo_surf.convert()
# загружаем фон
snow_surf = pygame.image.load("D:\Adventures of Escimo\snow.jpg").convert()
iglu_surf = pygame.image.load("D:\Adventures of Escimo\iglu.webp").convert_alpha()
# масштабирование картинки, если исходный размер не соответсвует требованиям. Формат записи
# //x - где x число во сколько раз надо уменьшить картинку,
# *x где x число во сколько раз надо увеличить картинку
escimo_surf = pygame.transform.scale(escimo_surf, (escimo_surf.get_width() // 2, escimo_surf.get_height() // 2))
snow_surf = pygame.transform.scale(snow_surf, (snow_surf.get_width() // 3, snow_surf.get_height() // 3))
pygame.display.update()
# Начальные координаты для эскимоса
x = 500
y = 750

# Цикл игры
running = True
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
        # ESC для выхода из игры
        # Управление эскимосом wasd
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_w and y >= 50:
                y -= 50
            if event.key == pygame.K_a and x >= 50:
                x -= 50
            if event.key == pygame.K_s and y <= 750:
                y += 50
            if event.key == pygame.K_d and x <= 1600:
                x += 50
            if y < 450:
                y = 400
        # обновление всех изображений
        screen.blit(snow_surf, (0, 0))
        screen.blit(escimo_surf, (x, y))
        pygame.display.update()
pygame.quit()
