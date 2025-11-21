# Ruta 1: Francisco Sabadínguez

def dialogos_sabadinguez(eleccion_actual,ronda_actual,puntos):
    
    if eleccion_actual == 1:
        print("\nSabadínguez: ¿Qué haces perdiendo el tiempo aquí? ...Digo, ¿necesitabas algo?")
        input("\n( ❥ Presiona ENTER para continuar )")
        print("\n¿Qué respondes?")
        print("1. Solo quería hablar contigo un rato, me gusta tu compañía.")
        print("2. Pasaba por aquí, nada importante.")
        print("3. Relájate, tampoco eres tan intimidante.")
        r1 = int(input("\nElige una opción (1-3): "))
        ronda_actual +=1

        if r1 == 1:
            print("\nSabadínguez: Oh... esta bien, a mi también me agrada tu compañia.")
            puntos["Sabadínguez"] += 3
        elif r1== 2:
            print("\nSabadínguez: Ya veo...")
            puntos["Sabadínguez"] += 1
        elif r1 == 3:
            print("\nSabadínguez: Entonces mejor vete, no quiero verte ahora.")
        else:
            print("\nOpción invalida")


    elif eleccion_actual == 6:
        print("\nSabadínguez: Estoy leyendo esta novela, aunque probablemente no te interese.")
        input("\n( ❥ Presiona ENTER para continuar )")
        print("\n¿Qué respondes?")
        print("1. Claro que me interesa, ¿de qué trata?")
        print("2. Yo casi no leo, pero me alegra verte entusiasmado.")
        print("3. La literatura es aburrida.")
        r1 = int(input("\nElige una opción (1-3): "))
        ronda_actual +=1

        if r1 == 1:
            print("\nSabadínguez: Sientate conmigo, te contaré todo.")
            puntos["Sabadínguez"] += 3
        elif r1== 2:
            print("\nSabadínguez: Entiendo...Supongo que todos tienen sus propios gustos.")
            puntos["Sabadínguez"] += 1
        elif r1 == 3:
            print("\nSabadínguez: Si ofendes a la literatura, me ofendes a mí.")
            puntos["Sabadínguez"] -=2
        else:
            print("\nOpción invalida")
        input("\n( ❥ Presiona ENTER para continuar )")
    
    elif eleccion_actual == 11:
        print("\nSabadínguez: Me dijeron que hay tortugas en el estanque hoy.")
        input("\n( ❥ Presiona ENTER para continuar )")
        print("\n¿Qué respondes?")
        print("1. ¿Quieres ir a verlas juntos?")
        print("2. Qué curioso.")
        print("3. ¿Por qué te gustan tanto?")
        r1 = int(input("\nElige una opción (1-3): "))
        ronda_actual +=1

        if r1 == 1:
            print("\nSabadínguez: ¡Claro! Vamos.")
            puntos["Sabadínguez"] += 3
        elif r1== 2:
            print("\nSabadínguez: Si... Así son mis gustos.")
        elif r1 == 3:
            print("\nSabadínguez: Porque se parecen a mi ¿no crees?")
            puntos["Sabadínguez"] += 1
        else:
            print("\nOpción invalida")
        input("\n( ❥ Presiona ENTER para continuar )")
    
    elif eleccion_actual == 16:
        print("\nSabadínguez: Recordé algo que me dijiste hace días. No pensé que fuera importante...")
        input("\n( ❥ Presiona ENTER para continuar )")
        print("\n¿Qué respondes?")
        print("1. Me alegra que lo recuerdes, significa mucho.")
        print("2. ¿En serio te acuerdas de eso?")
        print("3. ¿Qué más recuerdas? ¿Mi fecha de nacimiento?")
        r1 = int(input("\nElige una opción (1-3): "))
        ronda_actual +=1

        if r1 == 1:
            print("\nSabadínguez: Me alegra que te alegre.")
            puntos["Sabadínguez"] += 3
        elif r1== 2:
            print("\nSabadínguez: Si... aun lo recuerdo.")
            puntos["Sabadínguez"] += 1
        elif r1 == 3:
            print("\nSabadínguez: No...Mejor olvidalo.")
        else:
            print("\nOpción invalida")
        input("\n( ❥ Presiona ENTER para continuar )")
    
    elif eleccion_actual == 21:
        print("\nSabadínguez: A veces siento que la gente no me entiende.")
        input("\n( ❥ Presiona ENTER para continuar )")
        print("\n¿Qué respondes?")
        print("1. Yo quiero entenderte, si me dejas.")
        print("2. Bueno, eres complicado.")
        print("3. Eso les pasa a los que leen demasiado.")
        r1 = int(input("\nElige una opción (1-3): "))
        ronda_actual +=1

        if r1 == 1:
            print("\nSabadínguez: ¿En serio? Nunca nadie me habia dicho eso...Gracias.")
            puntos["Sabadínguez"] += 3
        elif r1== 2:
            print("\nSabadínguez: Supongo que sí...")
        elif r1 == 3:
            print("\nSabadínguez: No pense que me vieras así...")
            puntos["Sabadínguez"] -= 1
        else:
            print("\nOpción invalida")
        input("\n( ❥ Presiona ENTER para continuar )")
    
    elif eleccion_actual == 26:
        print("\nSabadínguez: El club de literatura necesita más miembros...")
        input("\n( ❥ Presiona ENTER para continuar )")
        print("\n¿Qué respondes?")
        print("1. Podría unirme, solo si tú me enseñas.")
        print("2. Suena interesante.")
        print("3. Nah, demasiadas letras.")
        r1 = int(input("\nElige una opción (1-3): "))
        ronda_actual +=1

        if r1 == 1:
            print("\nSabadínguez: Excelente, me alegra que te nos unas.")
            puntos["Sabadínguez"] += 3
        elif r1== 2:
            print("\nSabadínguez: Avisame si te quieres unir.")
            puntos["Sabadínguez"] += 1
        elif r1 == 3:
            print("\nSabadínguez: Entiendo...")
        else:
            print("\nOpción invalida")
        input("\n( ❥ Presiona ENTER para continuar )")
    
    elif eleccion_actual == 31:
        print("\nSabadínguez: No es que quiera pasar tiempo contigo... solo coincidimos mucho.")
        input("\n( ❥ Presiona ENTER para continuar )")
        print("\n¿Qué respondes?")
        print("1. Si coincidimos tanto, tal vez es destino.")
        print("2. Sí, pura casualidad.")
        print("3. ¿Me estás stalkeando?")
        r1 = int(input("\nElige una opción (1-3): "))
        ronda_actual +=1

        if r1 == 1:
            print("\nSabadínguez: Si... Me gustaría que asi fuese.")
            puntos["Sabadínguez"] += 3
        elif r1== 2:
            print("\nSabadínguez: Almenos estamos de acuerdo.")
            puntos["Sabadínguez"] += 1
        elif r1 == 3:
            print("\nSabadínguez: Claro que no, olvidalo.")
        else:
            print("\nOpción invalida")
        input("\n( ❥ Presiona ENTER para continuar )")
    
    elif eleccion_actual == 36:
        print("\nSabadínguez: ¿Te gustan los poemas?")
        input("\n( ❥ Presiona ENTER para continuar )")
        print("\n¿Qué respondes?")
        print("1. Especialmente si tú los lees.")
        print("2. Algunos.")
        print("3. No, gracias.")
        r1 = int(input("\nElige una opción (1-3): "))
        ronda_actual +=1

        if r1 == 1:
            print("\nSabadínguez: Si... Me gustaría que asi fuese.")
            puntos["Sabadínguez"] += 3
        elif r1== 2:
            print("\nSabadínguez: Almenos estamos de acuerdo.")
            puntos["Sabadínguez"] += 1
        elif r1 == 3:
            print("\nSabadínguez: Claro que no, olvidalo.")
            puntos["Sabadínguez"] -= 2
        else:
            print("\nOpción invalida")
        input("\n( ❥ Presiona ENTER para continuar )")
    
    elif eleccion_actual == 41:
        print("\nSabadínguez: Hoy estás... diferente.")
        input("\n( ❥ Presiona ENTER para continuar )")
        print("\n¿Qué respondes?")
        print("1. ¿Me lo dices porque me estás observando?")
        print("2. ¿Diferente cómo?")
        print("3. Probablemente dormí mal.")
        r1 = int(input("\nElige una opción (1-3): "))
        ronda_actual +=1

        if r1 == 1:
            print("\nSabadínguez: Si...Me gusta verte")
            puntos["Sabadínguez"] += 3
        elif r1== 2:
            print("\nSabadínguez: Tienes algo...que me cautiva.")
            puntos["Sabadínguez"] += 1
        elif r1 == 3:
            print("\nSabadínguez: Claro...Nunca entiendes nada.")
            puntos["Sabadínguez"] -= 2
        else:
            print("\nOpción invalida")
        input("\n( ❥ Presiona ENTER para continuar )")
    
    elif eleccion_actual == 46:
        print("\nSabadínguez: No sé por qué sigo hablando contigo...")
        input("\n( ❥ Presiona ENTER para continuar )")
        print("\n¿Qué respondes?")
        print("1. Porque en el fondo te gusto.")
        print("2. Porque no tienes a quién más molestar.")
        print("3. Si quieres, me voy.")
        r1 = int(input("\nElige una opción (1-3): "))
        ronda_actual +=1

        if r1 == 1:
            print("\nSabadínguez: Me conoces muy bien...")
            puntos["Sabadínguez"] += 3
        elif r1== 2:
            print("\nSabadínguez: Quizas sí.")
            puntos["Sabadínguez"] += 1
        elif r1 == 3:
            print("\nSabadínguez: No quise decir eso.")
        else:
            print("\nOpción invalida")
        input("\n( ❥ Presiona ENTER para continuar )")

    return ronda_actual
