peso = float(input("Qual é o seu peso? (kg) "))
altura =float(input("Qual é a sua altura (M) "))
imc = peso / (altura ** 2)
print (f"O IMC dessa pessoa é de {imc:.1f}")
if imc < 18.5:
    print ("Voce esta abaixo do PESO normal ")
elif 18.5 <= imc < 25:
    print ("Voce esta no peso IDEAL ")
elif 25 <= imc < 30:
    print ("Voce esta esta em SOBREPESO")
elif 30 <= imc < 40:
    print ("Voce esta em OBESIDADE , CUIDADO")
elif imc >= 40:
    print ("Voce esta em OBESIDADE MORBIDA TENHA MUITO CUIDADO!")
