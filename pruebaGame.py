#Curso de udemy jasjas
# Invasión alienígena

#Importar la libreria pygame
import pygame
from configuraciones import Configuraciones
from nave import Nave
import funcionesJuego as fj

#Etapa 1 - Creación de la nave, se podrá mover derecha/izquierda y también debéra poder disparar

def iniciarJuego():
  #Inicializa una configuración predeterminada
  pygame.init() 

  confi = Configuraciones()

  pantalla = pygame.display.set_mode((confi.screenWidth,confi.screenHeight))
  pygame.display.set_caption("Invasión alienígena")

  #Crea la nave
  nave = Nave(pantalla)

  #bucle principal de animación del juego
  while True:
    #Escuchar las entradas por teclado/mouse
    fj.verificarEventos()
    #Setteamos el color de fondo
    pantalla.fill(confi.color)
    #Hacemos aparecer la nave
    nave.mostrarNave()
    #Hacer visible la pantalla más reciente
    pygame.display.flip()



#Ejecutar el juego
iniciarJuego()

