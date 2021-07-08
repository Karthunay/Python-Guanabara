#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área, e a quantidade de tinta necessária para pintá-la, sabendo que cada litro  de tinta pinta uma área de 2mt².

largura = float(input('Digite a largura: '))
altura = float(input('Digite a altura: '))
area = largura*altura
print(f'Área: {area:.2f}\n'
      f'Quantidade de tinta: {area/2:.0f}lt/mt²')
#or
print(f'Área: {largura*altura:.2f}\n'
      f'Quantidade de tinta: {largura*altura/2:.0f}lt/mt²')