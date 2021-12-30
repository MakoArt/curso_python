
frase="soy una frase compleja"
frase2="para estudiar python"


print(frase.startswith("S")) #Devuelve un booleano en función de si el string empieza por la letra que indiquemos 

print(frase.replace("compleja","simple")) #Reemplaza los string que le indiquemos  

nuevoFormato='-'.join(frase)#Intercala un caracter entre cada elemento
print(nuevoFormato)

print(frase.count("frase")) # Me dice cuantos elementos que yo le indique hay en la cadena de texto  

print(frase.capitalize())#Pone la primera letra en mayuscula 

print(frase.endswith("a"))#Nos devolvera True o False en función de si termina por el caracter indicado 

print(frase.find("perro"))#Va a buscar la palabra y nos va a dar la posición que ocupa y si no existe nos da un -1 

print(frase.index("compleja"))#Va a buscar la palabra que le indiquemos y nos va a decir el indice a partir del cual empieza esta palabra 

print(frase.split())#Me divide en comas y separa la frase en elementos individuales 

# Otras curiosidades de los strings  

print(frase[4]) # pedimos el indice numero 4 de el string frase  
print(frase[0:8])#pedimos los caracteres desde la posición 0 a la 8 no includido  
print(frase[2:6])#pedimos los caracteres desde la posición 2 a la 6 no includido  
print(frase[2:]) #pedismo desde el 2 hasta el final de la frase 

#Concatenación clasica

nuevaFrase=frase 
otraFrase=frase2 

print(nuevaFrase + otraFrase)

#Concatenación moderna 

print(f'{nuevaFrase} {otraFrase}')
