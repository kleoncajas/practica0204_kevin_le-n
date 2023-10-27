contraseña = input("Introduce una contraseña  ")
contraseña1 = input("Vuelve a introducir la contraseña  ")
while contraseña != contraseña1:
    contraseña1 = input("Vuelve a introducir la contraseña  ")
if contraseña == contraseña1:
    print("Contraseña correcta")