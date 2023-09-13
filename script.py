
def suma(val1, val2):
    resultado = int(val1) + int(val2)
    print("------------------------------ suma ---------------------------------")
    print("El resultado de la suma de "+ str(val1) + " y " + str(val2) + " es: " + str(resultado))

def resta(val1, val2):
    resultado = int(val1) - int(val2)
    print("------------------------------ resta ---------------------------------")
    print("El resultado de la resta de "+ str(val1) + " y " + str(val2) + " es: " + str(resultado))
    
def multiplicacion(val1, val2):
    resultado = int(val1) * int(val2)
    print("------------------------------ multiplicacion ---------------------------------")
    print("El resultado de la multiplicacion de "+ str(val1) + " y " + str(val2) + " es: " + str(resultado))
    
def division(val1, val2):
    resultado = int(val1) / int(val2)
    print("------------------------------ division ---------------------------------")
    print("El resultado de la division de "+ str(val1) + " y " + str(val2) + " es: " + str(resultado))
    
def potencia(val1, val2):
    resultado = int(val1) ** int(val2)
    print("------------------------------ potencia ---------------------------------")
    print("El resultado de la potencia entre "+ str(val1) + " y " + str(val2) + " es: " + str(resultado))
    
def raiz(val1, val2):
    resultado1 = int(val1) **0.5
    resultado2 = int(val2) **0.5
    print("------------------------------ raiz cuadrada ---------------------------------")
    print("El resultado de la raiz cuadrada de "+ str(val1) +" es: " + str(resultado1))
    print("El resultado de la raiz cuadrada de "+ str(val2) +" es: " + str(resultado2))


val1 = input('Ingresa un numero: ')
val2 = input('Ingresa un segundo numero: ')

suma(val1, val2)
resta(val1, val2)
multiplicacion(val1, val2)
division(val1, val2)
potencia(val1, val2)
raiz(val1,val2)

nombre = input('¿Cuál es su nombre? ')
calificacion = input('Califique le programa con una nota: ')
descripcion = input('Describa el por qué de su calificación: ')
print("---------------------------------------------------------------")
print('Nombre del usuario del programa: '+ nombre)
print('Nota de calificación del programa: ' + str(calificacion))
print('Descripción de la calificación: ' + descripcion)
print("---------------------------------------------------------------")
