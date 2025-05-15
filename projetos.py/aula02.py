nome = str(input('Digite o seu nome:'))
peso = int(input('Digite o seu peso:'))
altura = float(input('Digite sua altura:'))


imc = peso / (altura ** 2)

print(f'O seu imc é:', imc)