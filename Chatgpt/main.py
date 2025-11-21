# Amor en la Escuela Inferior de Economía y Negocios ♡
# Prototipo de dating simulator ♡

#Importación y definición de funciones necesarias:

ronda_actual = 1
MAX_RONDAS = 10
n=0

def esperar():
    input("\n( ❥ Presiona ENTER para continuar )")
    
from Julian_dialogos import dialogos_julian
from Neverardo_dialogos import dialogos_neverardo
from Sabadinguez_dialogos import dialogos_sabadinguez
from Teodoro_dialogos import dialogos_teodoro

# Puntos de afinidad

puntos = {
    "Sabadínguez": 0,
    "Neverardo": 0,
    "Julian": 0,
    "Teodoro": 0
}
        
# Menu de selección de personaje:

print("\nBienvenido/a a la Escuela Inferior de Economía y Negocios")
print("\nUn nuevo ciclo inicia, y con él... la posibilidad de encontrar el amor.")
esperar()

print("\nCuatro estudiantes llaman tu atención en el pasillo principal...")
esperar()

while ronda_actual <= MAX_RONDAS:
    print("1. Sabadínguez - el amante de las letras y las tortugas")
    print("2. Julian Apple - el rebelde genio de las matemáticas")
    print("3. Never - el líder alegre del consejo estudiantil")
    print("4. Teodoro - el programador tímido")
    eleccion = int(input("\n¿Con quién te gustaría hablar ahora? (1-4): "))
    eleccion_actual = n + eleccion
    
    print(eleccion_actual)
    print(ronda_actual)
    print(n)
        
    # Ejecución de dialogos de personaje seleccionado

    if eleccion == 1:
        ronda_actual = dialogos_sabadinguez(eleccion_actual, ronda_actual, puntos)
    elif eleccion == 2:
        ronda_actual = dialogos_julian(eleccion_actual, ronda_actual, puntos)
    elif eleccion == 3:
        ronda_actual = dialogos_neverardo(eleccion_actual, ronda_actual, puntos)
    elif eleccion == 4:
        ronda_actual = dialogos_teodoro(eleccion_actual, ronda_actual, puntos)
    else:
        print("Opción invalida")
    n += 5

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
    break