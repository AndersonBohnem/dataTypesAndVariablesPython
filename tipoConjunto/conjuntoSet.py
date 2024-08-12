import os

def clearConsole():
    os.system('cls')

#Tipo Conjunto

clearConsole()
oneSet = {1, 2, 3, 4, 5}
twoSet = {3, 4, 5, 6, 7}

print("Primeiro Conjunto" , oneSet)
print("Segundo  Conjunto" , twoSet)

unity = oneSet | twoSet
print("\n---União" , oneSet , " | " , twoSet , "\nResposta: " , unity)

intersection = oneSet & twoSet
print("\n---Interseção " , oneSet , " & " , twoSet , "\nResposta: " , intersection)

difference = oneSet - twoSet
print("\n---Diferença pega os elementos que contém no primeiro e não no segundo" , oneSet , " & " , twoSet , "\nResposta: " , difference)