#Faça um programa que leia algo pelo teclado e mostre o seu tipo primitivo e todas as informações possíveis sobre ele.

k = input('Digite algo:')
print(type(k))
print(f'Tem espaço? {k.isspace()}')
print(f'É um número? {k.isnumeric()}')
print(f'É alfanumérico? {k.isalnum()}')
print(f'É alfabético? {k.isalpha()}')
print(f'Está minúsculo? {k.islower()}')
print(f'Está maiúsculo? {k.isupper()}')
print(k.isascii())
print(f'É um digito? {k.isdigit()}')
print(f'É um código identificador? {k.isidentifier()}')
print(f'É imprimivel {k.isprintable()}')
print(f'Está captalizada/Maiuscula e minuscula? {k.istitle()}')
print(f'É decimal? {k.isdecimal()}')






