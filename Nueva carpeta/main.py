import pygame
from ajustes import *
from portada import *
import random
import sys

iniciar_juego = True

def main():
    pygame.init()
    iniciar_juego = toleportada()
    if iniciar_juego:

        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

        
if __name__ == "__main__":
    main()

