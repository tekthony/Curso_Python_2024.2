# Tipos de datos estructurados(TDA - Tipos de datos abstractos)
```python
#lista= sus valores o elementos se pueden actualizar, eliminar.

lista=["abel".20,5.2,.5,False,["texto",.2]]

#tupla= sus valores o elementos no pueden ser modificados o eliminados.

tupla=("abel",20,5.2,False,[])

#Diccionario o objetos
# los diccionarios almacenan los datos con clave:valor

diccionario={"nombre":"Anthony", "edad":15 }
```
# OBSERVACION

- [!TIP]
- **Observacion: ** Que los tipos de datos estructurados pueden almacenar en su interior otros tipos de datos estructurados.

```python
lista_alumnos=[
    {
        "nombre":"abel",
        "edad":20
    },{
        "nombre":"jose ma",
        "edad":13
    },{
        "nombre":"ruth",
        "edad":13
        "amigos":["flor","rocio"]  
    }
]
```
## Metodos
### 1. Convertir texto a lista

```python

# Metodo list

texto="hola"
list(texto)#["h","o","l","a"]

# Metodo split
texto="hola como estan, alumnitos lindos"
texto.split(",") #separa desde la coma, trocea texto en arrai a partir de una condicion(limitador)..
```

### 2. Agregar elementos al final de una lista

``` python
# Metodo append = es el metodo que me permite agregar elementos a una lista.
lista=["hola"]
lista.append("mundo")
print(lista)
#["hola","mundo"]

# Metodo insert - es el metodo que permite agregar elementos en cualquier ubicacion de mi lista.

lista_nombres=["edith","ruth","luz"]
lista_nombres.insert(0,"anthony")

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
```

## 4. buscar un elemento en una lista
 ```python 
 lista_nombres=[edith","ruth"."lux"]
 indice=lista_nombres[indice])


 pertenencias="edith" in lista _nombres #tru false

```
## 5. Comparacion de listas:

Podemos hacer uso de los operadores de comparacion para comparar listas:
**Ejm**

```python
compara=[1,2,3]<[1,2,4]
# 1 al primer elementos no xq son iguales en ambas listas.
# 2  no  por que son iguales en ambas listas.
# 3 evalua que es menor que 4.
# entonces la primera lista es menor que la segunda lista.
print(compara)
#salida:
```

### 6. Cuidado con las copias.

### 7. FE DE ERRATAS (Actualizar Listas)
```python
lista=[1,3,4,5,6]
lista[0]=2
print(lista)
#[2,3,4,5,6]

# modificando lista con diccionario:
alumnos=[
    {
        "nombre":"abel",
        "edad":15

    },
    {
        "nombre":"charo",
        "edad":20
    }
]
alumnos[0]["edad"]=30
print(alumnos)

# alumnos[0]={"nombre":"mafer","edad":15}     para reemplazar todo el diccionario.
# alumnos [1][sexo]="por definir" agregar una caracteristica mas a charo

```










