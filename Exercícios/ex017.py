import math
catOposto = int(input('Digite o comprimento do cateto oposto: '))
catAdjacente = int(input('Digite o comprimento do cateto adjacente: '))
hipotenusa = math.sqrt(math.pow(catOposto, 2) + math.pow(catAdjacente, 2))
print(f'A hipotenusa é {hipotenusa}')
