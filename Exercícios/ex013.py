#Faça um algorítimo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Digite o seu salário atual: R$'))
reajuste = float(input('Digite o percentual de reajuste: '))
print(f'O salário reajustado é R${salario*reajuste/100+salario:.2f}')
#or
print(f'O salário reajustado em 15% é R${salario*1.15:.2f}')
#or
print(f'O salário reajustado em 15% é R${salario*0.15+salario:.2f}')