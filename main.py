# Création de la fonction count_word
def count_word():
    return (len(phrase.split(' ')))

# On demande à l'utilisateur sa phrase
phrase = str(input("Écrivez une phrase afin d'en compter le nombre de mots: "))

# Création de la variable pour la f-string
reponse = f"Votre chaîne de caractères contient {count_word()} mots et onomatopées."

# On donne le nombre de mots dans la phrase de l'utilisateur
print(reponse)