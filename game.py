import pygame
import sys
import time
from player import *
from blocks import *

# window
WIN_WIDTH = 800  # Ширина создаваемого окна
WIN_HEIGHT = 640  # Высота
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)  # Группируем ширину и высоту в одну переменную
BACKGROUND_COLOR = (0, 64, 0)
NAME = "Battle of one"


def main():
    pygame.init()  # Инициация PyGame, обязательная строчка
    screen = pygame.display.set_mode(DISPLAY)  # Создаем окошко
    pygame.display.set_caption(NAME)  # Пишем в шапку
    surf = pygame.Surface(DISPLAY)
    surf.fill(BACKGROUND_COLOR)

    entities = pygame.sprite.Group()  # Все объекты
    platforms = []  # то, во что мы будем врезаться или опираться

    level = ["K_______________________L",     # карта
             "|                       |",
             "|                       |",
             "|              1        |",
             "|                       |",
             "|  I_J                  |",
             "|                       |",
             "|                   I___3",
             "|                       |",
             "|                       |",
             "|                       |",
             "|          I__J         |",
             "|                       |",
             "|                       |",
             "|                       |",
             "|             K_L       |",
             "|          I__T_T__J    |",
             "|  IJ                   |",
             "|                       |",
             "M_______________________N"]

    # ---***--- Метод обновления карты ---***---#
    def updateMap(map):
        # очистка масивов
        entities.empty()
        i = len(platforms)
        while i > 0:
            del platforms[0]
            i -= 1

        # заполнение масивов
        x = y = 0  # координати блока
        for row in map:
            for col in row:
                if col == "_":
                    pf = Platform(x, y, "Map/block(center).png")       # загрузка изображения в соответствующий блок
                if col == "K":
                    pf = Platform(x, y, "Map/block(left-top).png")
                if col == "L":
                    pf = Platform(x, y, "Map/block(right-top).png")
                if col == "M":
                    pf = Platform(x, y, "Map/block(left-bot).png")
                if col == "N":
                    pf = Platform(x, y, "Map/block(right-bot).png")
                if col == "1":
                    pf = Platform(x, y, "Map/block(1).png")
                if col == "I":
                    pf = Platform(x, y, "Map/block(left).png")
                if col == "J":
                    pf = Platform(x, y, "Map/block(right).png")
                if col == "T":
                    pf = Platform(x, y, "Map/block(3-bot).png")
                if col == "|":
                    pf = Platform(x, y, "Map/block(vert).png")
                if col == "3":
                    pf = Platform(x, y, "Map/block(3-left).png")

                if not col == " ":        # Если блок существует, добавляем его в масив
                    entities.add(pf)
                    platforms.append(pf)

                x = x + PLATFORM_WIDTH
            y = y + PLATFORM_HEIGHT
            x = 0


    updateMap(level)  # обновляем карту
    player1 = Player1(800 - 96, 400, "left")  # Создаем персонажей (координата Х, У, смотрит "влево")
    player2 = Player2(64, 400, "right")
    entities.add(player1)
    entities.add(player2)

    t = time.time()   # загружаем в переменную время от начала эпохи

    while 1:  # Основной цикл программы
        for event in pygame.event.get():    # проверка на закрытие окна
            if event.type == pygame.QUIT:
                sys.exit()

        pygame.draw.rect(screen, (0, 0, 0), (0, 0, WIN_WIDTH, WIN_HEIGHT))  # закраска черным на каждой итерации

        t = time.time() - t     # получаем время между итерациями (например 10 001 - 10 000 = 1)
        player1.update(t*2, platforms)    # обновляем персонажей. t*2 -- ускоряет его в 2 раза
        player2.update(t*2, platforms)
        t = time.time()

        entities.draw(screen)  # отображение всего
        pygame.display.update()  # обновление и вывод всех изменений на экран


if __name__ == "__main__":
    main()
