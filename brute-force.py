#/usr/bin/python3
#coding: utf-8

'''

# les bibliothèques
from itertools import product

# toutes les possibilitées possible
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_+=~`[]{}:;\"'<>,.?/\\"

# fichie en écriture qui sera résultat.txt
fichier = open("résultat.txt", "w", encoding = "utf8")

# boucle for
for p in range (2,15):
    for cc in product(alphabet, repeat=p):
        ligne = ''.join(cc) + '\n'
        fichier.write(ligne)
# fermeture du file
fichier.close()   


#------------------------------------------------------------------------------------------------------------

'''
# second brute force 

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_+=~`[]{}:;\"'<>,.?/\\"


def brute_force(word, length):

    if length <= 5:
        for lettre in alphabet:
            if password == word + alphabet:
                print ("vous avez trouvé le mot de passe" + word + lettre )
            else:
                print (word + lettre)
                brute_force(word + lettre, length + 1)
            
password = input ("entre ton mot de passe =)")
brute_force('', 1)























