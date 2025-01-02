import sys
import pygame

#Responde a los eventos por teclado o mouse
def verificarEventos():
      #Sirve para controlar las entradas por teclado o mouse
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit()