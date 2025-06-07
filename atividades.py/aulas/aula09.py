# TRY E EXCEPT


numero_div = float(input("Digite um número para ser divido: "))
divisao = float(input("Por qual número deseja dividir? "))


resultado = numero_div / divisao

try: 
    print(f"O resultado é {resultado}")

except:
    print("Nenhum número foi digitado.")