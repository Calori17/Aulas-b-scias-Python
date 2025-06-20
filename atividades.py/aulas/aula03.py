# EXERCICIO IF 

nome = str(input('Digite qual é seu nome:'))
idade = int(input('Digite sua idade:'))


if idade >= 18:
    print (f'Seja muito bem vindo {nome}! Você possui {idade} anos. Pode entrar, você é maior de idade!')    
else:
    print (f'Olá, {nome}. Não podemos permitir sua entrada! Você possui apenas {idade} anos.')

sobremesa = str(input('Você deseja uma sobremesa gratuita? '))

certeza = str(input("Tem certeza? Ela acabou de ser feita. "))

resposta = 'Tenho certeza'

if (sobremesa == 'Sim' or sobremesa == 'sim') and certeza != resposta:
    print("Tudo bem, aguarde um momento que logo iremos trazer a sobremesa.")
elif sobremesa == 'Não' or sobremesa == 'não':
    print("Poxa, tudo bem. Mas ela é ótima, esperamos que na próxima você aceite.")
else:
    print("Desculpa, não entendi.")


pedido_namoro = str(input("você quer namorar comigo?"))

if pedido_namoro == "Sim" or "sim":
    print ("Eu te amo!")

elif pedido_namoro == "Não" or "não":
    print ("Eu não queria mesmo.")

else:
    print ("É sim ou não, burra")