import os
def clearConsole():
        os.system('cls')

#O objeto range em Python é usado para gerar uma sequência de números.

clearConsole()#Limpar tela

#Range comeca a contagem do 0...
for i in range(5):# 0,1,2,3,4
    print(i)

clearConsole()#Limpar tela

#Range com início e fim específicos
for i in range(2, 8):#2.3.4.5.6.7
    print(i)

clearConsole()#Limpar tela

#Range com passo (step): Pula 2 Numeros 
for i in range(0, 11, 2):#0, 2, 4, 6, 8, 10
    print(i)

clearConsole()#Limpar tela

#Range em ordem decrescente
for i in range(10, 0, -1): #10,9,8,7,6,5,4,3,2,1
    print(i)

clearConsole()#Limpar tela

#Range para iterar sobre índices de uma lista:
frutas = ["maçã", "banana", "laranja", "uva"]
for i in range(len(frutas)):
    print(f"Fruta {i}: {frutas[i]}")
#Retorno 
#Fruta 0: maçã
#Fruta 1: banana
#Fruta 2: laranja
#Fruta 3: uva