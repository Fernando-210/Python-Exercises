from random import randint
print("=-="*30)
print("VAMOS JOGAR PAR OU IMPAR")
print("=-="*30)
v = 0
while True:
    jogador = int(input("Escolha um numero: "))
    computador = randint(0,10)
    total = jogador + computador
    tipo = " " 
    while tipo not in 'PI':
        tipo = str(input("PAR OU IMPAR? ")).strip().upper()[0]
    print(f"Voce jogou {jogador} e o computador {computador}. Total de {total}", end=" ")
    print("DEU PAR " if total % 2 == 0 else "DEU IMPAR" )
    if tipo == "P":
        if total % 2 == 0:
            print("Voce venceu")
            v += 1
        else:
            print("Voce perdeu")
            break
    elif tipo == "I":
        if total % 2 == 1:
            print("Voce venceu")
            v += 1
        else:
            print("Voce perdeu")
            break
    print("Vamos jogar novamente")
print (f"GAME OVER! Voce venceu {v} vezes")
