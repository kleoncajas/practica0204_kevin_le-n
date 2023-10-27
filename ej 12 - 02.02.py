frase = input("Introduce una frase  ")
letra = input("Introduce una letra  ")
n_veces = 0
for letra in frase:
    if letra == letra:
        n_veces += 1
print(n_veces)