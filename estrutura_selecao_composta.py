idade = int(input("Digite sua idade: "))
"""
este programa  mostra a faixa etaria
"""

if idade < 18: # esta é a primeira condição 
    print("Menor de idade") # menor de idade 
elif 18 <= idade < 60: 
    print("Adulto")
else:
    print("Idoso")