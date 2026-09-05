print ("Gerado de PA")
print ("=-="*10)
p1 = (int(input("Primeiro termo: ")))
rz = (int(input("Razao da PA: ")))
termo = p1
cont = 1
while cont <= 10 :
    print (f"{termo}~>", end=" ")
    termo+= rz
    cont += 1
print ("FIM...")
