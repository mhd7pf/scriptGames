import random

#head game

print("*** bienvenue dans FUME MOI OU JE TE FUME ***".title())
print("Vous allez affronter un ennemi redoutable !")
print("Vous avez 3 potions pour vous soigner pendant le combat.")
print("Bonne chance !")

def play():
    player_healph = 100
    ennemy_healph = 100
    print("point de vie joueur 🔰: ",player_healph, "// point de vie Ennemy 🔱: ", 100)
    lim = "~" * 70
    nbr_potion = 3
    rejouer = ""

    #gameplay

    while True :
        user_choice = input("<> souhaitez-vous attaquer ⚔️  (1) ou utiliser une potion 🧪 (2) ? : ")
        if user_choice == "1" :
            player_attaque = random.randint(5, 15)
            ennemy_healph -= player_attaque
            if ennemy_healph <= 0 :
                ennemy_healph = 0
                print(f"Degats sur ennemy *{player_attaque}* 🩸 // Points de vie ennemy 🔱  restant {ennemy_healph} . ")
                print("felicitation ! Vous avez gagnez ! 🤩 🥳 🎉 🎊 🎖️ ".capitalize())
                while True:
                    rejouer = input("Voulez-vous rejouer ? (o/n) : ").lower()
                    if rejouer == "o" :
                        print("C'est reparti !")
                        play()
                        break
                    elif rejouer == "n" :
                        print("Merci d'avoir joué ! À bientôt !")
                        print("<|> fin du jeu. 🔚".upper())
                        break
                    else :
                        print("❌ Veuillez répondre par 'o' ou 'n'.")
            else :
                print(f"Degats sur ennemy *{player_attaque}* 🩸 // Points de vie ennemy 🔱  restant {ennemy_healph} . ")
        elif user_choice == "2" :
            if nbr_potion > 0 and player_healph < 100 :
                potion_add = random.randint(20, 30)
                print(f"vous avez utiliser une potion 🧪  + {potion_add} point de vie. ")
                player_healph += potion_add
                nbr_potion -= 1
                print(f"~ Il vous reste {nbr_potion} potions 🧪 ")
                print("♻️  Vous avez passer votre tour. ")
            elif player_healph >= 100 :
                print("💯 Vos points de vie sont au maximum !")
                continue
            else :
                print("✖️  vous n'avez plus de potion. 🧪 ")
                continue
        else :
            print("❌ veuillez entrer un choix valide !")
            continue
        
        

        ennemy_attaque = random.randint(10, 20)
        player_healph -= ennemy_attaque
        if player_healph <= 0 :
            player_healph = 0
            print(f"Degats sur player *{ennemy_attaque}* 🩸 // Points de vie playeur 🔰 restant {player_healph}.  ")
            print("Dommage ! Vous avez perdu !☹️  ❌ ")
            print("Vous fairez mieux la prochaine foix !!! ") 
            print(f"~ Il vous reste {nbr_potion} potions 🧪 ")
            while True:
                rejouer = input("Voulez-vous rejouer ? (o/n) : ").lower()
                if rejouer == "o" :
                    print("C'est reparti !")
                    play()
                    break
                elif rejouer == "n" :
                    print("Merci d'avoir joué ! À bientôt !")
                    print("<|> fin du jeu. 🔚".upper())
                    break
                else :
                    print("❌ Veuillez répondre par 'o' ou 'n'.")
        else :
            print(f"Degats sur player *{ennemy_attaque}* 🩸 // Points de vie playeur 🔰 restant {player_healph}.  ")
            print(lim)

play() #lancer le jeu