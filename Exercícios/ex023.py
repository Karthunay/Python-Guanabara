#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados

num = int(input('Digite um número: '))
U = num // 1 % 10
D = num // 10 % 10
C = num // 100 % 10
M = num // 1000 % 10

print(f'Unidade = {U}\n'
      f'Dezena = {D}\n'
      f'Centena = {C}\n'
      f'Milhar = {M}')