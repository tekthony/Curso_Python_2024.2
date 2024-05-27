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

###



