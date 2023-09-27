#La fonction compte le nombre de mots d'une chaîne de caractères de type string. L'input est la phrase qu'on rentre et l'output est le nombre de mots qui nous sera retourné
def count_word(phrase):
    phrase.strip()
    mots = phrase.count(" ")
    return mots + 1 
    
