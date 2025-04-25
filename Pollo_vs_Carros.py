from cmath import rect
import pygame
import sys
import math

rojo = (255, 0, 0)
azul = (0, 0, 255)
verde = (0,255,0)
rosado = (255,192,203)
negro = (0,0,0)
amarillo = (255,250,0)
blanco = (255,255,255)
naranja = (255,165,0)
cian = (0,255,255)
gris = (50,50,50)
celeste = (135,206,235)

PI = math.pi

pygame.init()

ventana = pygame.display.set_mode((700, 600))
pygame.display.set_caption("Pollo vs carros")

clock = pygame.time.Clock()


############################
# Bucle principal del juego
############################
while True: 
     clock.tick(50)

    # Ciclo para la deteccion de los eventos del juego
     for event in pygame.event.get():
        # Si se hace click en el boton de cerrar la ventana, el juego se termina
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Rellenar la ventana de color
     ventana.fill(celeste)
    
    # Dibujar un rectangulo
     pygame.draw.rect(ventana,verde, (1,1, 700,600))
     pygame.draw.rect(ventana,negro, (1,45, 700,500))
     pygame.draw.rect(ventana,gris, (1,500, 700,50))
     pygame.draw.rect(ventana,gris, (1,263, 700,50))
     pygame.draw.rect(ventana,gris, (1,45, 700,50))
     pygame.draw.rect(ventana,blanco, (335,555, 40,40))
    

    # Movimiento
     x = 5
     y = 5

    # Cambiar la posición del rectángulo basado en la input del usuario
     keys = pygame.key.get_pressed()
     if keys[pygame.K_LEFT]:
        rect.x -= 5
     if keys[pygame.K_RIGHT]:
         rect.x += 5
     if keys[pygame.K_UP]:
        rect.y -= 5
     if keys[pygame.K_DOWN]:
        rect.y += 5

       
    # Actualiza la visualizacion del la ventana
     pygame.display.flip()
        