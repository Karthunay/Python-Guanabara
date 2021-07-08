#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input('Digite o preço do produto: R$'))
desconto = float(input('Digite o percentual de desconto: '))
print(f'O produto sairá por R${preco-(preco*desconto/100):.2f}')
#or
print(f'O produto com desconto sairá por R${preco*0.95}')
#or
print(f'O produto sairá por R${preco-preco*0.05:.2f}')
