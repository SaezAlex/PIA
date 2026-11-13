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