#Listas es una estructura de datos ordenada y mutable  

animales=['perro','gato','canario']


print(animales[2])
print(animales[1:2])
print(animales[0:])

eliminaUltimo=animales.pop()#pop elimina el ultimo elemento de la lista y nos lo devuelve 
print(eliminaUltimo)
print(animales)

nuevaLista=animales.append("jirafa")#Me devuelve none porque no exista en la lista pero me lo añade 
print(nuevaLista)
print(animales)

insercion=animales.insert(2,"vaca")#inserta en la posicion que le indiquemos un elemento
print(insercion)
print(animales)

eliminar=animales.remove("vaca")#va a eliminar el elemento de la lista que le indiquemos 
print(animales)

revertirLista=animales.reverse()#pone la lista al reves 
print(revertirLista)
print(animales)

copiaLista=animales.copy()#copia la lista y la guardamos en otra variable 
print(copiaLista)

ordenarAlfabeticamente=animales.sort()#Ordena alfabeticamente o numeralmente los elementos de una lista
print(ordenarAlfabeticamente)
print(animales)

limpiamosLista=animales.clear()#Limpia la lista y la vacia
print(animales)