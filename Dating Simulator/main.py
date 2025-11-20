#Pantalla de inicio
print("EIEN Dating Simulator ❤︎₊ ⊹")
print("El destino tiene formas curiosas de unir a las personas… ")
print("¿Podrás encontrar el amor verdadero o perderte entre las palabras?")
print(".  +     \n ˚⠀ ⣴⠟⠉⠉⠛⢦⡀⢀⣴⠛⠉⠈⠙⠻⣄\n  ⣼⠃⠀⠀⠀⠀⠀⠙⠋⠀⠀⠀⠀⠀⠀⠹⣦\n ⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿\n ⠀⠿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡆\n  ⠀⢻⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡼⠃\n ⠀⠀⠀⠀⠻⢦⣄⠀⠀⠀⠀⠀⣠⡴⠛\n ⠀⠀⠀⠀⠀⠀⠉⠛⠶⣄⠶⠋    +.  *")

#Menu principal
def menu():
    while True:
        print("\n--- 𝑀𝑒𝓃ú 𝒫𝓇𝒾𝓃𝒸𝒾𝓅𝒶𝓁 ---")
        print("1. Iniciar")
        print("2. ¿Cómo jugar?")
        print("3. Créditos")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")
        
#Los prints son para que no me de error nomás chikos :(
        if opcion == "1":
            print() #espacio para función donde se desglosen los diálogos y eso uwu
        elif opcion == "2":
            print() #
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida.")

menu()