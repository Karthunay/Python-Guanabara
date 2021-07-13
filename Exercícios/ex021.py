#Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

import pygame

pygame.mixer.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play(loops=0, start=120.0)
while(pygame.mixer.music.get_busy()):pass

#or

import playsound
playsound.playsound('ex021.mp3')