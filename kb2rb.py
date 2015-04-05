#!/usr/bin/python 
#coding: utf8
# Импортируем библиотеку pygame
import pygame
from pygame import *
from util_pygame import load_pygame
#Объявляем переменные
WIN_WIDTH = 960 #Ширина создаваемого окна
WIN_HEIGHT = 600 # Высота
BACKGROUND_COLOR = "#00FF00"
def main():

    pygame.init() # Инициация PyGame, обязательная строчка 
    screen = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT)) # Создаем окошко
    pygame.display.set_caption("King Bounty 2 Rebirth") # Пишем в шапку
    bg = Surface((WIN_WIDTH,WIN_HEIGHT)) # Создание видимой поверхности
                                         # будем использовать как фон
    bg.fill(Color(BACKGROUND_COLOR))     # Заливаем поверхность сплошным цветом

    while 1: # Основной цикл программы
        for e in pygame.event.get(): # Обрабатываем события
            if e.type == QUIT:
                raise SystemExit, "QUIT"
        #pf=Surface((96,60))
        #pf.image.load('./pic/SUBJECT1_0.png').convert()
       # from test_pytmx import load_pygame
        screen.blit(bg, (0,0))
        tmxdata = load_pygame("./maps/forest.tmx")
        for x in range(0,10):
         for y in range(0,10):
          image=tmxdata.get_tile_image(x,y,1)
          screen.blit(image,((x)*96,(y)*60))
        #screen.flip()
        #screen.blit(bg, (0,0))      # Каждую итерацию необходимо всё перерисовывать 
        pygame.display.flip()     # обновление и вывод всех изменений на экран
if __name__ == "__main__":
    main()

