import pygame
#Gestionar el comportamiento de la nave
class Nave():
  #inicializa la nave y especificamos el punto de partida
  def __init__(self,pantalla,confi):
    self.pantalla = pantalla
    self.confi = confi
    
    #Cargar la imagen de la nave
    self.imagen = pygame.image.load("img/space-ship-148536_640.bmp")
    #rectangulo de la imagen "rect"
    self.rect = self.imagen.get_rect()
    self.pantallaRect = pantalla.get_rect()

    #Empieza la nave en la parte inferior central de la pantalla
    self.rect.centerx = self.pantallaRect.centerx
    self.rect.bottom = self.pantallaRect.bottom

    #Valor para el centro de la nave
    self.centro = float(self.rect.centerx)

    #Banderas de movimiento
    self.movimientoDerecha = False
    self.movimientoIzquierda = False


  #Actualiza la posición de la nave
  def upNave(self):
    if self.movimientoDerecha and self.rect.right < self.pantallaRect.right:
      self.centro += self.confi.velocidadNave

    if self.movimientoIzquierda and self.rect.left > 0:
      self.centro -= self.confi.velocidadNave

    #Actualiza el objeto rect
    self.rect.centerx = self.centro

  #Dibuja la nave en la ubicación actual
  def mostrarNave(self):
    self.pantalla.blit(self.imagen,self.rect)