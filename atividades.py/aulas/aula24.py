''' Testanto códigos básicos pós semenas sem estudo '''


# sistema de um show - input - print e if

nome = str(input("Olá, seja muito bem vindo a uma experiência inesquicível. Qual é o seu nome completo? "))
idade = int(input(f"Certo, {nome}. Pra saber se você está liberado, me diz sua idade. "))

if idade >= 18:
    print (f"Perfeito,{nome}! Como você tem {idade} anos, você está liberado para festa.")

else:
    print (f"Poxa, {nome}. Infelizmente devido a sua idade sua entrada não é liberada.")

# while


numero_de_produtos = 457
indice = 0

while indice < numero_de_produtos:
    input(f"Digite o número do lote ({indice + 1}/{numero_de_produtos}): ")
    indice += 1



