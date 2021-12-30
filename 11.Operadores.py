#Operadores Aritméticos + - / * % 

numero1=44 
numero2=234 

resultado=numero1 * numero2 

print(resultado)

print(20%2)

#Prioridad de operaciones  
#Paréntesis
#1.Potencias y raices 
#2.Multiplicaciones y las divisiones 
#3.Sumas y las restas 

resultado1=345*34+23/3
resultado2=345*(34+23)/3

print(resultado1)
print(resultado2)

#Operador de asignación que es el =  

numero=34

#Operadores Lógicos  and y or  

numero3=34 
numero4=59

if numero3>50 or numero4==59: 
    print("El resultado no es correcto")

#Operadores de comparación == != < > <= >= 
edad=20
genero="Masculino"

if edad<18: 
      print("No puedes acceder a ninguna de las salas")
elif edad >=18 and edad <30: 
     print("puedes entrar a la sala juvenil pero no a la plata")
elif edad>=30 and edad <50: 
    print("puedes entrar en la sala de plata pero no en la de oro")
else: 
    print("Puedes entrar en cualquier sala")




