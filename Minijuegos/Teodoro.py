#Indicaciones
print("\nJuego: Lecciones de Python con Teodoro")
input("❥ Presiona ENTER para continuar")
print("\n¿Puedes seguirle el ritmo a Teodoro en programación?")
input("❥ CONTINUAR")
print("\nLlena los espacios con las palabras faltantes para que el código funcione")
input("❥ CONTINUAR")

#Conteo de puntos adicionales
puntos = 0

#Definición de funciones para dinámica de consola
lista = []
def a1():
    print("hola mundo")
def a2():
    input("Ingresa tu nombre: ")
def a3():
    print("Teodoro".upper())
def a4():
    print("La lista ha sido creada exitosamente")
def a5():
    lista.append(input("Ingresa el primer string: "))
    lista.append(input("Ingresa el segundo string: "))
def a6():
    for l in lista:
        print(f"A Teodoro le gusta programar en {l}")

#Listas de información
codigos = ['Completa la función para imprimir la frase: _____("hola mundo")',
           'Completa la entrada para recolectar tu nombre: nombre = _____("Ingresa tu nombre: ")',
           'Imprime "Teodoro" completamente en mayúsculas: print("Teodoro"._____())',
           'Crea una lista vacía con sus respectivos delimitadores ([] o ()): lista = __',
           'Añade los strings "Python" y "R" a la lista que creaste: lista.______()',
           'Haz que la frase se imprima para ambos valores de la lista: for l in _____: print(f"A Teodoro le gusta programar en {l}")']
soluciones = ["print","input","upper","[]","append","lista"]
acciones = [a1, a2, a3, a4, a5, a6]

#Bucle de ejecución de minijuego
for c, s, a in zip(codigos, soluciones, acciones):
    print(f"\n{c}")
    respuesta = input("Ingresa tu respuesta y presiona ENTER para probar tu código: ")
    if respuesta == s:
        print()
        a()
        input("\n¡Tu código ha funcionado! Felicidades. Presiona ENTER para continuar.")
        puntos += 1
    else:
        input("\nERROR. Presiona ENTER para continuar.")

#Conclusión y puntos del juego
if puntos >= 4:
    print("\nTeodoro: Es… impresionante cómo resolviste todo. Ehm… si quieres… puedo enseñarte un par de trucos más de programación después.\n")
else:
    print("\nTeodoro: Oh… no te preocupes. En programación… todos nos equivocamos al inicio.\n")

#Añadir puntos adicionales al puntaje central