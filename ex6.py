n1 = float(input("Primeira nota "))
n2 = float(input("Segunda nota "))
media = (n1 + n2) /2
print (f"O aluno tirou {n1:.1f} e {n2:.1f}, a media do aluno é {media:.1f} ")
if 7 > media >= 5 :
    print ("O aluno está de recuperaçao")
elif media <5 :
    print ("O aluno está REPROVADO")
elif media >= 7 :
    print ("O aluno está Aprovado")
    