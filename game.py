import pygame
from player import *
from blocks import *
from pyganim import *

# window
WIN_WIDTH = 800  # Ширина создаваемого окна
WIN_HEIGHT = 640  # Высота
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)  # Группируем ширину и высоту в одну переменную
BACKGROUND_COLOR = (0, 64, 0)
NAME = "Battle of one"
ANIMATION_DELAY = 0.1 # скорость смены кадров


def main():
    pygame.init()  # Инициация PyGame, обязательная строчка
    screen = pygame.display.set_mode(DISPLAY)  # Создаем окошко
    pygame.display.set_caption(NAME)  # Пишем в шапку
    surf = pygame.Surface(DISPLAY)
    surf.fill(BACKGROUND_COLOR)

    hero = Player(55, 55)  # создаем героя по (x,y) координатам
    left = right = False  # по умолчанию — стоим
    up = False

    entities = pygame.sprite.Group()  # Все объекты
    platforms = []  # то, во что мы будем врезаться или опираться
    entities.add(hero)

    level = ["_________________________",
             "_                       _",
             "_                       _",
             "_                       _",
             "_                       _",
             "_                       _",
             "_                       _",
             "_                   _____",
             "_                       _",
             "_                       _",
             "_                 _     _",
             "_    ____               _",
             "_                       _",
             "_                _      _",
             "_    __                 _",
             "_                       _",
             "_          _________    _",
             "_                       _",
             "_                       _",
             "_________________________"]
    timer = pygame.time.Clock()

    x = y = 0  # координаты
    for row in level:
        for col in row:
            if col == "_":
                platform = Platform(x, y)
                entities.add(platform)
                platforms.append(platform)
            x = x + PLATFORM_WIDTH  # блоки платформы ставятся на ширине блоков
        y = y + PLATFORM_HEIGHT  # то же самое и с высотой
        x = 0  # на каждой новой строчке начинаем с нуля

    while 1:  # Основной цикл программы
        timer.tick(60) #fps = 60


        for e in pygame.event.get():
            keys = pygame.key.get_pressed()
            if e.type == KEYDOWN and e.key == K_UP:
                up = True

            if e.type == KEYUP and e.key == K_UP:
                up = False

            if e.type == KEYDOWN and e.key == K_LEFT:
                left = True
            if e.type == KEYDOWN and e.key == K_RIGHT:
                right = True

            if e.type == KEYUP and e.key == K_RIGHT:
                right = False
            if e.type == KEYUP and e.key == K_LEFT:
                left = False

            if e.type == pygame.QUIT:
                exit()
        screen.blit(surf, (0, 0))  # перерисовка на каждой итерации

        hero.update(left, right, up, platforms)  # передвижение
        entities.draw(screen)  # отображение всего
        pygame.display.update()  # обновление и вывод всех изменений на экран


if __name__ == "__main__":
    main()
