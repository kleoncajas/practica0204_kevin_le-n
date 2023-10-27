contraseña = input("Introduce una contraseña  ")
contraseña1 = input("Vuelve a introducir la contraseña  ")
if contraseña.lower() == contraseña1.lower() :
    print("La contraseña es correcta")
if contraseña.lower() != contraseña1.lower() :
    print("La contraseña es incorrecta")