from random import randint
import time
itens = ("PEDRA","PAPEL","TESOURA")
computador = randint (0,2)
print ("""Suas opçoes
[0] PEDRA
[1] PAPEL
[2] TESOURA """)
jogador = int(input("Qual e a sua jogada? "))
print("JO")
time.sleep(1)
print("KEN")
time.sleep(1)
print("PO!!!")
time.sleep(1)
print("-=" * 11)
print (f"O computador escolheu {itens[computador]}")
print (f"O jogador jogou {itens[jogador]}")
if computador == 0:
    if jogador == 0:
        print ("EMPATE")
    elif jogador == 1:
        print ("JOGADOR VENCE")
    elif jogador == 2:
        print ("COMPUTADOR VENCE")
    else:
        print ("JOGADA INVALIDA")
elif computador == 1:
    if jogador == 0:
        print ("COMPUTADOR VENCE")
    elif jogador == 1:
        print ("EMPATE")
    elif jogador == 2:
        print ("JOGADOR VENCE")
    else:
        print ("JOGADA INVALIDA")
elif computador == 2:
    if jogador == 0:
        print ("JOGADOR VENCE")
    elif jogador == 1:
        print ("COMPUTADOR VENCE")
    elif jogador == 2:
        print ("EMPATE")
    else:
        print ("JOGADA INVALIDA")
