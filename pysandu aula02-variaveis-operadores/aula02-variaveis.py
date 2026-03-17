print("hello world")

print(7 + 4)
print("7 + 4")
print("7" + "4") # contatenação de strings

# Comentários de 1 linha
'''
comentarios de
multiplas
linhas
'''

#variaves
nome = "Rodrigo" #str
idade = 19 #int
peso = 66  #float

print(nome, idade, peso)
print(f"oi, {nome}!")

# input -- simula forms o cmd
nome = input("digite seu nome: ")
idade = int(input("digite sua idade: "))
peso = float(input("digite seu peso: "))

print(nome, idade, peso)

#desafio 1
nome = input("digite seu nome: ")
print(f"bom vinda {nome}!")

#desafio 2
dia = input("dia do seu nacimento: ")
mes = input("mes do seu nacimento: ")
ano = input("ano do seu nacimento: ")
print("o seu aniversario é em:", dia, mes, ano,)

#desafio 3
numero1 = input("primeiro numero: ")
numero2 = input("segundo numero: ")
print("a soma desses numeros é:", int(numero1) + int(numero2))