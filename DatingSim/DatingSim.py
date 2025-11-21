# Amor en la Escuela Inferior de Economía y Negocios 💕
# Prototipo de dating simulator

def esperar():
    input("\n( ❥ Presiona ENTER para continuar )")

# Puntos de afinidad

puntos = {
    "Sabadínguez": 0,
    "Neverardo": 0,
    "Julian": 0,
    "Teodoro": 0
}

# Menu principal

print("\nBienvenido/a a la Escuela Inferior de Economía y Negocios")
print("\nUn nuevo ciclo inicia, y con él... la posibilidad de encontrar el amor.")
esperar()

print("\nCuatro estudiantes llaman tu atención en el pasillo principal...")
esperar()

ronda_actual = 1
MAX_RONDAS = 10
n=0

while ronda_actual <= MAX_RONDAS:
    print("1. Sabadínguez - el amante de las letras y las tortugas")
    print("2. Julian Apple - el rebelde genio de las matemáticas")
    print("3. Never - el líder alegre del consejo estudiantil")
    print("4. Teodoro - el programador tímido")
    eleccion = int(input("\n¿Con quién te gustaría hablar ahora? (1-4): "))
    eleccion_actual = n + eleccion
    n += 5

# Ruta 1: Francisco Sabadínguez

    if eleccion_actual == 1:
        print("\nSabadínguez: ¿Qué haces perdiendo el tiempo aquí? …Digo, ¿necesitabas algo?")
        esperar()
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
        esperar()

    if eleccion_actual == 6:
        print("\nSabadínguez: Estoy leyendo esta novela, aunque probablemente no te interese.")
        esperar()
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
        esperar()
    
    if eleccion_actual == 11:
        print("\nSabadínguez: Me dijeron que hay tortugas en el estanque hoy.")
        esperar()
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
        esperar()
    
    if eleccion_actual == 16:
        print("\nSabadínguez: Recordé algo que me dijiste hace días. No pensé que fuera importante...")
        esperar()
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
        esperar()
    
    if eleccion_actual == 21:
        print("\nSabadínguez: A veces siento que la gente no me entiende.")
        esperar()
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
        esperar()
    
    if eleccion_actual == 26:
        print("\nSabadínguez: El club de literatura necesita más miembros...")
        esperar()
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
        esperar()
    
    if eleccion_actual == 31:
        print("\nSabadínguez: No es que quiera pasar tiempo contigo... solo coincidimos mucho.")
        esperar()
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
        esperar()
    
    if eleccion_actual == 36:
        print("\nSabadínguez: ¿Te gustan los poemas?")
        esperar()
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
        esperar()
    
    if eleccion_actual == 41:
        print("\nSabadínguez: Hoy estás... diferente.”")
        esperar()
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
        esperar()
    
    if eleccion_actual == 46:
        print("\nSabadínguez: No sé por qué sigo hablando contigo...")
        esperar()
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
        esperar()
        
# Ruta 2: Julian Apple

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

# Ruta 3: Neverardo Llanura

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

    if eleccion_actual == 8:
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

    if eleccion_actual == 13:
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

    if eleccion_actual == 18:
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

    if eleccion_actual == 23:
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

    if eleccion_actual == 28:
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

    if eleccion_actual == 33:
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

    if eleccion_actual == 38:
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

    if eleccion_actual == 43:
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

    if eleccion_actual == 48:
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

