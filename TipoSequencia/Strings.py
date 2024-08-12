import os
def clearConsole():
    os.system('cls')

#Strings são sequências de caracteres que podem ser utilizadas para armazenar e manipular texto em linguagens de programação. 
clearConsole()

Basic_1 = "Ola Mundo"
name = "Carlos"    
surname = "Silva"
age = "19"
hobby = "andar de Bike"

print("Podemos chamar a variável direto:")
print(Basic_1)
print("\nChamar adicionando com mensagem:")
print("Nome: " , name)
print("Sobrenome: " , surname)

print("\nMeu nome é" , name , surname , "tenho" , age , "anos e gosto de" , hobby)