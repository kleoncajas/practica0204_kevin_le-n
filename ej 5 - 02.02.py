nombre = input("¿Cuál es tu nombre?  ")
sexo = input("Género Femenino o Masculino  ")
if (sexo == "Femenino" and nombre < "M") or (sexo == "Masculino" and nombre > "N") :
    casa = "Gryffindor"
else :
    casa = "Slytherin"
print("Tu casa es",casa)