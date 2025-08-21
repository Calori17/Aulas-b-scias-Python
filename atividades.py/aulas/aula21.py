# DESAFIO IA

import random

Num_1 = int(input("Digite o número 1: "))
Num_2 = int(input("Digite o número 2: "))

soma = Num_1 + Num_2

print(f"A soma de {Num_1} e {Num_2} é: {soma}")

resultado_final = soma


while resultado_final == 3:
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


    




           





