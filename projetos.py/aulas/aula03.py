nome = str(input('Digite qual é seu nome:'))
idade = int(input('Digite sua idade:'))


if idade >= 18:
    print (f'Seja muito bem vindo {nome}! Você possui {idade} anos.Pode entrar, você é maior de idade!')    
else:
    print (f'Olá, {nome}. Não podemos permitir sua entrada! Você possui apenas {idade} anos.')
