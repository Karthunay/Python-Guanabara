#O mesmo professor do desafio 019, quer sortear a ordem de apresentação de trabalho dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem dos sorteados.

from random import sample, shuffle
aluno1 = str(input('Nome do primeiro aluno: '))
aluno2 = str(input('Nome do segundo aluno: '))
aluno3 = str(input('Nome do terceiro aluno: '))
aluno4 = str(input('Nome do quarto aluno: '))

alunos = [aluno1, aluno2, aluno3, aluno4]
shuffle(alunos)

print(f'A ordem de apresentação será:\n {alunos}')
#or
print(f'A ordem da apresentação será:\n {sample(alunos, k=4)}')