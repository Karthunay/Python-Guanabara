#Faça um programa que leia um número inteiro e mostre na tela o seu sucessor, e seu antecessor.

n1 = int(input('Digite um número:'))
print(f'O antecessor de {n1} é {n1-1}, e o sucessor é {n1+1}')
print('O antecessor de {} é {}, e o sucessor é {}'.format(n1, (n1-1), (n1+1)))