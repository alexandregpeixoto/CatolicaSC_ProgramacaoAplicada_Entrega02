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


def is_word_guessed(secret_word, letters_guessed):
    """
    secret_word: string, a palavra que o usuário está adivinhando; 
      assume que todas as letras são minúsculas
    letters_guessed: list (de letras), quais letras foram dadas 
      como palpite até agora; assume que todas as letras são minúsculas
    returns: boolean, True se todas as letras de secret_word estiverem
      em letters_guessed; False caso contrário
    """
    # DICA: você pode querer usar a função "all" aqui.
    # ENTRE SEU CÓDIGO AQUI E APAGUE A LINHA "pass"
    pass



def get_guessed_word(secret_word, letters_guessed):
    """
    secret_word: string, a palavra que o usuário está adivinhando
    letters_guessed: list (de letras), quais letras foram dadas 
      como palpite até agora; assume que todas as letras são minúsculas
    returns: string, de letras e underscores (_), que representam
      quais letras em secret_word foram adivinhadas até agora.
    """
    # ENTRE SEU CÓDIGO AQUI E APAGUE A LINHA "pass"
    pass



def get_available_letters(letters_guessed):
    """
    letters_guessed: list (de letras), quais letras foram dadas 
      como palpite até agora; assume que todas as letras são minúsculas
    returns: string (de letras), as letras para as quais o usuário ainda não
      deu palpite.
    """
    # ENTRE SEU CÓDIGO AQUI E APAGUE A LINHA "pass"
    pass



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
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass


# Quando você terminar sua função hangman, role o código
# até o fim e descomente as primeiras duas linhas para testar
# (dica: você pode querer escolher sua própria secret_word
# enquanto estiver testando/desenvolvendo seu programa)
# -----------------------------------

if __name__ == "__main__":
    pass

    # Para testar a parte 2, comente a linha pass acima
    # e descomente as duas linhas abaixo.

    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

