Numero_de_alunos = 5

indice = 0
while indice < Numero_de_alunos:
    nota = float(input(f"Digite a nota do aluno {indice + 1}: "))

    if 0 <= nota <= 10:
        print(f"A nota do aluno {indice + 1} é {nota}")
        indice += 1  # Avança para o próximo aluno
    else:
        print("Digite uma nota entre 0 e 10")