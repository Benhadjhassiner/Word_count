# Définition de la fonction count_word

def count_word(phrase):
    phrase.strip()
    mots = phrase.count(" ")
    return mots + 1
