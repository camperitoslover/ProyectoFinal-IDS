def minijuego_julian(puntos):
    #Indicaciones
    print("\nJuego: Razonamiento Matemático con Julian Apple")
    input("\n( ❥ Presiona ENTER para continuar )")
    print("\n¡Impresiona a Julian con tus habilidades numéricas!")
    input("❥ CONTINUAR")
    print("\nResuelve los problemas numéricos correctamente, la respuesta siempre será un entero")
    input("❥ CONTINUAR")

    #Conteo de puntos adicionales
    puntos_adicionales = 0

    #Diccionario de preguntas y respuestas
    problemas = {"¿Cuánto es 7 + 5?":12,
                "Si tienes 15 chocolates y regalas 8, ¿cuántos te quedan?":7,
                "¿Cuánto es 6 × 4?":24,
                "Un cuaderno cuesta 3 dólares. ¿Cuánto valen 5 cuadernos?":15,
                "¿Cuál es el resultado de 48 ÷ 6?":8,
                "Un número multiplicado por 7 da 63. ¿Cuál es el número?":9,
                "La suma de dos números es 35 y uno de ellos es 14. ¿Cuál es el otro?":21,
                "Resuelve: (45 ÷ 5) + (12 × 2)":33}

    #Bucle de preguntas y respuestas
    for p,r in problemas.items():
        print(f"\n{p}")
        respuesta = int(input("Ingresa tu respuesta: "))
        if respuesta == r:
            input("¡Correcto! Presiona ENTER para continuar.")
            puntos_adicionales += 1
        else:
            input("Respuesta incorrecta. Presiona ENTER para continuar.")

    #Conclusión y puntos del juego
    if puntos >= 5:
        print("\nJulian Apple: ¡Vaya! No sabía que eras tan bueno en matemáticas, supongo que te subestimé...")
        print("\nFelicidades ganas puntos adicionales")
        puntos["Julian"] += 5
    else:
        print("\nJulian Apple: Bueno... No a todos se nos dan los números\n")
        
    return puntos["Julian"]