#Crie um programa que leia dois números e mostre a soma entre eles.

n1 = int(input('Qual a sua idade?'))
n2 = int(input('Qual a idade do seu irmão?'))
s = n1 + n2
print(f'A soma entre a sua idade {n1} e a idade do seu irmão {n2}, é {s}')
print(f'A soma entre a sua idade {n1} e a idade do seu irmão {n2}, é {n1+n2}')
print('A soma entre a sua idade {} e a idade do seu irmão {}, é {}.'.format (n1, n2, (n1+n2)))