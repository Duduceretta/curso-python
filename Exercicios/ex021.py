#Faça um programa que abra e reproduza um arquivo MP3
import pygame

pygame.mixer.init()
pygame.mixer.music.load("End Of Valor.mp3")
pygame.mixer.music.play()
input('Pressione enter para sair... ')
