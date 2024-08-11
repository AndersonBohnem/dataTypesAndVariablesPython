import os
def clearConsole():
    os.system('cls')

#Listas em Python são coleções ordenadas e mutáveis de elementos, que podem ser de tipos diferentes, como números, strings, ou até mesmo outras listas.

#Lista comeca a Contagem de 0 
Number = [1, 2, 3, 4, 5]

Mix = [10, "Olá", 3.14, True] # contem tipos Int, Strings, float, Booleano

Fruit = ["maçã", "banana", "laranja", "uva"] 

FirstFruit = Fruit[0]  # "maçã"
LastFruit =  Fruit[3]  # "uva"
#Fruit[1] = "manga"  # Substitui "banana" por "manga"
#Fruit.append("abacaxi")  # Adiciona "abacaxi" ao final da lista
#Fruit.remove("laranja")  # Remove "laranja" da lista

clearConsole()#Limpar tela
print(Fruit)#Chamando da lista de Frutas
print(FirstFruit)#Chamando da primeira fruta da Lista
print(LastFruit)#Chamando da ultima fruta da Lista
print(Mix)#Chamado Mix 
print(Number)#Chamando Numeros 
