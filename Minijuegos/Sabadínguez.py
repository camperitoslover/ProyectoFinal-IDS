#Indicaciones del juego
print("\nJuego: Adivina el Significado con Sabadínguez")
input("❥ Presiona ENTER para continuar")
print("\nAyuda a Sabadínguez a escribir un poema para la feria de literatura")
input("❥ CONTINUAR")
print("\nSelecciona el significado correcto de los salvadoreñismos")
input("❥ CONTINUAR")

#Conteo de puntos adicionales
puntos = 0

#Diccionario formato "salvadoreñismo: definición"
salvadoreñismos = {"canillera":"piernas",
                   "amarre":"compromiso",
                   "desteñirse":"morir",
                   "la de hacer versos":"cabeza",
                   "bisagras":"rodillas",
                   "máscara":"cara",
                   "aceitunas":"ojos",
                   "claveles":"dedos",
                   "buñuelo":"nariz",
                   "dulzaina":"sonrisa"}

#Función random
import random

#Bucle de ejecución del minijuego
for s, d in salvadoreñismos.items():
    #Creación de lista adicional de respuestas incorrectas usando sample
    incorrectas = list(salvadoreñismos.values())
    incorrectas.remove(d)
    incorrectas = random.sample(incorrectas, 2)
    #Función shuffle para randomizar el lugar de la respuesta correcta
    opciones = [d] + incorrectas
    random.shuffle(opciones)
    
    print(f"\n¿Qué significa el siguiente salvadoreñismo?: {s}")
    
    for numero, opcion in enumerate(opciones, start=1):
        print(f"{numero}. {opcion}")

    respuesta = int(input("Ingresa tu respuesta (1-3): "))
    
    correcta = opciones.index(d)+1
    
    if respuesta == correcta:
        input("\n¡Bien! Has definido correctamente la palabra. Presiona ENTER para continuar.")
        puntos += 1
    elif respuesta > 3:
        input("\nEsa respuesta no es válida. Presiona ENTER para continuar")
    else:
        input("\nDefinición Incorrecta. Presiona ENTER para continuar")

#Conclusión y puntos del juego  
if puntos > 6:
    print("Sabadínguez: Oh… lo lograste. Debo admitir que eso fue… bastante admirable.")
else:
    print("Sabadínguez: No pasa nada… incluso en los mejores libros hay capítulos difíciles.")

#Añadir puntos adicionales al puntaje central