import pygame
#Gestionar el comportamiento de la nave
class Alien():
  #inicializa la nave y especificamos el punto de partida
  def __init__(self,pantalla,confi):
    self.pantalla = pantalla
    self.confi = confi
    
    #Cargar la imagen de la nave
    self.imagen = pygame.image.load("img/ufoP.bmp")
    #rectangulo de la imagen "rect"
    self.rect = self.imagen.get_rect()
    self.pantallaRect = pantalla.get_rect()

    #Empieza la nave en la parte inferior central de la pantalla
    self.rect.centerx = self.pantallaRect.centerx
    self.rect.top = self.pantallaRect.top

    #Valor para el centro de la nave
    self.centro = float(self.rect.centerx)

    #Banderas de movimiento
    self.movimientoDerecha = False
    self.movimientoIzquierda = False


  #Dibuja la nave en la ubicación actual
  def mostrarAlien(self):
    self.pantalla.blit(self.imagen,self.rect)