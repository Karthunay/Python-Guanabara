kmCarro = float(input('Digite os KM percorrido pelo carro alugado: '))
diasCarro = int(input('Digite quantos dias o carro foi alugado: '))
diasCarro = diasCarro*60.00
kmCarro = kmCarro*0.15
print(f'O custo final de locação foi de R${diasCarro+kmCarro:.2f}')


