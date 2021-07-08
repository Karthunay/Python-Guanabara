# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

mt = float(input('Digite a quantidade de metros: '))
cm = mt*100
mm = mt*1000
print(f'Centímetros: {cm:.0f}cm,\n'
      f'Milímetros: {mm:.0F}mm')