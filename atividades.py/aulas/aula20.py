# CALCULADORA WHILE


while True:

    # DIGITAÇÃO DE NÚMERO

    num_1 = input("Digite o número 1: ")
    num_2 = input("Digite o número 2: ")
    operador = input("Digite o operador: (+-/*): ")

    # CONFIRMAÇÃO NÚMERO SER FLOAT

    try:
        num_1_float = float(num_1)
        num_2_float = float(num_2)
        numeros_validos = True

    except:
        numeros_validos = None

    # CORRIGINDO ERROS

    if numeros_validos is None:
        print ("Um ou ambos números são inválidos")
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print ("Operador inválido")
        continue

    if operador > 1:
        print ("Digite apenas um operador.")
        continue

    # CONTAS

    print ("Estamos calculando... O resultado é: ")

    if operador == "+":
        print (num_1_float + num_2_float)
    

    elif operador == "-":
        print (num_1_float - num_2_float)
        

    elif operador == "/":
        print (num_1_float / num_2_float)
        

    elif operador == "*":
        print (num_1_float * num_2_float)
    

    else:
        ("Não conseguimos fazer o calculo, vamos tentar novamente.")

    
    sair = input("Deseja sair? ").lower()
    print (sair)

    sair = input("Digite 'sair' para encerrar ou pressione Enter para continuar: ").lower()

    if sair == "sair":
        print("Encerrando operação.")
        break

    else:
        continue


   

 
    



