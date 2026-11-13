import random

# Constantes de las jugadas
PIEDRA = "piedra"
PAPEL = "papel"
TIJERAS = "tijeras"

def decidir_ganador(user_action, computer_action):
    """
    decide el resultado de la ronda usando condicionales anidados
    cubriendo las combinaciones posibles entre usuario y ordenador
    """
    if user_action == computer_action:
        print(f"Usuario y ordenador eligieron {user_action}. Empate!")
    
    elif user_action == PIEDRA:
        if computer_action == TIJERAS:
            print("Piedra rompe tijeras. Ganaste!")
        else: # computer_action == PAPEL
            print("Papel envuelve piedra. Perdiste.")
            
    elif user_action == PAPEL:
        if computer_action == PIEDRA:
            print("Papel envuelve piedra. Ganaste!")
        else: # computer_action == TIJERAS
            print("Tijeras cortan papel. Perdiste.")
            
    elif user_action == TIJERAS:
        if computer_action == PAPEL:
            print("Tijeras cortan papel. Ganaste!")
        else: # computer_action == PIEDRA
            print("Piedra rompe tijeras. Perdiste.")
            
    else:
        print("Opción no válida.")

def main():
    """
    función principal que gestiona el bucle del juego.
    el usuario puede jugar varias rondas seguidas hasta salir con Ctrl+C.
    """
    opciones_validas = [PIEDRA, PAPEL, TIJERAS]
    
    print("Bienvenido al juego de Piedra, Papel o Tijera!")
    print("Para salir del juego en cualquier momento, presiona Ctrl + C.\n")
    
    while True:
        # Solicitar entrada al usuario
        user_action = input("Elige una opción (piedra, papel o tijera): ").lower().strip()
        
        # Validar que la entrada sea correcta
        if user_action not in opciones_validas:
            print("⚠️ Opción incorrecta. Por favor, escribe piedra, papel o tijera.")
            continue
            
        # El ordenador elige al azar
        computer_action = random.choice(opciones_validas)
        
        print(f"\nElegiste {user_action}. El ordenador eligió {computer_action}")
        
        # Llamar a la función para decidir el ganador
        decidir_ganador(user_action, computer_action)
        print("-" * 40)

if __name__ == "__main__":
    main()