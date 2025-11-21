# Ruta 3: Neverardo Llanura

def dialogos_neverardo(eleccion_actual,ronda_actual,puntos):
    from main import esperar
    
    if eleccion_actual == 3:
        print("\nNeverardo: ¿Ya entregaste tu formulario para el comité cultural?")
        esperar()
        print("\n¿Qué respondes?")
        print("1. Sí, porque quiero ayudarte en lo que pueda.")
        print("2. Aún no, pero lo haré.")
        print("3. No pienso meterme a nada más.")
        r = int(input("\nElige una opción (1-3): "))
        ronda_actual += 1

        if r == 1:
            print("\nNeverardo: Eso significa mucho para mí, de verdad.")
            puntos["Neverardo"] += 3
        elif r == 2:
            print("\nNeverardo: No hay prisa, pero me alegra saberlo.")
            puntos["Neverardo"] += 1
        elif r == 3:
            print("\nNeverardo: Está bien, respeto tu decisión.")
        else:
            print("Opción inválida")
        esperar()

    elif eleccion_actual == 8:
        print("\nNeverardo: La escuela necesita más voluntarios para el evento.")
        esperar()
        print("\n¿Qué respondes?")
        print("1. Estoy contigo, dime qué necesitas.")
        print("2. Tal vez pueda apoyar un rato.")
        print("3. No me voy a levantar temprano por eso.")
        r = int(input("\nElige una opción (1-3): "))
        ronda_actual += 1

        if r == 1:
            print("\nNeverardo: Gracias, realmente puedo contar contigo.")
            puntos["Neverardo"] += 3
        elif r == 2:
            print("\nNeverardo: Un rato ya es bastante, aprecio tu ayuda.")
            puntos["Neverardo"] += 1
        elif r == 3:
            print("\nNeverardo: Jaja, comprendo. A veces cansa.")
        else:
            print("Opción inválida")
        esperar()

    elif eleccion_actual == 13:
        print("\nNeverardo: A veces me preocupa no estar haciendo suficiente.")
        esperar()
        print("\n¿Qué respondes?")
        print("1. Haces más que cualquiera aquí.")
        print("2. Te entiendo, pero descansa.")
        print("3. No exageres.")
        r = int(input("\nElige una opción (1-3): "))
        ronda_actual += 1

        if r == 1:
            print("\nNeverardo: Gracias... necesitaba escucharlo.")
            puntos["Neverardo"] += 3
        elif r == 2:
            print("\nNeverardo: Quizás tienes razón... debería intentarlo.")
            puntos["Neverardo"] += 2
        elif r == 3:
            print("\nNeverardo: Tal vez sí... no lo sé.")
        else:
            print("\nOpción inválida")
        esperar()

    elif eleccion_actual == 18:
        print("\nNeverardo: ¿Qué piensas de la economía? Es mi materia favorita.")
        esperar()
        print("\n¿Qué respondes?")
        print("1. Podrías enseñarme, me gustaría aprender contigo.")
        print("2. Suena interesante... supongo.")
        print("3. Odio los números.")
        r = int(input("\nElige una opción (1-3): "))
        ronda_actual += 1

        if r == 1:
            print("\nNeverardo: Me encantaría. Podemos empezar cuando quieras.")
            puntos["Neverardo"] += 3
        elif r == 2:
            print("\nNeverardo: Poco a poco puede gustarte más.")
            puntos["Neverardo"] += 1
        elif r == 3:
            print("\nNeverardo: Jaja, está bien. No todos disfrutan lo mismo.")
        else:
            print("\nOpción inválida")
        esperar()

    elif eleccion_actual == 23:
        print("\nNeverardo: A veces me siento abrumado por tantas responsabilidades.")
        esperar()
        print("\n¿Qué respondes?")
        print("1. Puedes apoyarte en mí cuando lo necesites.")
        print("2. Debes delegar.")
        print("3. Bueno, tú lo elegiste.")
        r = int(input("\nElige una opción (1-3): "))
        ronda_actual += 1

        if r == 1:
            print("\nNeverardo: Gracias... de verdad significa mucho.")
            puntos["Neverardo"] += 3
        elif r == 2:
            print("\nNeverardo: Tienes razón, debería confiar más en los demás.")
            puntos["Neverardo"] += 1
        elif r == 3:
            print("\nNeverardo: Jaja, eso también es cierto.")
        else:
            print("\nOpción inválida")
        esperar()

    elif eleccion_actual == 28:
        print("\nNeverardo: Me gustaría que hubiera más armonía en la escuela.")
        esperar()
        print("\n¿Qué respondes?")
        print("1. Yo trabajaré contigo para lograrlo.")
        print("2. Sí, sería bonito.")
        print("3. A mí me da igual.")
        r = int(input("\nElige una opción (1-3): "))
        ronda_actual += 1

        if r == 1:
            print("\nNeverardo: Juntos podemos hacer grandes cosas.")
            puntos["Neverardo"] += 3
        elif r == 2:
            print("\nNeverardo: Me alegra que lo pienses.")
            puntos["Neverardo"] += 1
        elif r == 3:
            print("\nNeverardo: Entiendo... cada quien sus prioridades.")
        else:
            print("\nOpción inválida")
        esperar()

    elif eleccion_actual == 33:
        print("\nNeverardo: ¿Has pensado en unirte al consejo estudiantil?")
        esperar()
        print("\n¿Qué respondes?")
        print("1. Si tú estás ahí, claro que sí.")
        print("2. Podría considerarlo.")
        print("3. No, gracias.")
        r = int(input("\nElige una opción (1-3): "))
        ronda_actual += 1

        if r == 1:
            print("\nNeverardo: Eso... me haría muy feliz.")
            puntos["Neverardo"] += 3
        elif r == 2:
            print("\nNeverardo: Lo pensaré contigo si quieres.")
            puntos["Neverardo"] += 1
        elif r == 3:
            print("\nNeverardo: Está bien, no es para todos.")
        else:
            print("Opción inválida")
        esperar()

    elif eleccion_actual == 38:
        print("\nNeverardo: Me alegra cuando la gente coopera.")
        esperar()
        print("\n¿Qué respondes?")
        print("1. Siempre cooperaré contigo.")
        print("2. Hago lo que puedo.")
        print("3. No es lo mío.")
        r = int(input("\nElige una opción (1-3): "))
        ronda_actual += 1

        if r == 1:
            print("\nNeverardo: Por eso confío tanto en ti.")
            puntos["Neverardo"] += 3
        elif r == 2:
            print("\nNeverardo: Y lo haces bien, créeme.")
            puntos["Neverardo"] += 1
        elif r == 3:
            print("\nNeverardo: Está bien, no todos pueden con todo.")
        else:
            print("\nOpción inválida")
        esperar()

    elif eleccion_actual == 43:
        print("\nNeverardo: ¿Has pensado en tu futuro?")
        esperar()
        print("\n¿Qué respondes?")
        print("1. Quiero construir uno donde tú estés.")
        print("2. Un poco.")
        print("3. Me da flojera pensar en eso.")
        r = int(input("\nElige una opción (1-3): "))
        ronda_actual += 1

        if r == 1:
            print("\nNeverardo: No esperaba eso... pero me alegra escucharlo.")
            puntos["Neverardo"] += 3
        elif r == 2:
            print("\nNeverardo: Está bien, vas por buen camino.")
            puntos["Neverardo"] += 1
        elif r == 3:
            print("\nNeverardo: Jaja, a veces también me pasa.")
        else:
            print("\nOpción inválida")
        esperar()

    elif eleccion_actual == 48:
        print("\nNeverardo: Tu actitud últimamente me inspira.")
        esperar()
        print("\n¿Qué respondes?")
        print("1. Tú también me inspiras, más de lo que imaginas.")
        print("2. Gracias.")
        print("3. ¿En serio?")
        r = int(input("\nElige una opción (1-3): "))
        ronda_actual += 1

        if r == 1:
            print("\nNeverardo: No sabes cuánto significa eso para mí.")
            puntos["Neverardo"] += 3
        elif r == 2:
            print("\nNeverardo: Gracias a ti también.")
            puntos["Neverardo"] += 1
        elif r == 3:
            print("\nNeverardo: Sí, muy en serio.")
            puntos["Neverardo"] += 1
        else:
            print("Opción inválida")
        esperar()

    return ronda_actual
