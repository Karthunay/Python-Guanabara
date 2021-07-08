#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.

from math import trunc, floor
numero = float(input('Digite um número: '))
print(f'O número {numero} tem a parte inteira {trunc(numero)}')
#or
numero = float(input('Digite um número: '))
print(f'O número {numero} tem a parte inteira arredondada {numero:.0f}')
#or
numero = float(input('Digite um número: '))
print(f'O número {numero} tem a parte inteira {floor(numero)}')
#or 
numero = float(input('Digite um número: '))
print(f'O número {numero} tem a parte inteira {int(numero)}')