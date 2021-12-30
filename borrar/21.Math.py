import math

#pasar de grados a radianes  
deg=45
rad=deg/180*math.pi
print(rad)

#pasar de radianes a grados 
rad=4 
deg=rad/math.pi*180 
print(deg)

#pasar de radianes a grados con formula 

rad2=math.degrees(4)

#pasar de grados a radianes 

deg2=math.radians(45)

print(rad2)
print(deg2)

#Funciones seno conseno y tangente  
#sin(angle)=vertical_side/hypotenusa
#cos(angle)=horizontal_side/hypotenusa  

#entity_x += math.cos(entity_direction)*speed 
#entity_y -= math.sin(entity_direction)*speed

#math.atan2(y,x)

#colisiones 
x=5 
y=4
resultado=math.sqrt(math.pow((x**2-x**1),2)+math.pow((y**2-y**1),2))

#Math.hypot  

h=math.hypot(1.5,1.5)#coordenadas de los dos puntos 
#print(h)

frase='hfola'

espacios=frase.dos
print(espacios)