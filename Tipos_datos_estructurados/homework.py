# 1.-Crear una lista de 5 alumnos, cada alumnos almacenaremos su nombre, apellido y edad.
# Insertar al final de la lista los datos de Anthony.
# Eliminar de la lista sin existe los datos de abel.
# Buscar y mostrar el alumnos en la posicion 4 de la lista.

# Paso 1: Crear una lista con 5 alumnos
alumnos = [
    {"nombre": "Juan", "apellido": "Pérez", "edad": 20},
    {"nombre": "María", "apellido": "López", "edad": 22},
    {"nombre": "Carlos", "apellido": "García", "edad": 21},
    {"nombre": "Ana", "apellido": "Martínez", "edad": 23},
    {"nombre": "Luis", "apellido": "Hernández", "edad": 19}
]

# Paso 2: Insertar al final de la lista los datos de Anthony
anthony = {"nombre": "Anthony", "apellido": "Santos", "edad": 24}
alumnos.append(anthony)

# Paso 3: Eliminar de la lista los datos del alumno llamado Abel si existe
alumnos = [alumno for alumno in alumnos if alumno["nombre"].lower() != "abel"]

# Paso 4: Buscar y mostrar el alumno en la posición 4 de la lista
if len(alumnos) > 4:
    alumno_pos4 = alumnos[4]
    print("Alumno en la posición 4:", alumno_pos4)
else:
    print("No hay suficientes alumnos en la lista para mostrar la posición 4.")


#2.- Crear una lista cn 3 diccionarios donde tendran los datos de sus mascotas(nombres, edad, sexo, raza)
# Tareas
# Mostrar la lista con los 4 diccionarios
# Editar el 3er registroy cambiarle la edad sin modificar la lista original.
# Mostrar la lista original y luego la lista con el 3er registro modificado.

#yo como dueño de mi mascota
#deseo ver una lista de mis mascotas
#para tener un resumen o control de elllos


#yo como dueño de mi mascota
#deseoactializar la edad de mi mascota
#para tener una lista correcta de mi amscota   #descrivir el por que de la secuencia y para que.


# el director del tecnologico jose maria arguedas, desea actualizar el proceso academico de registros de notas de sus alumnos
# con la siguiente aclaracion, los docentes podran poner las notas pero no podran editarlas.
# solo los coordinadores de programa de estudios podran dar acceso de edicion de nota previa peticion del docente encargado,
#los estudiantes solo podran ver sus notas y su porcentaje de la asistencia esta sera registrada a travez de un sensor detector en el ingreso del instituto y puerta del aula 
# que se les asignara. 

## yo como docente
## puedo poner las notas 
## por que soy el responsable de la unidad didactica.







