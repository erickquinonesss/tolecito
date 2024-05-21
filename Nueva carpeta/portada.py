import pygame
from ajustes import *
from pygame.locals import *

class Portada(pygame.sprite.Sprite):
    def __init__(self, fondo_img):
        super().__init__()
        self.fondo_portada = pygame.image.load("imagenes/ToleHunt.jpg")  # Carga la imagen de fondo
        self.image = self.fondo_portada
        self.rect = self.image.get_rect()

def toleportada():
    pygame.init()
    Tamaño_pantalla = (WIDTH, HEIGHT)  # Define el tamaño de la pantalla
    screen = pygame.display.set_mode(Tamaño_pantalla)
    pygame.display.set_caption(titulo)

    # Ruta de la imagen de fondo
    fondo_img = pygame.image.load("imagenes/ToleHunt.jpg")

    # Crear una instancia del menú con la imagen de fondo
    portada_inicio = Portada(fondo_img)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.blit(portada_inicio.image, portada_inicio.rect)
        pygame.display.update()

        tecla = pygame.key.get_pressed()
        if tecla [K_RETURN]: 
            return True

if __name__ == "__main__":
    toleportada()

