import pygame
#Gestionar el comportamiento de la nave
class Nave():
  #inicializa la nave y especificamos el punto de partida
  def __init__(self,pantalla):
    self.pantalla = pantalla
    
    #Cargar la imagen de la nave
    self.imagen = pygame.image.load("img/space-ship-148536_640.bmp")
    #rectangulo de la imagen "rect"
    self.rect = self.imagen.get_rect()
    self.pantallaRect = pantalla.get_rect()

    #Empieza la nave en la parte inferior central de la pantalla
    self.rect.centerx = self.pantallaRect.centerx
    self.rect.bottom = self.pantallaRect.bottom

    #Banderas de movimiento
    self.movimientoDerecha = False
    self.movimientoIzquierda = False
    self.movimientoArriba = False
    self.movimientoAbajo = False

  

  #Actualiza la posición de la nave
  def upNave(self):
    if self.movimientoDerecha:
      self.rect.centerx += 1

    if self.movimientoIzquierda:
      self.rect.centerx -= 1

    if self.movimientoArriba:
      self.rect.bottomleft += 1

    if self.movimientoAbajo:
      self.rect.bottomleft -= 1

  #Dibuja la nave en la ubicación actual
  def mostrarNave(self):
    self.pantalla.blit(self.imagen,self.rect)