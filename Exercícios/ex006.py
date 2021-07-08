#Crie um algorítmo que leia um número e mostre o seu dobro, triplo e raíz quadrada

from math import sqrt

n1 = int(input('Digite um número:'))
print(f'O dobro de é {n1*2};\nO triplo é {n1*3};\nE a raiz quadrada é {sqrt(n1):.0f} ou {n1**(1/2):.0f}')