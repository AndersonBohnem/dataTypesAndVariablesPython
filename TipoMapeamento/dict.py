import os
def clearConsole():
    os.system('cls')

#Um dicionário em Python é uma coleção de pares chave-valor, onde cada chave é única e é usada para acessar o valor correspondente.
clearConsole()
SimpleDictionary = {
    "nome": "Alice",
    "idade": 30,
    "cidade": "São Paulo"
}

print("---------------------------------------------")
print(SimpleDictionary)
print("---------------------------------------------")

#Acessando valores por chave
name = SimpleDictionary["nome"]
print(name)  # Saída: Alice

Cidade = SimpleDictionary["cidade"]
print(Cidade)

Idade = SimpleDictionary["idade"]
print("Idade antes da Modificaocao: ",Idade) #Saida: 30

#Adicionando um novo par chave-valor
SimpleDictionary["profissão"] = "Engenheira"

#Atualizando o valor de uma chave existente
SimpleDictionary["idade"] = 31
Idade = SimpleDictionary["idade"]
print("Idade Depois da Modificaocao: ",Idade)

#Removendo um par chave-valor
del SimpleDictionary["cidade"]

print("---------------------------------------------")
print(SimpleDictionary)
print("---------------------------------------------")

#Usando get para acessar valores com um valor padrão
profissao = SimpleDictionary.get("profissão", "Desconhecida")
print("Profissao:",profissao)  # Saída: Engenheira (ou "Desconhecida" se a chave não existir)
