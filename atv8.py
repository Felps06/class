
# Função que imprime uma mensagem na tela
def saudacao():
    print("Olá! Bem-vindo(a) ao meu programa.")

# Chamando a função
saudacao()


# Função que concatena duas strings e imprime o resultado
def concatenar_strings(str1, str2):
    resultado = str1 + " " + str2
    print("A concatenação das strings é:", resultado)

# Chamando a função
concatenar_strings("Olá", "mundo!")


# Função que calcula o quadrado de um número e retorna o resultado
def calcular_quadrado(numero):
    quadrado = numero ** 2
    return quadrado

# Chamando a função e armazenando o resultado em uma variável
resultado = calcular_quadrado(5)
print("O quadrado do número é:", resultado)