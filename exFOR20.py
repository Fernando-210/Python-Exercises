from datetime import date
atual = date.today().year
totmaior= 0
totmenor = 0
for person in range(1,8):
    nasc = int(input(f"Em que ano a {person} pessoa nasceu "))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print (f"Tivemos ao todo {totmenor} menores de idade e {totmaior} maiores de idade")
