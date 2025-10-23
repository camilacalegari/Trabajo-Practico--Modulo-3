import math
def cuadratica(a,b,c):
    discriminante = b**2 - 4*a*c

    if a == 0:
        return "No es una ecuacion cuadratica"
    
    if discriminante < 0:
        return "No tiene solución"
    
    if discriminante == 0:
        x = -b / (2*a)
        return f"Hay una solución x = {round(x,2)}"
    
    else:
        x1 = (-b + math.sqrt(discriminante))/(2*a)
        x2 = (-b - math.sqrt(discriminante))/(2*a)
        return f"Dos soluciones: x1 = {round(x1,2)}, x2 = {round(x2,2)}"

try:
    a = float(input("Ingrese el número de a: "))
    b = float(input("Ingrese el número de b: "))
    c = float(input("Ingrese el número de c: "))

    resultado = cuadratica(a,b,c)
    print(resultado)

except ValueError:
    print("Por favor, ingrese números válidos")