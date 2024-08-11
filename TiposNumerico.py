# Inteiros (int): Representam números inteiros, positivos ou negativos, sem decimais. Exemplo: 42, -7.
# Ponto Flutuante (float): Representam números reais, ou seja, números com casas decimais. Exemplo: 3.14, -0.001.
# Números Complexos (complex): Representam números complexos, que têm uma parte real e uma parte imaginária. Exemplo: 2 + 3j.

#---------------------------------------------------------------------------------------------------------------------------------#

# Exemplo de uso de inteiros
a = 10
b = -5

# Operações com inteiros
soma = a + b          # 10 + (-5) = 5
produto = a * b       # 10 * (-5) = -50
divisao_inteira = a // 3   # Divisão inteira: 10 // 3 = 3
potencia = a ** 2      # Potência: 10^2 = 100

print("Soma:", soma)
print("Produto:", produto)
print("Divisão inteira:", divisao_inteira)
print("Potência:", potencia)

#---------------------------------------------------------------------------------------------------------------------------------#

# Exemplo de uso de ponto flutuante
x = 3.14
y = -0.5

# Operações com floats
soma = x + y               # 3.14 + (-0.5) = 2.64
divisao = x / 2            # 3.14 / 2 = 1.57
raiz_quadrada = x ** 0.5   # Raiz quadrada: sqrt(3.14) = 1.772004514666935

print("Soma:", soma)
print("Divisão:", divisao)
print("Raiz quadrada:", raiz_quadrada)

#---------------------------------------------------------------------------------------------------------------------------------#

# Exemplo de uso de números complexos
z1 = 2 + 3j
z2 = 1 - 4j

# Operações com números complexos
soma = z1 + z2             # (2 + 3j) + (1 - 4j) = 3 - 1j
produto = z1 * z2          # (2 + 3j) * (1 - 4j) = 14 - 5j
modulo = abs(z1)           # Módulo: |2 + 3j| = sqrt(2^2 + 3^2) = 3.605551275463989

print("Soma:", soma)
print("Produto:", produto)
print("Módulo de z1:", modulo)

#---------------------------------------------------------------------------------------------------------------------------------#

# Convertendo entre tipos numéricos
a = 10          # Inteiro
b = float(a)    # Convertendo para float: 10 -> 10.0

c = 3.14
d = int(c)      # Convertendo para inteiro (truncando): 3.14 -> 3

e = 7
f = complex(e)  # Convertendo para complexo: 7 -> (7 + 0j)

print("Inteiro para float:", b)
print("Float para inteiro:", d)
print("Inteiro para complexo:", f)

#---------------------------------------------------------------------------------------------------------------------------------#

# Operações misturando tipos numéricos
a = 5           # Inteiro
b = 2.5         # Float
c = 1 + 2j      # Complexo

resultado = a + b      # Inteiro + Float = Float: 5 + 2.5 = 7.5
resultado2 = b * c     # Float * Complexo = Complexo: 2.5 * (1 + 2j) = 2.5 + 5j

print("Resultado (int + float):", resultado)
print("Resultado (float * complex):", resultado2)
