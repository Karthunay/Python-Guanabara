#Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.

tabx = int(input('Digite um numero: '))
print('-'* 12)
print(f'TABUADA DO {tabx}\n'
      f'{tabx} x 1 = {tabx}\n'
      f'{tabx} x 2 = {tabx*2}\n'
      f'{tabx} x 3 = {tabx*3}\n'
      f'{tabx} x 4 = {tabx*4}\n'
      f'{tabx} x 5 = {tabx*5}\n'
      f'{tabx} x 6 = {tabx*6}\n'
      f'{tabx} x 7 = {tabx*7}\n'
      f'{tabx} x 8 = {tabx*8}\n'
      f'{tabx} x 9 = {tabx*9}\n'
      f'{tabx} x10 = {tabx*10}\n'
      f'----------------------')
#or
n = int(input('Digite um número: '))
for x in range(1,11):
      print(f'{n:2} x{x:2} = {n*x:2}')