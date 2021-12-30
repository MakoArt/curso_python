class Persona():
    nombre=''
    apellido=''
    edad=0 
    altura=0
    color_pelo=''
    color_ojos=''
    clase_social=''
    def __init__(self,nombre,apellido,edad,altura,color_pelo,color_ojos,clase_social):
        self.nombre=nombre 
        self.apellido=apellido 
        self.edad=edad 
        self.altura=altura 
        self.color_pelo=color_pelo 
        self.color_ojos=color_ojos 
        self.clase_social=clase_social
    
    def  saludar(self):
        print("Hola buenas noches") 
        
    def setApellido(self,apellido): #Setter 
        self.apellido=apellido 
        return apellido
    
    def getApellido(self): 
        return self.apellido
        
   


mujer=Persona("Maria","Garcia",20,170,"Rubio","Azules","Media")
hombre=Persona("Javier","Rodriguez",34,176,'negro','azules','media')

print("La mujer se llama : ",mujer.nombre)
print("La mujer se apellida : ",mujer.apellido)
print("La mujer tiene : ",str(mujer.edad) + " anios")
print("La mujer mide : ",mujer.altura)
print("Su color de pelo es : ",mujer.color_pelo)
print("Sus ojos son de color : ",mujer.color_ojos)
print("Su clase social es : ",mujer.clase_social)

mujer.saludar()
hombre.saludar()
mujer.setApellido("Fernandez")
print(mujer.getApellido())


class Marciano(Persona): 
    
    velocidad_vuelo=0
    
    def __init__(self,nombre,apellido,edad,altura,color_pelo,color_ojos,clase_social,velocidad_vuelo):
     super().__init__(nombre,apellido,edad,altura,color_pelo,color_ojos,clase_social)
     self.velocidad_vuelo=velocidad_vuelo
     
    def saludar(self):
        print("Hola buenos dias")
     
     
marciano=Marciano("mrv","crack",345,300,"Verde","Rojos","pobre",34)

marciano.saludar()

