#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo. Calcule e mostre o comprimento da hipotenusa.

from math import pow, sqrt, hypot
catOposto = float(input('Digite o comprimento do cateto oposto: '))
catAdjacente = float(input('Digite o comprimento do cateto adjacente: '))
hipotenusa = sqrt(pow(catOposto, 2) + pow(catAdjacente, 2))
print(f'A hipotenusa é {hipotenusa:.2f}')
#or
hipotenusa = hypot (catOposto, catAdjacente)
print(f'A hipotenusa é {hipotenusa:.2f}')
#or
print(f'A hipotenusa é {hypot(catOposto, catAdjacente):.2f}')