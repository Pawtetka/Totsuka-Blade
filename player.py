import pygame

WIDTH = 32
HEIGHT = 32
GRAVITY = 313.6 # Сила, которая будет тянуть нас вниз

class Player1(pygame.sprite.Sprite):
    def __init__(self, x, y, orientation):
        pygame.sprite.Sprite.__init__(self)
        self.dx = self.dy = 0                                             # скорость перемещения по координатам
        self.onGround = False                                             # На земле ли я?
        self.orientation = orientation                                    # персонаж смотрит влево или вправо?
        self.image = pygame.image.load("Cubes/AnimationRight/cube1.png")  # загрузка картинки
        self.rect = pygame.Rect(x, y, WIDTH, HEIGHT)                      # прямоугольный объект
        self.currentFrame = 1.0                                           # номер текущего кадра анимации

    def update(self, t, platforms):
        self.keyboard()

        self.rect.x += self.dx * t             # перемещение по Х
        self.collision(self.dx, 0, platforms)  # проверка на столкновение

        if not self.onGround: self.dy = self.dy +  GRAVITY * t    # если мы не на земле, то изменяем скорость
        self.rect.y += self.dy * t                                # перемещение по У
        self.onGround = False
        self.collision(0, self.dy, platforms)  # проверка на столкновение

        self.dx = 0  # Обнуление скорости

        #--- Анимация ---#
        self.currentFrame += t*2                # тут можна регулировать скорость анимации, t*2 ускоряет в 2 раза
        if self.currentFrame >= 5: self.currentFrame = 1.0    # если номер кадра больше 5, то устанавливаем в начало

        if self.orientation == "right":         # смотрит вправо -- загружем нужную картинку
            self.image = pygame.image.load("Cubes/AnimationRight/cube"+str(int(self.currentFrame))+".png")
        elif self.orientation == "left":
            self.image = pygame.image.load("Cubes/AnimationLeft/cube"+str(int(self.currentFrame))+".png")



    # ---***--- Обработка событий клавиатуры ---***---#
    def keyboard(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.dx = -256               # если зажата кнопка, то заем скорость
            self.orientation = "left"    # кнопка влево -- персонаж смотрит влево
        if keys[pygame.K_RIGHT]:
            self.dx = 256
            self.orientation = "right"
        if keys[pygame.K_UP] and self.onGround:
            self.dy = -260               # задаем начальную скорость прижка
            self.onGround = False        # теперь персонаж не на земле


    # ---***--- Метод проверки на столкновение с картой ---***---#
    def collision(self, dx, dy, platforms):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):   # если есть пересечение платформы с игроком
                if dx > 0:                                     # если движется вправо
                    self.rect.x = p.rect.x - self.rect.width   # останавливаем его

                if dx < 0:                                     # если движется влево
                    self.rect.x = p.rect.x + 32                # останавливаем его

                if dy > 0:                                     # если падает
                    self.rect.y = p.rect.y - self.rect.height  # останавливается
                    self.onGround = True                       # становится на землю
                    self.dy = 0                                # скорость = 0

                if dy < 0:                                     # если движется вверх
                    self.rect.y = p.rect.y + 32                # останавливатся
                    self.dy = 0


# Второй персонаж, наследуется от первого
class Player2(Player1):
    # ---***--- переписываем управление под другие клавиши ---***---#
    def keyboard(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.dx = -256
            self.orientation = "left"
        if keys[pygame.K_d]:
            self.dx = 256
            self.orientation = "right"
        if keys[pygame.K_w] and self.onGround:
            self.dy = -260
            self.onGround = False



