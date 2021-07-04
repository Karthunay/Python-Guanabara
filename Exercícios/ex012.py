preço = float(input('Digite o preço do produto:R$'))
desconto = float(input('Digite o percentual de desconto:'))
print(f'O produto sairá por R${preço-(preço*desconto/100):.2f}')
#or
print(f'O produto com desconto sairá por R${preço*0.95}')
#or
print(f'O produto sairá por R${preço-preço*0.05:.2f}')
