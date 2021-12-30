#Directorios 

import os 

# def cambiar_directorio(direccion): 
#     os.chdir(direccion)         #cambiamos la ruta
#     direccion_activa=os.getcwd() #coger la ruta en la que estamos actualmente
#     print('El directorio actual de trabajo es',direccion_activa) #imprmimos 
    
# direccion_activa=os.getcwd()
# print('El directorio actual de trabajo es',direccion_activa) 

# cambiar_directorio('libMath')#entre comillas le pasamos la direccion
# #cogemos la direccion de la nueva y nos sale en la consola 

# #borrar directorio (comeso una ruta entera con las barras \\ )
# #metemos esta ruta que empieza en c 
# os.rmdir()#eliminamos un directorio
# os.removedirs()#elimina varios directorios
# #Abrir y cerrar archivos  
# os.O_WRONLY  
# os.O_APPEND

# #Abrimos el archivo 

# miArchivo=os.open('datos.txt',os.O_RDWR|os.O_CREAT) #abrimos y damos los permisos lectur y escritura , 

# linea="escribir esto"
# datos=str.encode(linea)#encode los transforma en binarios
# os.write(miArchivo,datos)
# os.close(datos)
# print('cerramos el archivo')

#Varibles de entorno 

datos=os.environ 
claves=datos.keys()
for elemento in claves: #nos traen las variables de entorno 
    print(elemento),'\n'
    
#submodulo path







#ruta absoluta 
#todo el recorrido de carpetas hasta donde hoy desde C: la relativa la siguiente o la de atras solo 
absoluta=os.path.abspath('borrar') #ruta absoluta 

print(absoluta)
#directorio base  

base=os.path.basename('borrar')#nombre base
print(base)
#saber si existe directorio  

existe=os.path.exists('libMath/potencias.py')
print(existe)

#conocer tamaño de directorio  

existe=os.path.getsize('libMath/potencias.py') # me dice los bites en tamaño

#saber si una ruta es un directorio 
os.path.isdir('ruta')
#saber si una ruta es un archivo  
os.path.isfile('ruta/archivo')


