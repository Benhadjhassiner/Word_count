# Définition de la fonction count_word

#L'input est la phrase que l'utilisateur donnera
def count_word(phrase):
    phrase.strip()
    #La fonction va compter le nomre de mots
    mots = phrase.count(" ")
    return mots + 1
    #L'output est le nombre de mots qu'on retournera
