print ('1', type("1"))
print (1, type(1))
print (1.1, type(1.1))
print (True, type(True))


nome_completo = 'Arthur Calori' 
print (nome_completo)


nome = 'Arthur'
idade = 17
maior_de_idade = idade >= 18

print ('Nome:' , nome)
print ('Idade:' , idade)
print ('é maior de idade?' , maior_de_idade)

# SISTEMA SALARIOS

salario = int(input('Digite o seu salario:'))

if salario <= 3000:
    print('Programador Junior')

elif salario >= 3001 and salario <= 6000:
    print('Programador Pleno')

elif salario >= 6001 and salario <= 9000:
    print('Programador Senior')

else:
      print ('Gerente de projeto')

