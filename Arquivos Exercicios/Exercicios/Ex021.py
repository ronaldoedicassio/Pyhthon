#Faça um programa para reproduzir um audio de um aquivo MP3

import pygame
pygame.init()
pygame.mixer.music.load('Ex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()



