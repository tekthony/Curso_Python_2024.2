# TIPOS DE DATOS ESTRUCTURADOS (TDA - tipos de datos estrucutrados)
```python 
#sus valores o elemenmtos se pueden actualizar , elieminar
lista=["abel",20.5.2,.5,False,["texto",.2]]

#tupla -sus valores o elementos no pueden ser modificados o eliminados.
tupla=("abel",20,5.2,False,[])

#diccionarios u objetos
#los diccionarios almacena los datsos con clve:valor 
dicionario={"nombres":"antonio","edad":15,sexo:False}

-[!TIP]
-**observacion** que los tipos de datso estructuradospara almacenar en su interior otros tipos de datos estructurados

lista_alumnos=[
{
    "nombre":"abel"
    edad:20
    "amigos":["no tiene"]
},{
    "nombre":"ruth"
    edad:54
    "amigos":"flor","hipo"
}

```
## 1. convertir texto a lista 
``` python 
#metodo list
texto "hola"
list{texto}
#["h","o","l","a"]

#metodo split
texto="hola como estas, alumnitos lindos"
texto .split(",")

### 2. agregar elementos al final de una lista
``` python 
# METODO APPEND -es el metodo que me permite agrefgar elemnetos a }
#una lista 

lista=["hola"]
lista.append("mundo")
print(lista)
#["hola",["mundo"] 

#METODO INSERT _ es el metodo que me permite agrega elementos en cualquiera
#ubicacion de mi lista
lista_nombre=["edith","ruth","liz"]
lista_nombre.inser(0."antony")
```
## 3. elmiminar elemetntos de una lista 
``` python
#METODO POP - es el metodo que elimina el ultimo elemento de una lista es el contrario de append.
 lista_nombre=["edith","ruth","liz"]
 lista_nombre.pop()

 #primera opcion  - metodomremove - este metodo elimina el por el nombre el elemento que coinsida dentro de mi lista.
 #(por indice)

 lista_nombre=["edith","ruth","liz"]
 lista_nombre.remove("ruth")

 #sefunda opcion - metodo pop -al pasarle por parametro un indice este lo eliminar de la lista.
 #(numero)
  ista_nombre=["edith","ruth","liz"]
 lista_nombre.pop(0)

 ### 4. buscar un elemento en una lista
 ```python 
 lista_nombres=[edith","ruth"."lux"]
 indice=lista_nombres[indice])


 pertenencias="edith" in lista _nombres #tru false
 ```
 ### 5. Comparacion de listas
 podemos hacer uso de los operadores de comparacion para comprar listas 

 **ejm**
 ``` python
 comparar=[1,2,3]>[1,2,4]
 print(compara)
 #salida:
 # 1 no porque son iguales en ambas listas 
 # 2 no porque son iguales en ambas listas
 # 3 3valua que es menor a 4
 # entonces la primera lista es menor que la segunda lista 
print (compara)
```
###

###6.cuidados de las copias 
###7.fe de etrratas(actualixzar listas)
```python 
lista=[1,3,4,5]
lista[0]=2
prin[lista]
 #ejemplo en listas 
  alumnos=[
    {
        "nombre":"abel"
        "edad":19

    },{
        "nombre":"anthony"
        "edad":29

    }
  ]
amumnos[0]{"edad"}=30
alumno [0]={nombre":"mafer","edad":15} #para actualizar
alumno [1]["sexo"]="por definir" # adicionamos el sexo para anthony
print(alumnos)
```

##metodos

son herramientas de python para poder manipular tipos de datos estructurados 
y tipos de datso tipo strin

### 8. Listas y diccionarios por comprencion
es una tecnica pythonica que nos permite crear listas y diccionarios en una sola linea conbinandio bucles y deciciones.

> [!NOTE]
> **vlc*** value loop condicion - valor bucle condicion
#Lista por comprencion:
```python
texto="1,4,8,9,6"
nueva_lista=[int(n) for n in texto.split(",") if int(n)%2==0]
print(nueva_lista)

```

#Diccionario por comprencion:

```python
lista_amigos=["abel","anthony","edith","ruth"]
diccionario={amigo:len(amigo)for amigo in lista_amigos}
print(diccionario)

```






















