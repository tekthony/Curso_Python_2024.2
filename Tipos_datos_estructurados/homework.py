#crear un lista 5 alumnos cada alumnos almacenados su nombre  apellidos y edad
#insertar al final de la lista si existe los datos de antoni
#eliminar de la lista si existe los dtos de abel
#buscar y mostrar el alumnos en la 4 posicion de la lista

# lista_alumnos=[{
#         "nombre":"abel",
#         "apellido":"jurado",
#         "edad":15
#     },{
#         "nombre":"melany",
#         "apellido":"perez",
#         "edad":28
#     },{
#         "nombre":"antony",
#         "apellido":"chipana",
#         "edad":19
#     },{
#         "nombre":"flor",
#         "apellido":"de maria",
#         "edad":18
#     },{
#         "nombre":"jorge",
#         "apellido":"jacinto",
#         "edad":26
# }]
# #insertarmos  al final de la lista los datos de antoni:
# lista_alumnos.append({
#      "nombre":"antony",
#      "apellido":"chipana",
#      "edad":19
# })
# print(lista_alumnos)
# # eliminarmos  de la lista si existe los datos de abel:
# lista_alumnos.remove({
#     "nombre":"abel",
#     "apellido":"jurado",
#     "edad":15
# })
# print(lista_alumnos)
# # buscarmos  y mostrarmos  al alumno en la posicion 4 de la lista:
# indice=lista_alumnos.index({
#   "nombre":"flor",
#   "apellido":"de maria",
#   "edad":18
# })
# print(lista_alumnos[indice])

# 2. crear una lista con 3 diccionarios donde tendran los datos de sus 
#mascotas (nombre,edad,sexo,raza)

#tarea 
#mostrar la lista con los 4 diccionarios 
#edtar el 3er registro y cambiarle la edad sin modificar la lista original
#mostrar la lista original y luego la lista con el 3er registro 

#UN EMPRESARIO DE ALQUILER DE AUTOS DESEA GUARADAR EN UNA BASE DE DATOS LA INFORMACION 
#DE SUS VEHIVULOS, PROCESO QUE DESEA AUTOMATIZAR CON UN SISTEMA INFORMATICO
# #LAS ACCIONES PUEDE REALIZAR EL EMPRESARIO SON VER LAS LISTAS DE AUTOS QUE TIENE , PODRA TAMBIEN ACTUALIZAR  LA #LISTA Y AGREGAN EN NUEVO VEHICULO.

# lista_autos=[{
#         "placa":"adc254",
#         "año":2000,
#         "color":"azul",
#         "marca":"toyota"      
#     },{
#         "placa":"mdc254",
#         "año": 2018,
#         "color":"negro",
#         "marca":"suzuki"
#     },{
#         "placa":"kdc254",
#         "año":2022,
#         "color":"negro",
#         "marca":"hilux"
#     }
# ]
#como empresario de autos
#deseo tener la lista de autos
#actualizar y agregar nuevo vehivulo

# print(lista_autos)


# crear una lista de los 20 numero primos haciendo uso de comprencion. 

primeros_primos = [n for n in range(2, 100) if all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))][:20]

print("Los primeros 20 números primos son:", primeros_primos)

