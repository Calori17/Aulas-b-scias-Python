# CONNTINUE

contador = 0

while contador <= 150:

    contador += 1
    resultado = (contador) 

    if contador >= 0 and contador <= 4:
        print (f"idade {contador}: Bebê")
        continue

    if contador >= 5 and contador <= 10:
        print (f"idade {contador}: Criança")
        continue

    if contador >= 11 and contador <= 15:
        print (f"idade: {contador}: Pré adolecsente")
        continue

    if contador >= 16 and contador <= 18:
        print (f"idade: {contador}: Adolecsente")
        continue

    if contador >= 19 and contador <= 50:
        print (f"idade: {contador}: Adulto")
        continue

    if contador >= 51 and contador <= 99:
        print (f"idade: {contador}: Idoso")
        continue

    else:
        print (f"idade: {contador}: Já morreu")
        break

