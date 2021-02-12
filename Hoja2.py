#Validando contraseña
contraseña1 = str (input ("Ingrese su contraseña: "))
contraseña2= str(input ("Por favor, confirme su contraseña: "))
if contraseña1 == contraseña2 or contraseña1.lower() == contraseña2 or contraseña1 == contraseña2.lower() :
    print ("Tu contraseña coincide :D")
else:
    print ("Tu contraseña no coincide : (")


#Listado de alumnos 
nombre = str (input("Ingresa tu nombre por favor: "))
sexo = str (input("Ingresa tu género (H ó M): "))
if nombre.lower() <= "m" and sexo == "m" or sexo == "M":
    print ("Grupo A")
else :
    print ("Grupo B")