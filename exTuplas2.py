times = ("Flamengo", "Palmeiras", "Athletico-PR", "Fluminense", "Bahia", 
        "Cruzeiro", "Atlético-MG", "Santos", "Red Bull Bragantino", "São Paulo", 
        "Coritiba", "Vitória", "Botafogo", "Vasco da Gama", "Mirassol", 
        "Corinthians", "Internacional", "Grêmio", "Remo", "Chapecoense")
print("-=-"*25)
print(times)
print("-=-"*25)
print(f"Os 5 primeiros colocados sao {times[0:5]}")
print("-=-"*25)
print(f"Os ultimos 4 times sao {times[-4:]}")
print("-=-"*25)
print(f"Times em ordem alfabetica: {sorted(times)}")
print("-=-"*25)
print(f"O chapecoense esta na {times.index("Chapecoense")} posiçao")