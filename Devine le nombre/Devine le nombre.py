import random

#head code

print("*^*♤ Bienvenue dans le jeu du nombre mistère*^*".title())
def aide():
	print("Vous devez deviner un nombre entre 0 et 100.")
	print("Vous avez 5 essais pour trouver le bon nombre.")
	print("Après chaque essai, vous recevrez un indice pour vous aider.")
	print("Bonne chance !")
	nbrm = random.randint(0, 100)
	nbr_essais = 5
	lim = "*" * 61
	reessai = ""

	#gameplay

	while True :
		a = input("<> Devine le nombre : ")
		if a.isdigit() :
			if int(a) > nbrm :
				print("C'est moin *-*")
				nbr_essais -= 1
				print(f"Il vous reste {nbr_essais} essais. ")
				print(lim)
			elif int(a) < nbrm :
				print("C'est plus *+*")
				nbr_essais -= 1
				print(f"Il vous reste {nbr_essais} essais. ")
				print(lim)
			elif int(a) == nbrm :
				nbr_essais -= 1
				nfoix = 5 - nbr_essais
				print(f"🥳 🎉 Félicitation ! vous avez réussi au bout de {nfoix} essais.")
				while True:
					reessai = input("Voulez-vous rejouer ? (o/n) : ").lower()
					if reessai == "o" :
						aide()
						break
					elif reessai == "n" :
						print("Merci d'avoir joué ! À bientôt !")
						break
					else :
						print("❌ Veuillez répondre par 'o' ou 'n'.")
		else :
			print("❌ Veuillez entrer un nombre valide")
			continue	
		if nbr_essais <= 0 :
			print(f"Dommage! Vous avez perdu! le nombre à deviner était le '{nbrm}'")
			while True:
					reessai = input("Voulez-vous rejouer ? (o/n) : ").lower()
					if reessai == "o" :
						aide()
						break
					elif reessai == "n" :
						print("Merci d'avoir joué ! À bientôt !")
						break
					else :
						print("❌ Veuillez répondre par 'o' ou 'n'.")

aide()  # Start the game

