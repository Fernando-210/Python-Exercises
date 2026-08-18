num = int(input("digite um numero inteiro: "))
print ("""Escolha uma das bases para conversão
[1]Converter para Binário
[2]Converter para Octal
[3]Converter para HEXADECIMAL""")
opçao = int(input("Sua opcao:"))
if opçao == 1 :
    print (f"{num} convertido para Binario é igual a {bin(num)[2:]}")
elif opçao == 2:
    print (f"{num} convertido para Binario é igual a {oct(num)[2:]}")
elif opçao == 3:
    print (f"{num} convertido para Binario é igual a {hex(num)[2:]}")
else:
    print ("opçao invalida, tente novamente")

