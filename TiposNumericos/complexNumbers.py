import os

def clearConsole():
    os.system('cls')

#Tipo Números Complexos

clearConsole()
oneVariable = 20 + 2j
twoVariable = 10 + 5j

print("Valor Variável 1: " , oneVariable)
print("Valor Variável 1 real: " , oneVariable.real)
print("Valor Variável 1 imaginária: " , oneVariable.imag)
print("Valor Variável 2: " , twoVariable)
print("Valor Variável 2 real: " , twoVariable.real)
print("Valor Variável 2 imaginária: " , twoVariable.imag)

sum = oneVariable + twoVariable
print("\n---Soma: " , oneVariable , " + " , twoVariable , "\nResultado: " , sum)

sumReal = oneVariable.real + twoVariable.real
print("\n---Soma Números Real: " , oneVariable.real , " + " , twoVariable.real , "\nResultado: " , sumReal)

sumImag = oneVariable.imag + twoVariable.imag
print("\n---Soma Números Imaginários: " , oneVariable.imag , " + " , twoVariable.imag , "\nResultado: " , sumImag)

multiplication = oneVariable * twoVariable
print("\n---Muitiplicação: " , oneVariable , " x " , twoVariable , "\nResultado: " , multiplication)