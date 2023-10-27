numero = int(input("Introduce la altura del triángulo  "))
numero1 = 1
for a in range (1, numero +1): 
    for b in range (numero1, 0, -2):
        print(b, end = " ")
    numero1 += 2
    print()