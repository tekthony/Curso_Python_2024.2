# lista={"abel","anthony","luz"}
# diccionario ={"nombre":"antonio","edad":15 }
# print(diccionario)

# texto="hola"
# lista_texto=list(texto)
# lista2=[e for e in texto]
# print(lista2)

# texto_largo="hola comom estan bienvenidos al salon"
# nueva_texto=texto_largo[16:]
# nueva_lista=nueva_texto.split(" ")
# print(nueva_lista)

# texto_largo="loquitas_.mp4"
# nuevo_elemeno=texto_largo.split(".")
# print("nuevo_elemento"[-1])

#join: es el metodo para unir elemetos en un solo texto 

# texto_largo="este es un texto largo chiquita y chiquitita "
# nuevo_elemeno=texto_largo.split("  ")
# print(nuevo_elemeno)

#otra manera

# texto_largo="este es un texto largo chiquita y chiquitita "
# nuevo_elemeno=texto_largo.split(" ")
# print("/".join(nuevo_elemeno))


# # #DATOS ESTRUCTUR6ADOS
# lista_original=[1,2,3,4]
# copia_lista=lista_original
# lista_original[-1]=15
# print(copia_lista)

# # #crear un problema que recie
# # #DATOS PRIMITIVOba una lista desordenada y muestre por terminal 
# # #la lista ordenada y la lista pervia a ser ordenada

# # #primera manera
# # lista=[5,454,5,4,12,87,8]
# # otra_variable=list.sort()
# # print(lista)
# #  #COPY : copia el valor de la lista: el elementeo que esta almacenando

# #segunda solucion
# lista=[5,454,5,4,12,87,8]

# copia_lista=lista.copy()
# otra_variable=list.sort()
# copia_lista=lista.copy()
# print(lista)


# crear una lista de numeros enteros del siguiente texto

# texto="1,4,8,9,6"
# nueva_lista=[]
# for n in texto.split(","):
#     nueva_lista.append(int(n))
# print(nueva_lista)
# # convertir=texto.split(",")
# # print(convertir)

# # Aplicando la tecnica vlc valor blucle y condicion.

# texto="1,4,8,9,6"
# nueva_lista=[int(n) for n in texto.split(",") if int(n)%2==0]
# print(nueva_lista)

# Diccionario por comprension.

# lista_amigos=["abel","anthony","edith","ruth"]
# diccionario={}
# for _,v in enumerate(lista_amigos): # _ cuando no usare indice.
#     diccionario[v]=len(v)
# print(diccionario) # ejecuta la longitud de cada uno como dicci9onario.

#Aplicando el vlc.

lista_amigos=["abel","anthony","edith","ruth"]
diccionario={amigo:len(amigo)for amigo in lista_amigos}
print(diccionario)





