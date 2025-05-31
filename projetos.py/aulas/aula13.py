# INTRODUÇÃO WHILE

condicao_while = True

while condicao_while:
    nome = (str(input("Qual é o seu nome? ")))
    print (f"Seu nome é {nome}")


    if nome == "Sair" or nome == "":
        break

print ("Perguntas de  nome finalizado.")