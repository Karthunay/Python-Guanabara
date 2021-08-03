#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint, randrange

numero = randint(0,5)

print('Vou pensar em número, tente adivinhar!')
usuario = int(input('Qual o número eu pensei? '))
if usuario == numero:
    print('Parabéns! Você venceu!')
else:
    print(f'Pensei no número {numero}. Você perdeu.')