# Définition de la fonction count_word

def count_word(phrase): #L'input est la phrase que l'utilisateur donnera, ici la variable "phrase"
    phrase.strip()
    #La fonction va compter le nombre de mots d'une chaîne de caractères
    mots = phrase.count(" ")
    return mots + 1 
    #L'output est un nombre de mots qu'on retournera, ici la variable "mots" auquelle on ajoute 1
