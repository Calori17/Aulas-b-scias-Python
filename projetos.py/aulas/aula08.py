# EXERCICIO

nome = str(input('Digite o seu nome:'))
idade = int(input('Digite sua idade:'))

if nome != '' and idade >= 0:
    print(f"Seu nome é {nome}")
    print(f"Seu nome invertido é {nome[::-1]}")
    print(f"Seu nome contém {len(nome)} letras.")
    print (f"A primeira letra do seu nome é {nome[0]}")
    print (f"A ultima letra do seu nome é {nome[-1]}")

else:
    print ("Nome e idade não digitados")

if ' ' in nome:
    print("Seu nome contém espaços.")
else:
    print("Seu nome **não** contém espaços.")


# ARTHUR
# 012345

