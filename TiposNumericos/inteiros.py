import os

def clearConsole():
    os.system('cls')

#Tipo Inteiros

clearConsole()
oneVariable = 20
twoVariable = 10

print("Valor variavel 1: " , oneVariable)
print("Valor variavel 2: " , twoVariable)

sum = oneVariable + twoVariable
print("\n---Soma: " , oneVariable , " + " , twoVariable , "\nResultado: " , sum)

multiplication = oneVariable * twoVariable
print("\n---Muitiplicação: " , oneVariable , " x " , twoVariable , "\nResultado: " , multiplication)

division = oneVariable / twoVariable
print("\n---Divisão: " , oneVariable , " / " , twoVariable , "\nResultado: " , division)

integerDivision = oneVariable // twoVariable
print("\n---Divisão Inteira: " , oneVariable , " // " , twoVariable , "\nResultado: " , integerDivision)

power = oneVariable ** twoVariable
print("\n---Potência: " , oneVariable , " ** " , twoVariable , "\nResultado: " , power)

cont = 10
# Caso a variavel sumVariable for maior que a variavel cont ele ira entrar no if somando com o valor do cont
if(sum > cont):
    sum = sum + cont
    print("Resultado da Soma: " , sum)

if(sum > cont):
    sum += cont
    print("Resultado da Soma: " , sum)