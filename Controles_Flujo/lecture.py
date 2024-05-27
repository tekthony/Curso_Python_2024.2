# #ejemplo de if
# if True:
#     print("es verdad")
# else:
#     print("es falso")

# #ejemplo de for
# #imprimir los numeros pares
# #entre 1 - 20
# for n in range(1,21):

#Primer ejmplo if estructurado.

# edad:int=int(input("escribe tu edad: "))
# if edad >=18:
#     print("eres mayor")
# else:
#     print("eres menor de edad")

# #segundo ejemplo if almacenado en variable.

# edad:int=int(input("Escribe tu edad: "))
# respuesta:str="eres mayor" if edad>=18 else "eres menor"
# print(respuesta)

#Crear un programa que me imprima las 5 vocales.
# vocales:str="aeiou"
# print(vocales[0])
# print(vocales[1])
# print(vocales[2])
# print(vocales[3])
# print(vocales[4])

#segunda forma:

# vocales:str="aeiou"
# for n in range (0,5):
#     print(vocales[n])

## Crear un programa que me muestre los 8 primeros numeros pares.

# for n in range (1,17):

#     if n%2==0:
#         print(n)

#segubnda forma:
# contador=0
# for n in range (1,17):
#     if n%2==0:
#          contador+=1
#          print(f"{n} es par numero {contador}")

#crear un programa que pida al usuario escribir una oracion
#y mostrar por terminal la cantidad de vocales a que 
#tiene esa oracion
#OJO: solo las "a" minusculas.
#len = Muestra la longitud de las letras
# oracion:str=input("Escribir una oracion: ")
# vocales="a"
# contador=int=0
# for n in range(0,len(oracion)):
#     if oracion[n] =="a":
#         contador=contador + 1
#         ## contador += 1
# #indice y letra:

# #for i,l in enumerate("aeiou"):
#     #print(f"el indice es {i} y la letra es {l}")
# #enumerate divide el stream, en indice y letras.
# print(f"la cantidad de letras que tengo es {contador}")

#Crear un programa que cuente la cantidad de comas y me muestre sus indices
#Ojo tiene que pedir al usuario

# oracion:str=input("Escribir una oracion: ")
# contador=int=0
# for indice,letra in enumerate(oracion):
#     if letra == ",":
#         print(f"su indice es {indice}")
#         contador+=1
# print (f"la cantidad de comas es {contador}" )

#Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido(desde 1 hasta su edad)

# edad=int(input("Cual es tu edad?: "))
# for i in range (edad):
#     print("tu tienes " + str(i+1) + " años")

# crear un programa que me pida el nombre de tres personas y guarde en un avariable global la ultima letra de sus nombres
#mostrar por pantalla la variable global con las tres ultimaas letras del nombre de cada persona.

# ultima_letra:str=""
# for n in range (3):
#     nombre:str=input("escribe tu nombre: ")
#     #ultima_letra+=nombre[-1]
#     last_letter:str=nombre[-1]
#     ultima_letra+=last_letter
#     #ultima_letra=ultima_letra+last_letter
# print(ultima_letra)

# Crear un programa que muestre por terminal la siguiente figura:
# a
# ee
# iii
# oooo
# uuuuu

# letras="a","e","i","o","u"
# for n in range (letras):
#     print(letras)

# Crear un programa  que muestra la tabla de multiplicar de 1 al 5.

# for i in range (1,6):
#     print(f"tabla de multiplicar del {i}")
#     for j in range (1,13):
#         print(f"{i}*{j} = {i*j}")

# metodo dos:

# Crear un programa  que muestra la tabla de multiplicar de 1 al 5.

# for i in range (1,6):
#     for j in range (1,13):
#         print(f"{i}*{j}={i*j}")

#Tercer metodo:

# for i in range (1,6):
#     for j in range (1,13):
#         resultado= i*j
#         print(f"{i}*{j}={resultado}")

# Crear un programa que pida un numero y que muestre la tabla de mukltiplicar de ese numero:

numero:int=int(input("Ingrese un numero: "))
print(f"La tabla de multiplicacion de {numero} es: ")
for n in range (1,13):
    resultado=numero*n
    print (f"{numero} * {n} = {resultado}") 
















 






    








 