# IMPAR OU PAR 

numero = int(input("Digite um número: "))

if numero % 2 == 0:
    print("O número é par.")
elif numero % 2 != 0:
    print("O número é ímpar.")


# HORARIO


horario = int(input("Olá, digite que horas são agora (Formato 24h):"))

if horario >= 4 and horario <= 11:
       print (f"Bom dia, agora é {horario}:00 da manhã")
elif horario >= 12 and horario <= 17:
           print (f"Boa tarde, agora é {horario}:00 da tarde")
elif horario >= 18 and horario <= 23:
        print (f'Boa noite, agora é {horario}:00 da noite')
elif horario >= 00 and horario <= 3:
        print (f'Boa noite, agora é {horario}:00 da madrugada.')
else:
        print ("Nenhum número foi digitado.")


# CONTADOR DE LETRAS

nome = str(input("Digite o seu nome:"))

if not nome.isalpha():
       print ("O nome precisa possui apenas letras.")
elif len(nome) <= 4:
       print ("Seu nome é pequeno.")
elif len(nome) >= 5 and len(nome) <= 6:
       print ("Seu nome é médio.")
elif len(nome) >= 7 and len(nome) <= 20:
       print ("Seu nome é grande.")
else:
       print ("Nenhum nome foi digitado.")

