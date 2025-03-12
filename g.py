import pygame.time

pygame.init() #обязательная команда
window_size=(500, 500)
pygame.init() #обязательная команда
screen=pygame.display.set_mode(window_size) #создание окна размером 300 на 300
pygame.display.set_caption('Моя игра')
background_color = (225, 225, 225) #создаем цвет фона (синий)
screen.fill(background_color) #залить фон цвет
clock = pygame.time.Clock() #создание игрового таймера (фпс)
x = 150
y = 150
a = 250
b = 250

while True: #игровой цикл
    clock.tick(40) #частота обновления сцены (40 кдр/сек)
    pygame.display.update() #обновление содержимого экрана
    for event in pygame.event.get(): #проходимся по событиям
        if event.type == pygame.QUIT: #если нажать на крестик
            pygame.QUIT() #выход из игры
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        a -= 3
    elif keys[pygame.K_d]:
        a += 3
    elif keys[pygame.K_w]:
        b -= 3
    elif keys[pygame.K_s]:
        b += 3
    else:
        if a != 250 or b != 250:
            if a > 250:
                a -= 3
            if a < 250:
                a += 3
            if b > 250:
                b -= 3
            if b < 250:
                b += 3
    screen.fill((225, 225, 225))  # заливка фона
    r = pygame.Rect(x, y, 100, 50)  # создание прямоугольника
    pygame.draw.rect(screen, (0, 0, 0), r) #цвет прямоугольника
    rad = 50
    pygame.draw.circle(screen, (0, 225, 225), (a, b), rad) #создание круга
    pygame.display.update()
a = (225,0,0)😒

