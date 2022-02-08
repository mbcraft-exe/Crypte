>>> import Crypte

# Chiffrer un simple fichier :
>>> print(Crypte.crypte("Hello World"))

# Sortie :
.57.3.20.20.9.41.62.9.4.20.14

# Déchiffrer une simple chaine de caractères :
>>> print(Crypte.decrypte(".57.3.20.20.9.41.62.9.4.20.14"))

# Sortie :
Hello World

# Chiffrer un fichier (tous types de fichiers contenant du texte et compatible UTF-8) :
>>> print(Crypte.crypte_with_file("fichier.txt"))

# Déchiffrer un fichier (tous types de fichiers contenant du texte et compatible UTF-8) :
>>> print(Crypte.decrypte_with_file("fichier.txt"))

# Ajouter des caractères non-présents par défaut dans les caractères de Crypte :
# Exemple A
>>> Crypte..init_keys("🎎🧥🎁🎆")

# Sortie :
Clés 🎎🧥🎁🎆 ajoutés à Crypte. 

# Exemple B
list = ["🎎", "🧥", "🎁", "🎆"]

>>> Crypte..init_keys(list)

# Sortie :
Clés 🎎🧥🎁🎆 ajoutés à Crypte. 