# Ruta 4: Teodoro Portillo

def dialogos_teodoro(eleccion_actual,ronda_actual,puntos):

    if eleccion_actual == 4:
        print("\nTeodoro: Ah... hola. No pensé que me saludaras.")
        input("\n( ❥ Presiona ENTER para continuar )")
        print("\n¿Qué respondes?")
        print("1. Me gusta saludarte, te ves adorable cuando te sorprendes.")
        print("2. Solo pasaba por aquí.")
        print("3. Relájate, no muerdo.")
        r = int(input("\nElige una opción (1-3): "))
        ronda_actual += 1

        if r == 1:
            print("\nTeodoro: ¿A-ad-ad... adorable? Gracias… eso es nuevo para mí.")
            puntos["Teodoro"] += 3
        elif r == 2:
            print("\nTeodoro: Oh… e-está bien… igual me alegró verte.")
        elif r == 3:
            print("\nTeodoro: Lo sé… pero igual me pongo nervioso.")
            puntos["Teodoro"] += 1
        else:
            print("\nOpción inválida")
        input("\n( ❥ Presiona ENTER para continuar )")

    elif eleccion_actual == 9:
        print("\nTeodoro: Estoy programando algo pequeño para la clase.")
        input("\n( ❥ Presiona ENTER para continuar )")
        print("\n¿Qué respondes?")
        print("1. ¿Puedo verlo? Me encanta cómo te apasionas.")
        print("2. Suena útil.")
        print("3. Qué aburrido.")
        r = int(input("\nElige una opción (1-3): "))
        ronda_actual += 1

        if r == 1:
            print("\nTeodoro: ¡S-sí, claro! E-es que... me emociona que te interese.")
            puntos["Teodoro"] += 3
        elif r == 2:
            print("\nTeodoro: Eso intento, jaja.")
            puntos["Teodoro"] += 1
        elif r == 3:
            print("\nTeodoro: Ah... o-okay... supongo que no es para todos.")
            puntos["Teodoro"] -= 2
        else:
            print("\nOpción inválida")
        input("\n( ❥ Presiona ENTER para continuar )")

    elif eleccion_actual == 14:
        print("\nTeodoro: ¿Has visto Alvin y las ardillas?")
        input("\n( ❥ Presiona ENTER para continuar )")
        print("\n¿Qué respondes?")
        print("1. ¡Sí! Me encanta, podemos verla juntos.")
        print("2. Una vez.")
        print("3. Es para niños.")
        r = int(input("\nElige una opción (1-3): "))
        ronda_actual += 1

        if r == 1:
            print("\nTeodoro: ¿E-en serio? ¡Qué emoción! Sí, veámosla juntos.")
            puntos["Teodoro"] += 3
        elif r == 2:
            print("\nTeodoro: Jeje, al menos la conoces.")
            puntos["Teodoro"] += 1
        elif r == 3:
            print("\nTeodoro: Oh... d-de acuerdo...")
            puntos["Teodoro"] -= 1
        else:
            print("\nOpción inválida")
        input("\n( ❥ Presiona ENTER para continuar )")

    elif eleccion_actual == 19:
        print("\nTeodoro: ¿Te gusta el anime?")
        input("\n( ❥ Presiona ENTER para continuar )")
        print("\n¿Qué respondes?")
        print("1. Lo amo, dime tu favorito.")
        print("2. Depende.")
        print("3. No.")
        r = int(input("\nElige una opción (1-3): "))
        ronda_actual += 1

        if r == 1:
            print("\nTeodoro: ¡Ah! Tengo muchos... te puedo recomendar varios.")
            puntos["Teodoro"] += 3
        elif r == 2:
            print("\nTeodoro: Bueno... te puedo sugerir alguno suavecito.")
            puntos["Teodoro"] += 1
        elif r == 3:
            print("\nTeodoro: O-oh... está bien...")
            puntos["Teodoro"] -= 2
        else:
            print("\nOpción inválida")
        input("\n( ❥ Presiona ENTER para continuar )")

    elif eleccion_actual == 24:
        print("\nTeodoro: Me da pena cuando la gente me mira.")
        input("\n( ❥ Presiona ENTER para continuar )")
        print("\n¿Qué respondes?")
        print("1. No tienes por qué, eres increíble.")
        print("2. Un poco tímido sí eres.")
        print("3. Entonces no te veré.")
        r = int(input("\nElige una opción (1-3): "))
        ronda_actual += 1

        if r == 1:
            print("\nTeodoro: ¿I-increíble yo?... Gracias... eso me anima mucho.")
            puntos["Teodoro"] += 3
        elif r == 2:
            print("\nTeodoro: Jaja, sí... un poquito.")
            puntos["Teodoro"] += 1
        elif r == 3:
            print("\nTeodoro: No, n-no, sí quiero que me veas... a veces.")
        else:
            print("\nOpción inválida")
        input("\n( ❥ Presiona ENTER para continuar )")

    elif eleccion_actual == 29:
        print("\nTeodoro: Hice galletas... ¿quieres?")
        input("\n( ❥ Presiona ENTER para continuar )")
        print("\n¿Qué respondes?")
        print("1. Solo si me las das tú.")
        print("2. Claro, gracias.")
        print("3. No, gracias.")
        r = int(input("\nElige una opción (1-3): "))
        ronda_actual += 1

        if r == 1:
            print("\nTeodoro: E-eh… s-sí, t-toma... espero que te gusten…")
            puntos["Teodoro"] += 3
        elif r == 2:
            print("\nTeodoro: Me alegra que te gusten... hice muchas.")
            puntos["Teodoro"] += 1
        elif r == 3:
            print("\nTeodoro: Ah... o-okay...")
            puntos["Teodoro"] -= 1
        else:
            print("\nOpción inválida")
        input("\n( ❥ Presiona ENTER para continuar )")

    elif eleccion_actual == 34:
        print("\nTeodoro: Estuve jugando un RPG anoche.")
        input("\n( ❥ Presiona ENTER para continuar )")
        print("\n¿Qué respondes?")
        print("1. ¡Quiero jugar contigo algún día!")
        print("2. ¿Era bueno?")
        print("3. Ya no juego nada.")
        r = int(input("\nElige una opción (1-3): "))
        ronda_actual += 1

        if r == 1:
            print("\nTeodoro: ¡S-sí! Sería increíble... yo... sí quiero.")
            puntos["Teodoro"] += 3
        elif r == 2:
            print("\nTeodoro: Sí, tenía buena historia.")
            puntos["Teodoro"] += 1
        elif r == 3:
            print("\nTeodoro: Oh... está bien...")
        else:
            print("\nOpción inválida")
        input("\n( ❥ Presiona ENTER para continuar )")

    elif eleccion_actual == 39:
        print("\nTeodoro: A veces pienso que soy muy débil.")
        input("\n( ❥ Presiona ENTER para continuar )")
        print("\n¿Qué respondes?")
        print("1. No lo eres, tienes un corazón enorme.")
        print("2. Todos tenemos debilidades.")
        print("3. Un poquito sí.")
        r = int(input("\nElige una opción (1-3): "))
        ronda_actual += 1

        if r == 1:
            print("\nTeodoro: T-tu... eres muy amable... gracias.")
            puntos["Teodoro"] += 3
        elif r == 2:
            print("\nTeodoro: Sí... supongo que es cierto.")
            puntos["Teodoro"] += 1
        elif r == 3:
            print("\nTeodoro: Ah... pensé que dirías otra cosa...")
            puntos["Teodoro"] -= 1
        else:
            print("\nOpción inválida")
        input("\n( ❥ Presiona ENTER para continuar )")

    elif eleccion_actual == 44:
        print("\nTeodoro: ¿Crees que soy una carga?")
        input("\n( ❥ Presiona ENTER para continuar )")
        print("\n¿Qué respondes?")
        print("1. Todo lo contrario, me haces sentir bien.")
        print("2. Claro que no.")
        print("3. No sé.")
        r = int(input("\nElige una opción (1-3): "))
        ronda_actual += 1

        if r == 1:
            print("\nTeodoro: D-dijiste eso... de verdad lo dijiste... gracias.")
            puntos["Teodoro"] += 3
        elif r == 2:
            print("\nTeodoro: Gracias... necesitaba oírlo.")
            puntos["Teodoro"] += 2
        elif r == 3:
            print("\nTeodoro: Oh... o-okay...")
        else:
            print("\nOpción inválida")
        input("\n( ❥ Presiona ENTER para continuar )")

    elif eleccion_actual == 49:
        print("\nTeodoro: Nunca pensé que alguien quisiera pasar tiempo conmigo.")
        input("\n( ❥ Presiona ENTER para continuar )")
        print("\n¿Qué respondes?")
        print("1. Yo quiero hacerlo todos los días.")
        print("2. Me caes bien.")
        print("3. Solo cuando estoy libre.")
        r = int(input("\nElige una opción (1-3): "))
        ronda_actual += 1

        if r == 1:
            print("\nTeodoro: ¿T-todos?... No sé qué decir... gracias...")
            puntos["Teodoro"] += 3
        elif r == 2:
            print("\nTeodoro: Tú también me caes bien... mucho.")
            puntos["Teodoro"] += 1
        elif r == 3:
            print("\nTeodoro: Oh… bueno... igual estoy feliz.")
        else:
            print("Opción inválida")
        input("\n( ❥ Presiona ENTER para continuar )")

    return ronda_actual
