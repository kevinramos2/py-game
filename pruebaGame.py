#Curso de udemy jasjas
# Invasión alienígena

#Importar la libreria pygame y sys(para salir del juego)
import pygame
import sys 
from configuraciones import Configuraciones

#Etapa 1 - Creación de la nave, se podrá mover derecha/izquierda y también debéra poder disparar

def iniciarJuego():
  #Inicializa una configuración predeterminada
  pygame.init() 

  confi = Configuraciones()

  pantalla = pygame.display.set_mode((confi.screenWidth,confi.screenHeight))
  pygame.display.set_caption("Invasión alienígena")

  #bucle principal de animación del juego
  while True:
    #Sirve para controlar las entradas por teclado o mouse
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit()
    #Setteamos el color de fondo
    pantalla.fill(confi.color)
    #Hacer visible la pantalla más reciente
    pygame.display.flip()




#Ejecutar el juego
iniciarJuego()

