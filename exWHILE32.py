soma = 0
junt = 0
while True:
    n = int(input("Digite um numero: "))
    if n == 999:
        break
    soma += n
    junt += 1 
print (f"A soma dos {junt} valores foi {soma}")
