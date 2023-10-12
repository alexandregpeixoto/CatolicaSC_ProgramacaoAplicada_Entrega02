# Atividade 2, hangman.py
# Nome:
# Tempo gasto:

# Jogo da Forca
# -----------------------------------
# Funções auxiliares
# Você não precisa entender o código a seguir,
# mas você precisará saber como usá-lo!
# Então, certifique-se de ler as docstrings dos métodos.
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Retorna uma lista de palavras válidas.
    As palavras são strings de letras minúsculas.

    Dependendo do tamanho da lista de palavras, esta função pode
    levar um tempo para terminar.
    """
    print("Carregando lista de palavras do arquivo...")
    # in_file: file stream
    in_file = open(WORDLIST_FILENAME, 'r')
    # line: string
    wordlist = in_file.readlines()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): lista de palavras (strings)

    Retorna uma palavra aleatória da wordlist
    """
    return random.choice(wordlist)

# fim das funções auxiliares

# -----------------------------------

# Carrega a lista de palavras na variável wordlist
# para que ela possa ser acessada de qualquer lugar do programa
wordlist = load_words()

def print_forca(attempts):
    # Imprime o desenho da forca com base no número de tentativas restantes.
    if attempts == 6:
        print(f"""
        _____
        |   |
        |      
        |         Tentativas restantes: {attempts}
        |    
        |______
        """)
    elif attempts == 5:
        print(f"""
        _____
        |   |
        |   O   
        |         Tentativas restantes: {attempts}
        |    
        |______
        """)
    elif attempts == 4:
        print(f"""
        _____
        |   |
        |   O   
        |   |     Tentativas restantes: {attempts}
        |    
        |______
        """)
    elif attempts == 3:
        print(f"""
        _____
        |   |
        |   O   
        |  /|     Tentativas restantes: {attempts}
        |   
        |______
        """)
    elif attempts == 2:
        print(f"""
        _____
        |   |
        |   O   
        |  /|\\   Tentativas restantes: {attempts}
        |   
        |______
        """)
    elif attempts == 1:
        print(f"""
        _____
        |   |
        |   O   
        |  /|\\   Tentativas restantes: {attempts}
        |  /   
        |______
        """)
    elif attempts == 0:
        print(f"""
        _____
        |   |
        |   O   
        |  /|\\   Tentativas restantes: {attempts}
        |  / \\  
        |______
        """)
    else:
        print("Número de tentativas inválido!")


def is_word_guessed(secret_word, letters_guessed):
    """
    secret_word: string, a palavra que o usuário está adivinhando; 
      assume que todas as letras são minúsculas
    letters_guessed: list (de letras), quais letras foram dadas 
      como palpite até agora; assume que todas as letras são minúsculas
    returns: boolean, True se todas as letras de secret_word estiverem
      em letters_guessed; False caso contrário
    """

    # current_word = ''
    # for letter in secret_word:
    #     if letter in letters_guessed:
    #         current_word += letter + ' '
    #     else:
    #         current_word += ' _ '
    return all(letra in letters_guessed for letra in secret_word)


def get_guessed_word(secret_word, letters_guessed):
    """
    secret_word: string, a palavra que o usuário está adivinhando
    letters_guessed: list (de letras), quais letras foram dadas 
      como palpite até agora; assume que todas as letras são minúsculas
    returns: string, de letras e underscores (_), que representam
      quais letras em secret_word foram adivinhadas até agora.
    """
    current_word = ''
    for letter in secret_word:
        if letter in letters_guessed:
            current_word += letter + ' '
        else:
            current_word += ' _ '
    return current_word


def get_available_letters(letters_guessed):
    """
    letters_guessed: list (de letras), quais letras foram dadas 
      como palpite até agora; assume que todas as letras são minúsculas
    returns: string (de letras), as letras para as quais o usuário ainda não
      deu palpite.
    """
    # chr(i) converte em char os valores ASCII das letras mínusculas de a até z
    lowercase_alphabet = [chr(i) for i in range(97, 123)]
    # adiciona letra na lista missing_letters quando
    # cada letra de lowercase_alphabet não estiver na lista letters_guessed
    missing_letters = [letra for letra in lowercase_alphabet if letra not in letters_guessed]
    return missing_letters

