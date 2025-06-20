# EXERCICIO IF 

nome = str(input('Qual é o seu nome?'))
idade = int(input('Quantos anos você tem?'))


if idade >= 18:
    print (f'Seja muito bem vindo {nome}! Você possui {idade} anos. E sua entrada no melhor restaurante foi liberada.')    
else:
    print (f'Olá, {nome}. Não podemos permitir sua entrada! Você possui apenas {idade} anos.')

sobremesa = str(input('Você deseja uma sobremesa gratuita? '))

if sobremesa.lower() == "sim":
    print ("Tudo bem, aguarde que logo menos iremos trazer a sobremesa")

elif sobremesa.lower() == "são":
    certeza = str((input("Tem certeza? Ela acabou de ser feita (Sim/Não)")))

    if certeza.lower() == "sim":
        print ("Tudo bem, logo menos a sobremesa estará aqui")

    else:
        print ("Tudo bem, sem problemas")

else:
    print ("Resposta inválida, por favor digite com Sim ou não.")



pedido_namoro = str(input("você quer namorar comigo?"))

if pedido_namoro == "Sim" or "sim":
    print ("Eu te amo!")

elif pedido_namoro == "Não" or "não":
    print ("Eu não queria mesmo.")

else:
    print ("É sim ou não, burra")