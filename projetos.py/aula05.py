# TABUADA

numero_calculo = int(input("Selecione o número que deseja ver a tabuada: "))

print(f"Tabuada do {numero_calculo}:")

for i in range(1, 11):
    resultado = numero_calculo * i
    print(f"{numero_calculo} x {i} = {resultado}")
