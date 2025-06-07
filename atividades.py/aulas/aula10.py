# EXERCICIO RADAR

velocidade = 61
local_carro = 110

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1

velocidade_acima = velocidade >= RADAR_1

multado = local_carro >= LOCAL_1

if velocidade_acima:
    print("O carro passou acima da velocidade exegida no radar.")

if multado:
    print("O carro passou no radar acima da velocidade e foi multado")

else:
    print ("O carro passou na velocidade acima e não foi multado.")
