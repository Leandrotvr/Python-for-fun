import random

def adivina_el_numero(idioma):
    numero_secreto = random.randint(1, 100)
    intentos = 0
    
    if idioma == 'es':
        print("¡Bienvenido al juego de adivinanza!")
        print("Estoy pensando en un número entre 1 y 100.")
    else:
        print("Welcome to the guessing game!")
        print("I'm thinking of a number between 1 and 100.")

    while True:
        try:
            if idioma == 'es':
                adivinanza = int(input("Introduce tu adivinanza: "))
            else:
                adivinanza = int(input("Enter your guess: "))
                
            intentos += 1
            
            if adivinanza < 1 or adivinanza > 100:
                if idioma == 'es':
                    print("Por favor, elige un número entre 1 y 100.")
                else:
                    print("Please choose a number between 1 and 100.")
                continue

            if adivinanza < numero_secreto:
                if idioma == 'es':
                    print("Demasiado bajo. Intenta de nuevo.")
                else:
                    print("Too low. Try again.")
            elif adivinanza > numero_secreto:
                if idioma == 'es':
                    print("Demasiado alto. Intenta de nuevo.")
                else:
                    print("Too high. Try again.")
            else:
                if idioma == 'es':
                    print(f"¡Felicidades! Adivinaste el número {numero_secreto} en {intentos} intentos.")
                else:
                    print(f"Congratulations! You guessed the number {numero_secreto} in {intentos} tries.")
                break

        except ValueError:
            if idioma == 'es':
                print("Por favor, introduce un número válido.")
            else:
                print("Please enter a valid number.")

def elegir_idioma():
    while True:
        idioma = input("Elige el idioma / Choose the language (es/en): ").strip().lower()
        if idioma in ['es', 'en']:
            return idioma
        else:
            print("Por favor, elige 'es' para español o 'en' para inglés.")

if __name__ == "__main__":
    idioma = elegir_idioma()
    adivina_el_numero(idioma)

