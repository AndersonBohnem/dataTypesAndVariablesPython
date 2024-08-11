import os

def clearConsole():
    os.system('cls')

#Tipo Float

clearConsole()
oneVariable = 64.0
twoVariable = 1.6

print("Valor variavel 1: " , oneVariable)
print("Valor variavel 2: " , twoVariable)

sum = oneVariable + twoVariable
print("\n---Soma: " , oneVariable , " + " , twoVariable , "\nResultado: " , sum)

division = oneVariable / twoVariable
print("\n---Divisão: " , oneVariable , " / " , twoVariable , "\nResultado: " , division)

squareRoot = oneVariable ** 0.5
print("\n---Raiz Quadrada: " , oneVariable , " / 0.5" , "\nResultado: " , squareRoot)


