import pygame
#Gestionar el comportamiento de la nave
class Nave():
  #inicializa la nave y especificamos el punto de partida
  def __init__(self,pantalla):
    self.pantalla = pantalla
    
    #Cargar la imagen de la nave
    self.imagen = pygame.image.load("/img/space-ship-148536_640.bmp")
    #rectangulo de la imagen "rect"
    self.rect = self.imagen.get_rect()
    self.pantallaRect = pantalla.get_rect()

    #Empieza la nave en la parte inferior central de la pantalla
    self.rect.centerx = self.pantallaRect.centerx
    self.rect.bottom = self.pantallaRect.bottom

  #Dibuja la nave en la ubicación actual
  def mostrarNave(self):
    self.pantalla.blit(self.imagen,self.rect)