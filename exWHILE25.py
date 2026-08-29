from time import sleep
n1 = int(input("Primeiro Valor: "))
n2 = int(input("Segundo Valor: "))
opçao= 0
while opçao != 5:
    print("""
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NUMEROS
    [5] SAIR DO PROGRAMA
    """)
    opçao = int(input("Qual é a sua opçao? "))
    if opçao == 1:
        soma = n1 + n2
        print (f"A soma entre {n1} + {n2} é {soma}")
    elif opçao == 2:
        produto = n1 * n2
        print (f"O resultado entre {n1} x {n2} é {produto}")
    elif opçao == 3:
        if n1 > n2:
            maior = n1
        else :
            maior = n2
            print (f"Entre {n1} e {n2} o maior valor é {maior}")
    elif opçao == 4:
        print("Informe os numeros novamente")
        n1 = int(input("Primeiro Valor: "))
        n2 = int(input("Segundo Valor: "))
    elif opçao == 5:
        print("Finalizando . . .")
    else:
        print("opçao invalida")
    print("=-=" * 10)
    sleep(2)
print ("FIM DO PROGRAMA")
