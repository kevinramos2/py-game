#Curso de udemy jasjas
# Invasión alienígena

#Importar la libreria pygame
import pygame
from funcionalidades import configuraciones
from personajes import nave
from funcionalidades import funcionesJuego as fj

#Etapa 1 - Creación de la nave, se podrá mover derecha/izquierda y también debéra poder disparar

def iniciarJuego():
  #Inicializa una configuración predeterminada
  pygame.init() 

  confi = configuraciones.Configuraciones()

  pantalla = pygame.display.set_mode((confi.screenWidth,confi.screenHeight))
  pygame.display.set_caption("Invasión alienígena")

  #Crea la nave
  naveP = nave.Nave(pantalla, confi)

  #bucle principal de animación del juego
  while True:
    #Escuchar las entradas por teclado/mouse
    fj.verificarEventos(naveP)
    naveP.upNave()
    #Actualizar pantalla
    fj.actualizarPantalla(confi,pantalla,naveP)




#Ejecutar el juego
iniciarJuego()

