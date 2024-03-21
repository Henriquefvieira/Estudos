import random

palavras = ['python', 'java', 'ruby', 'javascript', 'html', 'css', 'php']

def escolher_palavra(palavras):
    return random.choice(palavras)

def mostrar_palavra_oculta(palavra, letras_corretas):
    """Função para mostrar a palavra oculta com as letras corretas adivinhadas."""
    oculta = ''
    for letra in palavra:
        if letra in letras_corretas:
            oculta += letra
        else:
            oculta += '_'
    return oculta

def jogar_forca():
    palavra = escolher_palavra(palavras)
    letras_corretas = []
    tentativas_restantes = 6

    print("Bem-vindo ao jogo da forca!")
    print("A palavra tem", len(palavra), "letras.")

    while tentativas_restantes > 0:
        print("\nPalavra:", mostrar_palavra_oculta(palavra, letras_corretas))
        letra = input("Digite uma letra: ").lower()

        if letra in letras_corretas:
            print("Você já tentou esta letra. Tente outra.")
            continue

        if letra in palavra:
            print("Letra correta!")
            letras_corretas.append(letra)
        else:
            print("Letra incorreta. Tente novamente.")
            tentativas_restantes -= 1

        if '_' not in mostrar_palavra_oculta(palavra, letras_corretas):
            print("\nParabéns! Você adivinhou a palavra:", palavra)
            break

        print("Tentativas restantes:", tentativas_restantes)

    if tentativas_restantes == 0:
        print("\nFim de jogo! Você não conseguiu adivinhar a palavra. A palavra era:", palavra)

# Iniciar o jogo da forca
jogar_forca()