# Ruta 4: Teodoro Portillo

    if eleccion_actual == 4:
        print("\nTeodoro: Ah... hola. No pensé que me saludaras.")
        esperar()
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
        esperar()

    if eleccion_actual == 9:
        print("\nTeodoro: Estoy programando algo pequeño para la clase.")
        esperar()
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
        esperar()

    if eleccion_actual == 14:
        print("\nTeodoro: ¿Has visto Alvin y las ardillas?")
        esperar()
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
        esperar()

    if eleccion_actual == 19:
        print("\nTeodoro: ¿Te gusta el anime?")
        esperar()
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
        esperar()

    if eleccion_actual == 24:
        print("\nTeodoro: Me da pena cuando la gente me mira.")
        esperar()
        print("\n¿Qué respondes?")
        print("1. No tienes por qué, eres increíble.")
        print("2. Un poco tímido sí eres.")
        print("3. Entonces no te veré.")
        r = int(input("\nElige una opción (1-3): "))
        ronda_actual += 1

        if r == 1:
            print("\nTeodoro: ¿I-increíble yo? ...Gracias... eso me anima mucho.")
            puntos["Teodoro"] += 3
        elif r == 2:
            print("\nTeodoro: Jaja, sí... un poquito.")
            puntos["Teodoro"] += 1
        elif r == 3:
            print("\nTeodoro: No, n-no, sí quiero que me veas... a veces.")
        else:
            print("\nOpción inválida")
        esperar()

    if eleccion_actual == 29:
        print("\nTeodoro: Hice galletas... ¿quieres?")
        esperar()
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
        esperar()

    if eleccion_actual == 34:
        print("\nTeodoro: Estuve jugando un RPG anoche.")
        esperar()
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
        esperar()

    if eleccion_actual == 39:
        print("\nTeodoro: A veces pienso que soy muy débil.")
        esperar()
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
        esperar()

    if eleccion_actual == 44:
        print("\nTeodoro: ¿Crees que soy una carga?")
        esperar()
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
        esperar()

    if eleccion_actual == 49:
        print("\nTeodoro: Nunca pensé que alguien quisiera pasar tiempo conmigo.")
        esperar()
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
        esperar()

# Resultado final (Confesión)

print("\nDespues de pensarlo mucho, decides confesarle tu amor a una persona especial...")
esperar()

print("1. Sabadínguez - el amante de las letras y las tortugas")
print("2. Julian Apple - el rebelde genio de las matemáticas")
print("3. Never - el líder alegre del consejo estudiantil")
print("4. Teodoro - el programador tímido")
eleccion = int(input("\n¿A quién quieres confesarle tus sentimientos?: "))
confesion = True

while confesion == True:
    if eleccion == 1:
        if puntos["Sabadínguez"] >= 20:
            print("\nSabadínguez ha aceptado tu confesión. Ambos se dan su primer beso mientras una lluvia de cerezos cae lentamente.")
            print("\nFin del Juego")
            print("¡Gracias por Jugar!")
            break
        else:
            print("\nSabadínguez ha rechazado tu confesión. La relación entre ambos se vuelve incomoda...pero quiza puedas encontrar el amor en otro lugar.")
            print("\nFin del Juego")
            print("¡Gracias por Jugar!")
            print(puntos["Sabadínguez"])
            break

    if eleccion == 2:
        if puntos["Julian"] >= 20:
            print("\nJulian ha aceptado tu confesión. Ambos se dan su primer beso mientras una lluvia de cerezos cae lentamente.")
            print("\nFin del Juego")
            print("¡Gracias por Jugar!")
            break
        else:
            print("\nJulian ha rechazado tu confesión. La relación entre ambos se vuelve incomoda...pero quiza puedas encontrar el amor en otro lugar.")
            print("\nFin del Juego")
            print("¡Gracias por Jugar!")
            break
            
    if eleccion == 3:
        if puntos["Neverardo"] >= 20:
            print("\nNeverardo ha aceptado tu confesión. Ambos se dan su primer beso mientras una lluvia de cerezos cae lentamente.")
            print("\nFin del Juego")
            print("¡Gracias por Jugar!")
            break
        else:
            print("\nNeverardo ha rechazado tu confesión. La relación entre ambos se vuelve incomoda...pero quiza puedas encontrar el amor en otro lugar.")
            print("\nFin del Juego")
            print("¡Gracias por Jugar!")
            break

    if eleccion == 4:
        if puntos["Teodoro"] >= 20:
            print("\nTeodoro ha aceptado tu confesión. Ambos se dan su primer beso mientras una lluvia de cerezos cae lentamente.")
            print("\nFin del Juego")
            print("¡Gracias por Jugar!")
            break
        else:
            print("\nTeodoro ha rechazado tu confesión. La relación entre ambos se vuelve incomoda...pero quiza puedas encontrar el amor en otro lugar.")
            print("\nFin del Juego")
            print("¡Gracias por Jugar!")
            break