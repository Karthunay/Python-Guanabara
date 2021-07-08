#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import sin, cos, tan, radians
angulo = float(input('Digite o angulo: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print(f'O ângulo {angulo} tem as seguintes informações:\n'
      f'O seno é {seno:.2g}\n'
      f'O cosseno é {cosseno:.2f}\n'
      f'A tangente é {tangente:.2f}')
#or