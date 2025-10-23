#Ejercicio 1

num = int(input("Ingrese un numero: "))

if num <= 1:
    print("El numero no es primo")
else: 
    for i in range(2,num):
        if num % i == 0:
            print("El numero no es primo")
            break
    else:
        print("El numero es primo")
