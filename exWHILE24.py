from random import randint
computador = randint(0,10)
print ("Sou seu computador... acabei de pensar em numero entre 0 e 10.")
print ("Será que voce consegue adivinhar qual foi? ")
acertou = False
palpites = 0
while not acertou:
    jogador = int(input("Qual é o seu palpite?: "))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print ("Mais")
        elif jogador > computador:
            print("Menos , tente novamente")
print (f"ACERTOU!! com {palpites} tentativas")
