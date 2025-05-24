# TABUADA

numero_calculo = int(input("Selecione o número que deseja ver a tabuada: "))

print(f"Tabuada do {numero_calculo}:")

for i in range(1, 11):
    resultado = numero_calculo * i
    print(f"{numero_calculo} x {i} = {resultado}")

numero_01 = int(input("Digite o primeiro número que deseja somar?"))

numero_02 = int(input("Digite o segundo número que deseja somar?"))

print(f"O resultado é: {numero_01 + numero_02}.2f")