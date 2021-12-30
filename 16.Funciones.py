#Funciones que imprimen en consola

def suma (numero1,numero2): 
    print(numero1 + numero2)
    
suma(4,5)

#Funciones que retornan un resultado
def multiplicacion(numero3,numero4): 
   mult=numero3 * numero4 
   return mult

print(multiplicacion(4,3))


def saludo(nombre): 
    return "Hola buenos dias dias" + nombre

print(saludo("Maria"))
    
#Funciones a los que pasamos tuplas  

def dias_semana(*dias): 
    print(dias)

dias_semana('lunes','martes','miercoles','jueves','viernes','sabado','domingo')

#Pasando por sintaxis de clave-valor  

def colores(color1,color2,color3): 
    print("El color 1 es:"+color1)
    print("El color 2 es:"+color2)
    print("El color 3 es:"+color3)
    
colores(color1="Rojo",color2="Verde",color3="Amarillo")

#Por clave valor y tambien con diccionario

def meses_total(**meses): 
    print(meses)
    
meses_total(primer_mes="Enero",segundo_mes="Febrero",tercer_mes="Marzo")

#Parametros por defecto 

def nombres_propios(nombre1="Juan",nombre2="Maria",nombre3="Javier"): 
    print("El nombre es " + nombre1)
    print("El nombre es " + nombre2)
    print("El nombre es " + nombre3)

nombres_propios(nombre2="Susana")

#Podemos pasar listas por los parametros 

def animales(animales): 
    print("Los animales son " + str(animales))
    
lista=['caballo','toro','perro','gato']

animales(lista)

#Funciones Lambda  

def saludar(saludo):
    return "El saludo es: " + saludo
    
saludando=lambda saludo:saludo

print(saludando("Hola que tal")) 

#funciones con pass  

def estado(estado): 
    pass

