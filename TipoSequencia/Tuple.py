import os
def clearConsole():
        os.system('cls')

#Tuplas em Python são coleções ordenadas e imutáveis de elementos, o que significa que, uma vez criadas, seus valores não podem ser alterados.


Number = (1, 2, 3, 4, 5)

Fruit = ("maçã", "banana", "laranja", "uva") #Tupla de strings

Mix = (10, "Olá", 3.14, True)#Tupla mista (contem tipos Int, Strings, float, Booleano):

tupla_aninhada = ((1, 2), ("a", "b"), (True, False))#Tupla aninhada (tupla dentro de outra tupla)

FirstFruit = Fruit[0]  # "maçã"
LastFruit =  Fruit[3]  # "uva"

clearConsole()#Limpar tela

#Desempacotamento de tuplas
z, x, c, v, b = Number  # z = 1, x = 2, c = 3, v = 4, b = 5
print (z, x, c, v, b)
print(Fruit)#Chamando da lista de Frutas
print(FirstFruit)#Chamando da primeira fruta da Lista
print(LastFruit)#Chamando da ultima fruta da Lista
print(Mix)#Chamado Mix 

#clearConsole()#Limpar tela
# Isso causará um erro, pois tuplas são imutáveis
#Number[0] = 10