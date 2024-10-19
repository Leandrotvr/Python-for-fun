import random

mensajes = {
    'WELCOME': {
        'es': '¡Bienvenido al juego de adivinanza!',
        'en': 'Welcome to the guessing game!'
    },
    'GUESS': {
        'es': 'Introduce tu número: ',
        'en': 'Enter your number: '
    },
    'BAD_INPUT': {
        'es': 'Por favor, elige un número entre 1 y 100.',
        'en': 'Please choose a number between 1 and 100.'
    },
    'TOO_LOW': {
        'es': 'Demasiado bajo. Intenta de nuevo.',
        'en': 'Too low. Try again.'
    },
    'TOO_HIGH': {
        'es': 'Demasiado alto. Intenta de nuevo.',
        'en': 'Too high. Try again.'
    },
    'CONGRATULATIONS': {
        'es': '¡Felicidades! Adivinaste el número {0} en {1} intentos.',
        'en': 'Congratulations! You guessed the number {0} in {1} tries.'
    },
    'INVALID_INPUT': {
        'es': 'Por favor, introduce un número válido.',
        'en': 'Please enter a valid number.'
    }
}

def adivina_el_numero(idioma):
    numero_secreto = random.randint(1, 100)
    intentos = 0

    print(mensajes['WELCOME'][idioma])
    print(mensajes['GUESS'][idioma])

    while True:
        try:
            adivinanza = int(input(mensajes['GUESS'][idioma]))
            intentos += 1

            if adivinanza < 1 or adivinanza > 100:
                print(mensajes['BAD_INPUT'][idioma])
                continue

            if adivinanza < numero_secreto:
                print(mensajes['TOO_LOW'][idioma])
            elif adivinanza > numero_secreto:
                print(mensajes['TOO_HIGH'][idioma])
            else:
                print(mensajes['CONGRATULATIONS'][idioma].format(numero_secreto, intentos))
                break

        except ValueError:
            print(mensajes['INVALID_INPUT'][idioma])

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
