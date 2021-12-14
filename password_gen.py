import string
import random


## Les caractères utilisés pour générer le mot de passe
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generate_random_password():
	## la taille du mot de passe choisie
	length = int(input("Entrez la taille du mot de passe désirée: "))

	## Mélange aléatoire des caractères
	random.shuffle(characters)
	
	## Choix aléatoire des caractères à partir de la liste
	password = []
	for i in range(length):
		password.append(random.choice(characters))

	## Mélange aléatoire de la liste obtenue
	random.shuffle(password)

	## convertion de la liste de caractère obtenue après mèlange en une chaine de caractère
	## impression de cette liste
	print("".join(password))



## invoking the function
generate_random_password()
