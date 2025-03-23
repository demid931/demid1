import pygame

class Food:
    def __init__(self, name_image): #конструктор,тут создаем свойства
        self.image = pygame.image.load(name_image) #создание картинки
        rect = self.image.get_rect() #создание прямоугольника по границам картинки
        self.x = 100 #создание координаты х для картинки
        self.y = 100 #создание координаты у для картинки

    def draw_image(self): #отрисовка картинки
        screen.blit(self.image, (self.x,self.y))

    def move_food(self):  #движение еды
        self.y += 2

    def move_plate(self):  #движение тарелки
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.x -= 3
        elif keys[pygame.K_d]:
            self.x += 3


plate = Food('plate.png')
pygame.init() #обязательная команда
window_size=(300, 300)
screen=pygame.display.set_mode(window_size) #создание окна размером 300 на 300
pygame.display.set_caption('Моя игра')
background_color = (0, 0, 225) #создаем цвет фона (синий)
clock = pygame.time.Clock() #создание игрового таймера (фпс)
while True: #игровой цикл
    screen.fill(background_color)  # залить фон цвет

    plate.draw_image()
    for event in pygame.event.get():  # проходимся по событиям
        if event.type == pygame.QUIT:  # если нажать на крестик
            pygame.QUIT()  # выход из игры
    clock.tick(40)  # частота обновления сцены (40 кдр/сек)
    pygame.display.update() #обновление содержимого экрана