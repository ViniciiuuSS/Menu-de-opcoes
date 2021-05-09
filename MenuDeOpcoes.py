from time import sleep
import random

print("\033[33m-=-" * 54)
jo = ("\033[33m Jogo da adivinhação")
print(jo.center(170))
print("\033[33m-=-" * 54)
#-----------------------------------------------------------------------------------------------------------------------
inicio = input("Precione qualquer tecla para começar...")
print("Iniciando...")
sleep(1)

print("Bem vindo a calculadora! ")
numero1 = float(input("Digite um valor: "))
numero2 = float(input("Digite outro valor: "))
print("\033[33m-=-" * 54)

menu = 0
maior = 0
menor = 0
while menu != 5 :
    print(f"Numeros atuais \033[31m{numero1}, {numero2}\033[m")
    print("\033[33mSelecione a opção que deseja: ")
    menu = int(input("""[1] Soma\n[2] Multiplicar\n[3] Maior\n[4] Novos numeros\n[5] Sair do programa\nEscolha : """))
    if menu == 1:
        soma = numero1 + numero2
        print(f"A soma entre \033[34m{numero1}\033[m \033[33me\033[m \033[34m{numero2}\033[m \033[33mé de =\033[m \033[34m{soma}\033[m ")
    elif menu == 2:
        mult = numero1 * numero2
        print(f"A multiplicação entre \033[34m{numero1}\033[m \033[33mX\033[m \033[34m{numero2}\033[m \033[33m=\033[m \033[34m{mult}\033[m")
    elif menu == 3:
     if numero1 > maior:
        maior = numero1
        print(f"O maior numero é o \033[34m{maior}\033[m ")
     if numero1 < menor:
        menor = numero1
        print(f"O menor , numero é o \033[34m{menor}\033[m ")
     if numero2 > maior:
        maior = numero2
        print(f"O maior numero é o \033[34m{maior}\033[m ")
     if numero2 < menor:
        menor = numero2
        print(f"O menor numero é o \033[34m{menor}\033[m ")
    elif menu == 4:
        print("Digite os novos numeros ||")
        numero1 = float(input("Digite um valor: "))
        numero2 = float(input("Digite outro valor: "))
    elif menu == 5:
        print("Finalizando programa...")
        sleep(1)
    else:
        print("Opção invalida, tente novamente")
    sleep(2)
    print("\033[33m-=-" * 54)