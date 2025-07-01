# DESAFIO IA

import random

while True:
    numero_secreto = random.randint(1, 10)
    tentativas = 0
    adivinhar = None

    print("\nNovo jogo iniciado!")

    while adivinhar != numero_secreto:
        adivinhar = int(input("Adivinhe qual é o número entre 1 e 10: "))
        tentativas += 1

        if adivinhar > numero_secreto:
            print("O número digitado é maior que o secreto.")
        elif adivinhar < numero_secreto:
            print("O número digitado é menor que o secreto.")
        else:
            print(f"Parabéns! Você acertou em {tentativas} tentativa(s).")

    sair = input("Deseja sair? Digite 'sim' para sair, ou pressione Enter para jogar novamente: ").lower()

    if sair == "sim":
        print("Saindo do sistema.")
        break


    




           





