import sys
import pygame

#Responde a los eventos por teclado o mouse
def verificarEventos(nave):
      #Sirve para controlar las entradas por teclado o mouse
    for event in pygame.event.get():
      #verificar si la tecla que se presionó es la de salida
      if event.type == pygame.QUIT:
        sys.exit()
      #verificar si la tecla que se presionó es para mover a la derecha/izquierda, arriba/abajo
      elif event.type == pygame.KEYDOWN:
         verificarEventosKeyD(event, nave)
      elif event.type == pygame.KEYUP:
         verificarEventosKeyU(event, nave)

#Responde a los eventos por teclado/KeyDown
def verificarEventosKeyD(event,nave):
   if event.key == pygame.K_RIGHT:
      nave.movimientoDerecha = True
   elif event.key == pygame.K_LEFT:
      nave.movimientoIzquierda = True

#Responde a los eventos por teclado/KeyUp
def verificarEventosKeyU(event,nave):
   if event.key == pygame.K_RIGHT:
      nave.movimientoDerecha = False
   elif event.key == pygame.K_LEFT:
      nave.movimientoIzquierda = False

#actualiza las imagenes en pantalla
def actualizarPantalla(confi,pantalla,nave,alien):
       #Setteamos el color de fondo
    pantalla.fill(confi.color)
    #Hacemos aparecer la nave
    nave.mostrarNave()
    alien.mostrarAlien()
    #Hacer visible la pantalla más reciente
    pygame.display.flip()