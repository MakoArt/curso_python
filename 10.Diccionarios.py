#Diccionarios con clave-valor
empleado={
    'nombre':'Fernando',
    'apellido':'Gutierrez',
    'edad':36 , 
    'hijos':['Ruben','sonia']
}
print(empleado['apellido'])
print(empleado['hijos'][1])

for key in empleado:
    print(key,":",empleado[key]) 