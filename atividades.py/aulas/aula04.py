#CRIAR UMA INTERFACE DE CADASTRO PARA O PROGRAMADOR


print ('Seja bem vindo, Dev!')

nome = str(input('Qual é o seu nome?'))
idade = int(input('Qual é sua idade?'))
lingua_prog = str(input('Em qual lingua de programação você atua?'))

if idade >= 18:
    print(f'É um prazer conhece-lo, {nome}! Estamos anciosos para vê suas haibilidade em {lingua_prog}')

elif idade <=18: 
    print(f'Poxa, {nome}! Devido a sua idade não podemos da continuidade.')