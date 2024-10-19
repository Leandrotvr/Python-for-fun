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

def obtener_mensajes_traducidos(idioma):
    """Devuelve un diccionario de mensajes traducidos al idioma especificado."""
    return {clave: mensajes[clave][idioma] for clave in mensajes}

def adivina_el_numero(idioma):
    translatedMessages = obtener_mensajes_traducidos(idioma)
    numero_secreto = random.randint(1, 100)
    intentos = 0

    print(translatedMessages['WELCOME'])
    print(translatedMessages['GUESS'])

    while True:
        try:
            adivinanza = int(input(translatedMessages['GUESS']))
            intentos += 1

            if adivinanza < 1 or adivinanza > 100:
                print(translatedMessages['BAD_INPUT'])
                continue

            if adivinanza < numero_secreto:
                print(translatedMessages['TOO_LOW'])
            elif adivinanza > numero_secreto:
                print(translatedMessages['TOO_HIGH'])
            else:
                print(translatedMessages['CONGRATULATIONS'].format(numero_secreto, intentos))
                break

        except ValueError:
            print(translatedMessages['INVALID_INPUT'])

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
