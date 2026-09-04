print ("Gerado de PA")
print ("=-="*10)
p1 = (int(input("Primeiro termo: ")))
rz = (int(input("Razao da PA: ")))
termo = p1
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total :
        print (f"{termo}~>", end=" ")
        termo+= rz
        cont += 1
    print ("PAUSA")
    mais = int(input("Quantos termos voce quer mostrar a mais?"))
print (f"Progressao finaliza com {total} termos mostrados")

