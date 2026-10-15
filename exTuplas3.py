from random import randint
sort = ( randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))
print(f"Eu sorteei o valor {sort}")
for n in sort:
    print(f"{n}",end=" ")
print(f"\n O maior valor sorteado foi {max(sort)}")
print(f"O maior valor sorteado foi {min(sort)}")