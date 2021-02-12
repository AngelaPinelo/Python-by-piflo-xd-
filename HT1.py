#pedir al usuario que ingrese un número 
print ("Dibujaremos un triángulo de la altura que desees ")
x = int( input("Introduce un número entero (será su altura): ") )
i = x 
for i in range (x):
    for j in range(i+1):
        print ("*", end = "")
    print ("")


#Numeros primos 
print ("Deseas saber si tu número es primo?")
Esteban = int (input ("ingrese el número: "))
if Esteban == 0 or Esteban == 1 or Esteban == 4 :
    print ("Tú número no es primo :(")
elif Esteban ==2 :
    print ("Tu número si es primo :D")
elif Esteban % 2 == 0 :
      print ("Tu número no es primo :(")
else :
    print ("Tu número si es primo :D")