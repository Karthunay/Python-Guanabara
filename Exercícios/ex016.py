#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.

from math import fabs, floor
numero = float(input('Digite um número:'))
print(f'O número {numero} tem a parte inteira {fabs(numero)}')
#or
numero = float(input('Digite um número :'))
print(f'O número {numero} tem a parte inteira {numero:.0f}')
#or
numero = float(input('Digite um número :'))
print(f'O número {numero} tem a parte inteira {floor(numero)}')
