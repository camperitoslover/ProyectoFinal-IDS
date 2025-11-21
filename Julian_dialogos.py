# Ruta 2: Julian Apple

def dialogos_julian(eleccion_actual,ronda_actual,puntos):
    
    from main import eleccion_actual
    from main import esperar
    from main import ronda_actual
    from main import puntos
    
    if eleccion_actual == 2:
        print("\nJulian: Ey, te ves como si necesitaras una broma para animarte.")
        esperar()
        print("\n¿Qué respondes?")
        print("1. Solo tú logras animarme tan rápido.")
        print("2. Dale, sorpréndeme.")
        print("3. No estoy de humor.")
        r = int(input("\nElige una opción (1-3): "))
        ronda_actual += 1

        if r == 1:
            print("\nJulian: Uy, qué peligroso, me vas a hacer sonrojar.")
            puntos["Julian"] += 3
        elif r == 2:
            print("\nJulian: Te advertí... mi humor es devastador.")
            puntos["Julian"] += 2
        elif r == 3:
            print("\nJulian: Entonces voy a tener que insistir hasta que lo estés.")
        else:
            print("\nOpción inválida")
        esperar()

    if eleccion_actual == 7:
        print("\nJulian: ¿Probaste la pizza nueva del comedor?")
        esperar()
        print("\n¿Qué respondes?")
        print("1. Si quieres, la probamos juntos después.")
        print("2. Todavía no, ¿está rica?")
        print("3. Odio la pizza.")
        r = int(input("\nElige una opción (1-3): "))
        ronda_actual += 1

        if r == 1:
            print("\nJulian: Perfecto, así tengo excusa para invitarte.")
            puntos["Julian"] += 3
        elif r == 2:
            print("\nJulian: Sí, aunque todo sabe mejor con compañía.")
            puntos["Julian"] += 1
        elif r == 3:
            print("\nJulian: ¡¿Qué?! Eso sí me dolió en el alma.")
            puntos["Julian"] -= 2
        else:
            print("\nOpción inválida")
        esperar()

    if eleccion_actual == 12:
        print("\nJulian: Fallé un examen... y ni estudiando.")
        esperar()
        print("\n¿Qué respondes?")
        print("1. Seguro igual te fue mejor que a todos.")
        print("2. Podemos estudiar juntos la próxima.")
        print("3. Bueno, te lo mereces por flojo.")
        r = int(input("\nElige una opción (1-3): "))
        ronda_actual += 1

        if r == 1:
            print("\nJulian: Jaja, no sé si burlarme o agradecerte.")
            puntos["Julian"] += 2
        elif r == 2:
            print("\nJulian: ¿Estudiar contigo? Suena como motivación premium.")
            puntos["Julian"] += 3
        elif r == 3:
            print("\nJulian: Touché... pero me dolió igual.")
        else:
            print("\nOpción inválida")
        esperar()

    if eleccion_actual == 17:
        print("\nJulian: ¿Me ves como alguien coqueto?")
        esperar()
        print("\n¿Qué respondes?")
        print("1. Sí, pero contigo no me molesta.")
        print("2. Un poquito.")
        print("3. Demasiado.")
        r = int(input("Elige una opción (1-3): "))
        ronda_actual += 1

        if r == 1:
            print("\nJulian: Ay no, ahora sí me enamoro.")
            puntos["Julian"] += 3
        elif r == 2:
            print("\nJulian: Solo un poquito... por ti sería más.")
            puntos["Julian"] += 1
        elif r == 3:
            print("\nJulian: Admito nada.")
        else:
            print("\nOpción inválida")
        esperar()

    if eleccion_actual == 22:
        print("\nJulian: No me gusta ver a mis amigos tristes.")
        esperar()
        print("\n¿Qué respondes?")
        print("1. Entonces quédate a mi lado.")
        print("2. Qué lindo eres.")
        print("3. Está bien.")
        r = int(input("\nElige una opción (1-3): "))
        ronda_actual += 1

        if r == 1:
            print("\nJulian: Me voy a quedar aunque no estés triste.")
            puntos["Julian"] += 3
        elif r == 2:
            print("\nJulian: Lindo tú, por preocuparte.")
            puntos["Julian"] += 2
        elif r == 3:
            print("\nJulian: Con tal de verte mejor, hago lo que sea.")
        else:
            print("\nOpción inválida")
        esperar()

    if eleccion_actual == 27:
        print("\nJulian: Te ves súper bien hoy... Digo, normal.")
        esperar()
        print("\n¿Qué respondes?")
        print("1. ¿También te gusto normal?")
        print("2. Gracias, tú siempre luces bien.")
        print("3. ¿Estás ligando conmigo?")
        r = int(input("\nElige una opción (1-3): "))
        ronda_actual += 1

        if r == 1:
            print("\nJulian: Me gustas normal, especial, caótico… todo eso.")
            puntos["Julian"] += 3
        elif r == 2:
            print("\nJulian: Agh, no me digas eso que me derrito.")
            puntos["Julian"] += 2
        elif r == 3:
            print("\nJulian: ¿Y si sí? ¿Qué harías?")
            puntos["Julian"] += 1
        else:
            print("\nOpción inválida")
        esperar()

    if eleccion_actual == 32:
        print("\nJulian: A veces quiero tomarme la vida con calma.")
        esperar()
        print("\n¿Qué respondes?")
        print("1. Eso es lo que más me gusta de ti.")
        print("2. Deberías relajarte menos.")
        print("3. Te enseño métodos para relajarte más.")
        r = int(input("\nElige una opción (1-3): "))
        ronda_actual += 1

        if r == 1:
            print("\nJulian: Entonces no cambiaré nunca.")
            puntos["Julian"] += 3
        elif r == 2:
            print("\nJulian: Qué presión, jaja.")
        elif r == 3:
            print("\nJulian: Eso suena... interesante. Me interesa.")
            puntos["Julian"] += 2
        else:
            print("\nOpción inválida")
        esperar()

    if eleccion_actual == 37:
        print("\nJulian: Me dijeron que eras divertido.")
        esperar()
        print("¿Qué respondes?")
        print("1. Solo cuando estoy contigo.")
        print("2. A veces.")
        print("3. Creo que exageraron.")
        r = int(input("\nElige una opción (1-3): "))
        ronda_actual += 1

        if r == 1:
            print("\nJulian: Ese es el tipo de cosas que me alegran el día.")
            puntos["Julian"] += 3
        elif r == 2:
            print("\nJulian: Ya veremos, voy a ponerte a prueba.")
            puntos["Julian"] += 1
        elif r == 3:
            print("\nJulian: Pues yo creo que te quedaste corto.")
        else:
            print("\nOpción inválida")
        esperar()

    if eleccion_actual == 42:
        print("\nJulian: ¿Quieres venir a ver un partido conmigo?")
        esperar()
        print("\n¿Qué respondes?")
        print("1. Sí, solo si te sientas a mi lado.")
        print("2. Suena bien.")
        print("3. Paso.")
        r = int(input("\nElige una opción (1-3): "))
        ronda_actual += 1

        if r == 1:
            print("\nJulian: Obvio, ¿dónde más me sentaría?")
            puntos["Julian"] += 3
        elif r == 2:
            print("\nJulian: Bien, será divertido.")
            puntos["Julian"] += 2
        elif r == 3:
            print("\nJulian: Uff, me dolió, pero bueno.")
            puntos["Julian"] -= 1
        else:
            print("\nOpción inválida")
        esperar()

    if eleccion_actual == 47:
        print("\nJulian: Si fueras un sabor de pizza... ¿cuál serías?")
        esperar()
        print("\n¿Qué respondes?")
        print("1. El que más te guste a ti.")
        print("2. Tal vez pepperoni.")
        print("3. El más simple.")
        r = int(input("\nElige una opción (1-3): "))
        ronda_actual += 1

        if r == 1:
            print("\nJulian: Perfecto, te pediría siempre.")
            puntos["Julian"] += 3
        elif r == 2:
            print("\nJulian: Pepperoni... clásico y confiable.")
            puntos["Julian"] += 1
        elif r == 3:
            print("\nJulian: Lo simple también tiene su encanto.")
        else:
            print("\nOpción inválida")
        esperar()