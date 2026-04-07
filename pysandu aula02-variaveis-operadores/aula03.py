def boas_vindas(nome):
    print(f"Olá, {nome}! Seja bem-vindo!")

nome_digitado = input("Digite seu nome: ")
boas_vindas(nome_digitado)

#Função com parametro com retorno
def soma(num_a, num_b):
    soma = num_a + num_b
    return soma

resultado = soma(4, 3)
print(resultado)
print(type(nome_digitado))