#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60.00 por dia e R$0.15 por Km rodado.

kmCarro = float(input('Digite os KM percorrido pelo carro alugado: '))
diasCarro = int(input('Digite quantos dias o carro foi alugado: '))
dias = diasCarro*60.00
km = kmCarro*0.15
print(f'O custo final de locação foi de R${dias+km:.2f}')
#or
print(f'Serão {diasCarro} dias totais de locação a R${diasCarro*60:.2f}, com o total de {kmCarro}km percorridos a R${kmCarro*0.15:.2f}. O custo total será de R${kmCarro*0.15+diasCarro*60:.2f} ')