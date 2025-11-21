def minijuego_neverardo(puntos):
    #Indicaciones
    print("\nJuego: Economía 101 con Never")
    input("\n( ❥ Presiona ENTER para continuar )")
    print("\n¿Puedes seguirle el ritmo a Teodoro en programación?")
    input("❥ CONTINUAR")
    print("\nLlena los espacios con las palabras faltantes para que el código funcione")
    input("❥ CONTINUAR")

    #Conteo de puntos adicionales
    puntos_adicionales = 0

    #Diccionario con preguntas y respuestas
    preguntas = {"Si el precio de un bien aumenta, la cantidad ofrecida suele aumentar también.":"V",
                    "Si aumentan los gustos por un producto, la demanda se desplaza a la izquierda.":"F",
                    "El punto de equilibrio es donde la cantidad ofrecida es igual a la demandada.":"V",
                    "Un bien elástico cambia muy poco cuando cambia el precio.":"F",
                    "Una externalidad negativa genera un daño a terceros.":"V",
                    "Los costos fijos cambian con la cantidad producida.":"F",
                    "Si aumentan los costos de producción, la oferta se desplaza a la derecha.":"F",
                    "Si sube el precio de un bien, la demanda de su complemento baja.":"V",
                    "El excedente del consumidor es lo que estás dispuesto a pagar menos lo que pagas.":"V",
                    "Un precio máximo impuesto por el gobierno suele causar escasez.":"V"}

    for p, r in preguntas.items():
        print(f"\n{p}")
        respuesta = (input("\nIngresa tu respuesta: ").upper())
        if respuesta == r:
            input("\n¡Correcto! Presiona ENTER para continuar.")
            puntos_adicionales += 1
        else:
            input("\nRespuesta incorrecta. Presiona ENTER para continuar.")

    #Conclusión y puntos del juego   
    if puntos_adicionales >= 6:
        print("\nFelicidades ganas puntos adicionales")
        puntos["Neverardo"] += 5
    else:
        print("\nNo lograste ganar los puntos adicionales")
        
    return puntos["Neverardo"]

minijuego_neverardo()