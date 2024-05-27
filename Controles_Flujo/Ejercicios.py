## Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.

edad:int=int(input("Cual es tu edad: "))
if edad >=18 :
    print("Eres mayor de edad: ")
else:
    print("Eres menor de edad: ")

## Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario
## por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la
## guardada en la variable sin tener en cuenta mayusculas y minusculas.

contraseña_guardada = "contraseña"
contraseña_usuario = input("Ingrese la contraseña: ")
contraseña_guardada = contraseña_guardada
contraseña_usuario = contraseña_usuario
if contraseña_guardada == contraseña_usuario:
    print("¡La contraseña es correcta!")
else:
    print("¡La contraseña es incorrecta!")

## Escribir un programa que pida al usuario un numero entero positivo y muestre por pantalla la cuenta atras 
## desde ese numero hasta cero separados por comas.

numero = int(input("Introduce un número entero positivo: "))
for n in range (0,numero+0) :
    print (numero-n)







