#exer 2
numero = int(input("Escrava um numero: "))
if numero %2 == 0: print("esse numero é par")
else: print("esse numero é impar")

#exer 3
numero_1 = int(input("Escreva o primeiro numero: "))
numero_2 = int(input("Escrava o segundo numero: "))

if numero_1>numero_2:
    print("o maior numero é: ", numero_1)
elif numero_1<numero_2:
    print("o maior numero é: ", numero_2)
elif numero_1 == numero_2:
    print("os numeros são iguais:",)

#exer 4
num_1 = float(input("Escreva a primeira nota: "))
num_2 = float(input("Escreva a segunda nota: "))
num_3 = float(input("Escreva a terceira nota: "))
num_4 = float(input("Escreva a quarta nota: "))

media = (num_1 + num_2 + num_3 + num_4)/4
print(f"essa é a sua media: ", media)
if media >= 7:
    print("aprovado")
if 5 < media < 7:
    print("recuperação")
if media < 5:
    print("reprovado")

#exer 5
num_1 = float(input("Escreva o primeiro numero: "))
num_2 = float(input("Escreva o segundo numero: "))

if num_1 % num_2 == 0 or num_2 % num_1 == 0:
    print("São múltiplos")
else:
    print("Não são múltiplos")

#exer 6
try:
    num_1 = float(input("Escreva o primeiro numero: "))
    num_2 = float(input("Escreva o segundo numero: "))
except ValueError:
    print("Erro: digite um numero")
    exit()

operacao = input("Escolha a operação (+, -, *, /): ").strip()

if operacao == "+":
    print("Resultado", num_1 + num_2)
elif operacao == "-":
    print("Resultado", num_1 - num_2)
elif operacao == "*":
    print("Resultado", num_1 * num_2)
elif operacao == "/":
    if num_2 == 0:
        print("Erro: divisão por zero")
    else:
        print("Resultado", num_1 / num_2)
else:
    print("Operação Invalida")

#exer7
from datetime import datetime

data_de_nascimento_str = input("Escreva o dia, mês e ano que você nasceu (DD/MM/YYYY): ")
data_atual_str = input("Escreva o dia, mês e ano atual (DD/MM/YYYY): ")

try:
    # Parse the date strings into datetime objects
    data_de_nascimento = datetime.strptime(data_de_nascimento_str, "%d/%m/%Y")
    data_atual = datetime.strptime(data_atual_str, "%d/%m/%Y")

    # Calculate the age based on the year
    idade = data_atual.year - data_de_nascimento.year

    # Adjust age if the birthday hasn't occurred yet this year
    if data_atual.month < data_de_nascimento.month or \
       (data_atual.month == data_de_nascimento.month and data_atual.day < data_de_nascimento.day): # Corrected typo here
        idade -= 1

    # Check voting eligibility (now correctly ordered and inside the try block)
    if idade >= 18:
        print("pode votar")
    elif 16 <= idade < 18: # This condition now correctly handles optional voting for 16 and 17 year olds
        print("pode votar (voto opcional)")
    else: # idade < 16
        print("não pode votar")

except ValueError:
    print("Formato de data inválido. Por favor, use o formato DD/MM/YYYY.")

#exer8
