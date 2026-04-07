#exer 1
import pygame
pygame.init()
pygame.mixer.music.load('audio01-aula03.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
breakpoint()


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
num_1 = float(input("Escreva a primeiro nota: "))
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
