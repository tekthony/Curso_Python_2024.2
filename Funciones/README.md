## FUNCIONES

## Concepto

Matematicamente una funcion es una operacion que toma uno o mas valores llamados `argumentos` y produce un valor
denominado `resultado`. 

f(x)=x/1+x**2

> [!NOTE]
> Todos los lenguajes de programacion tiene funciones incorporadas (`funciones internas`), y funciones por el usuario(`funciones externas`)

En programacion una funcion es un programa, es una estructura que nos permite agrupar codigo y sus principales objetivos son:

- `NO REPETIR` fragmentos de codigo.
- `REUTILIZAR` el codigo en distintos escenarios.

## Estructura de una funcion.

Una funcion viene `Definida` por un `Nombre`, sus `Parametros`, y su valor de `Retorno`.
Una ves creada la funcion podremos solicitar su ejecucion `Invocando` la funcion por su `Nombre`👍

## Definir una funcion en python.

Para definir una funcion en python primero utilizaremos la palabra reservada `def` seguida por el `nombre` de la funcion. A continuacion especificaremos los `parametros` con `()` Si es una funcion sin parametros, `(a)` si es una funcion con parametros, si se tuviera mas de un parametros iran separados por `,`, finalizaemos la linea con `:` , en la siguiente linea sin olvidar el identado, comenzara el `cuerpo` de la funcion (micro programa) que puede contener 1 o mas sentencias, finalmente devera `retornar` un resultado con la palabra reservada `return`.

> [!TIP]
> Como retorno tambien se puede utilizar la `funcion interna`, `print()`, para depuracion de codigo no es recomendable usarlo en produccion.


>[!NOTE]
>Print = Dentro de una funcion es una herramienta para depurar el cogigo, para comprobar que una funcion este haciendo el trabajo de manera correcta.

**Ejemplo**
```python
def saludos():
    saludo="hola chivo"
    saludo_dos="como estas"
    return f"{saludo}, {saludo_dos}"
    #print(f"{saludo}, {saludo_dos}")
print(saludo())
#saludo()
```

### Invocar una funcion
Para invocar, (o llamar, ejecutar) una funcion solo tendremos que escribir el `nombre` de la funcion seguido por `()` parentesis.

```python
def saludo():
    print("hola")
#Invocando la funcion.
#saludo()
```

## Retornar un valor
Las funciones pueden retornar (o devolver) un valor.
```python
def uno():
    return
uno()
```

>[!WARNING]
> No confundir `print()` con `return`. el valor retornado por `return` nos permite usarlo de su contexto. y `print()` solo mostrara el literal por terminal.

**Ejemplos**
*En el archivo `lecture.py`

## Retornando multiples valores.
El secreto es hacerlo mediante un tipo de dato estructurado.
```python
def tupla():
    return 2,3,4
varios()
#retorna (2,3,4)
def lista():
    return ["hola",45]
#retorna "hola",45
def dicc():
    return{"nombre":"jose","edad":45}
dicc()
#return{"nombre":"jose","edad":45}
```