# Utilizado para contar a quantidade de letras únicas na palavra secreta. Parte da pontuação final do usuário.
def number_of_unique_letters(secret_word):
    unique_letters = set(secret_word)
    return len(unique_letters)

def hangman(secret_word):
    """
    secret_word: string, a palavra secreta a ser adivinhada.
    Inicia um jogo interativo de Forca.

    * No início do jogo, deixe o usuário saber quantas
      letras a secret_word contém e quantas tentativas ele tem.

    * O usuário deve começar com 6 tentativas

    * Antes de cada rodada, você deve mostrar ao usuário quantas tentativas
      ele ainda possui e quais letras o usuário ainda não tentou um palpite.

    * Peça ao usuário para fornecer um palpite por rodada. 
      Lembre-se de verificar se o usuário digita uma letra!

    * O usuário deve receber feedback imediatamente após cada palpite
      sobre se a letra aparece ou não na palavra secreta.

    * Após cada palpite, você deve mostrar ao usuário a
      palavra parcialmente adivinhada até agora.

    Siga os outros requisitos detalhados na descrição do problema.
    """
    # Chances iniciais
    attempts = 6
    # Inicializa o contador de rounds
    round = 1
    # Comprimento da palavra secreta
    comprimento = len(secret_word.strip())
    print(f"A palavra secreta possuí {comprimento} letras! ")
    # Cria uma lista para armazenar as letras digitadas
    letters_guessed = []
    while attempts != 0:
        # Imprime um separador de rodada
        print(f"                                               ")
        print(f"________________ ROUND {round} ________________")
        # Imprime a forca
        print_forca(attempts)

        # Mostra as letras disponíveis
        available_letters = get_available_letters(letters_guessed)
        print("Letras disponíveis:")
        print(available_letters)
        # Imprime a palavra secreta
        print("Palavra secreta:")
        print(get_guessed_word(secret_word,letters_guessed))

        # Usado para sinalizar a entrada correta do usuário
        correct_entry = False
        # Executa um loop para garantir a entrada correta do usuário
        while not correct_entry:
            # Solicita a entrada de uma letra
            letter = input("Digite uma letra: ")
            # Verifica se o comprimento da letra é 1 para garantir que o usuário digite apenas uma letra por vez
            # Também, verifica se o valor ASCII da letra digita está entra os valores das letras mínusculas, de 97 a 122
            if len(letter) == 1 and 97 <= ord(letter) <= 122:
                if letter in letters_guessed:
                    print("Você já tentou esta letra.")
                else:
                    correct_entry = True
                    letters_guessed.append(letter)
                    # Verifica se a palavra secreta contém a letra digita
                    if letter in secret_word:
                        print("A letra digitada está correta.")
                    else:
                        print("A letra digitada está incorreta.")
                        # Reduz as tentativas disponíveis
                        attempts -= 1
            else:
                print(f"{letter} não é uma letra válida!")

        if is_word_guessed(secret_word, letters_guessed):
            break

        round += 1


    if is_word_guessed(secret_word, letters_guessed):
        # Calcula a pontuação
        total_score = int(len(get_available_letters(letters_guessed)) * number_of_unique_letters(secret_word))
        # Imprime os dados de vitória
        print(f"                                               ")
        print(f"________________ VOCÊ GANHOU! _________________")
        print_forca(attempts)
        print(f"Você adivinhou a palavra {secret_word}!")
        print(f"Pontuação final: {total_score}")
    else:
        print(f"                                               ")
        print(f"________________ VOCÊ PERDEU! _________________")
        print_forca(attempts)
        print(f"Você não adivinhou a palavra {secret_word}!")


# Quando você terminar sua função hangman, role o código
# até o fim e descomente as primeiras duas linhas para testar
# (dica: você pode querer escolher sua própria secret_word
# enquanto estiver testando/desenvolvendo seu programa)
# -----------------------------------

if __name__ == "__main__":

    # Para testar a parte 2, comente a linha pass acima
    # e descomente as duas linhas abaixo.

    secret_word = choose_word(wordlist)
    # Remove qualquer espaço em branco da palavra
    secret_word = secret_word.strip()
    hangman(secret_word)

