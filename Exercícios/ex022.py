#Crie um programa que leia o nome completo de uma pessoa e mostre: 
#  * O nome completo com letras Maiúsculas e Minúsculas - *Quantas letras ao todo(Sem considerar espaço) - *Quantas letras tem o primeiro nome

nome = str(input('Digite o seu nome completo: ')).strip ()
print(f'Seu nome em letra maiúscula é: {nome.upper( )}\n'
         f'Seu nome com letra minúscula é: {nome.lower()}\n'
         f'Seu nome possui {len(nome)} letras.')
print('Seu primeiro nome tem {} letras '.format( len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras '.format(nome.find(' ')))