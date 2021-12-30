#1.Es lo que el usuario ingresa
vidas=3
nombre='Alejandro'

#2.Creamos un diccionario  

lista={
    'vidas':0, 
    'nombre':''
}
#3.Modificamos los datos del usuario 
lista['vidas']=vidas
lista['nombre']=nombre

#4.Escribimos en el archivo los datos del diccinario

archivo=open('18.Archivo.txt','w')
archivo.write(str(lista))
archivo.close()

#5Leer un archivo 
archivo=open('18.Archivo.txt','r')
for frase in archivo:
    print(frase)
archivo.close()