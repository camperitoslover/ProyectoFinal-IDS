# -*- coding: utf-8 -*-
# Amor en la Escuela Inferior de Economía y Negocios 💕
# Prototipo de dating simulator

def esperar():
    input("\n( Presiona ENTER para continuar... )")

# Puntos de afinidad
puntos = {
    "Sabadínguez": 0,
    "Never": 0,
    "Julian Apple": 0,
    "Teodoro": 0
}

print("🌸 Bienvenido/a a la Escuela Inferior de Economía y Negocios 🌸")
print("Un nuevo ciclo inicia, y con él... la posibilidad de encontrar el amor.")
esperar()

print("Cuatro estudiantes llaman tu atención en el pasillo principal...")
esperar()

print("1. Sabadínguez - el amante de las letras y las tortugas 🐢")
print("2. Never - el líder alegre del consejo estudiantil 📊")
print("3. Julian Apple - el rebelde genio de las matemáticas 📐")
print("4. Teodoro - el programador tímido 💻")

eleccion = input("\n¿Con quién te gustaría hablar primero? (1-4): ")

# ----------------------------------------------------------
# 💬 Ruta 1: Sabadínguez
# ----------------------------------------------------------
if eleccion == "1":
    print("\nTe acercas a Sabadínguez, que está leyendo bajo un árbol.")
    esperar()
    print("💬 Sabadínguez: 'Oh... hola. No muchos se sientan aquí a leer conmigo.'")
    esperar()
    print("¿Qué haces?")
    print("1. Le preguntas qué libro está leyendo.")
    print("2. Le dices que prefieres la economía a la literatura.")
    r1 = input("👉 Elige una opción: ")

    if r1 == "1":
        print("💬 Sabadínguez sonríe: 'Se llama El viejo y el mar. Pocos lo aprecian.'")
        puntos["Sabadínguez"] += 2
    else:
        print("💬 Sabadínguez suspira: 'Bueno... supongo que todos tenemos gustos distintos.'")
        puntos["Sabadínguez"] -= 1
    esperar()

# ----------------------------------------------------------
# 💬 Ruta 2: Never
# ----------------------------------------------------------
elif eleccion == "2":
    print("\nTe encuentras con Never organizando un evento del consejo estudiantil.")
    esperar()
    print("💬 Never: '¡Hey! Necesitamos manos para repartir volantes. ¿Nos ayudas?'")
    esperar()
    print("¿Qué haces?")
    print("1. Aceptas con entusiasmo.")
    print("2. Dices que estás ocupada con tareas.")
    r2 = input("👉 Elige una opción: ")

    if r2 == "1":
        print("💬 Never: '¡Eso sí es espíritu de equipo! Gracias.'")
        puntos["Never"] += 2
    else:
        print("💬 Never: 'Ah, bueno, será la próxima vez.'")
        puntos["Never"] -= 1
    esperar()

# ----------------------------------------------------------
# 💬 Ruta 3: Julian Apple
# ----------------------------------------------------------
elif eleccion == "3":
    print("\nJulian Apple está en el aula de matemáticas resolviendo ecuaciones.")
    esperar()
    print("💬 Julian: '¿Vienes a aprender o a copiar? Jajaja.'")
    esperar()
    print("¿Qué haces?")
    print("1. Le pides que te enseñe un truco matemático.")
    print("2. Le respondes con sarcasmo.")
    r3 = input("👉 Elige una opción: ")

    if r3 == "1":
        print("💬 Julian: 'Interesante... alguien con curiosidad. Me agradas.'")
        puntos["Julian Apple"] += 2
    else:
        print("💬 Julian: 'Vaya, otra que se cree divertida.'")
        puntos["Julian Apple"] -= 1
    esperar()

# ----------------------------------------------------------
# 💬 Ruta 4: Teodoro
# ----------------------------------------------------------
elif eleccion == "4":
    print("\nTeodoro está en la sala de cómputo, concentrado frente a su pantalla.")
    esperar()
    print("💬 Teodoro: 'E-estoy haciendo un programa para calcular promedios... ¿quieres verlo?'")
    esperar()
    print("¿Qué haces?")
    print("1. Le dices que suena genial y te interesa.")
    print("2. Le dices que prefieres hacerlo a mano.")
    r4 = input("👉 Elige una opción: ")

    if r4 == "1":
        print("💬 Teodoro sonríe tímidamente: 'G-gracias... no muchos entienden mi gusto por esto.'")
        puntos["Teodoro"] += 2
    else:
        print("💬 Teodoro baja la mirada: 'Oh... está bien, supongo.'")
        puntos["Teodoro"] -= 1
    esperar()

# ----------------------------------------------------------
# 🎯 Resultado final
# ----------------------------------------------------------
print("\n✨ Fin del día ✨")
print("Revisas mentalmente tus interacciones...")

for p, v in puntos.items():
    print(f"{p}: {v} puntos")

ganador = max(puntos, key=puntos.get)
esperar()

print(f"\n❤️ Sientes que tu conexión más fuerte fue con {ganador}.")
print("Quizá el destino tenga algo preparado entre ustedes... 💕")
print("\n--- FIN DEL PROTOTIPO ---")
