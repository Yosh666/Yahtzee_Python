import random
from itertools import groupby

neuf =1
dix = 2
valet = 3
dame = 4
roi = 5
As = 6

names={neuf: "9", dix: "10", valet: "J", dame: "Q", roi:"K", As: "A" }

player_score = 0
computer_score = 0

def start():
    print "Welcome to poker Game"
    while game():
        pass
    scores()

def game ()
    print ("Romuald l'ordinateur va lancer vos dés pour vous il est serviable Romuald")
    throws()
    return play_again()

def play_again():
    answer= raw_input("Une autre partie? y/n: ")
    if answer in ("y", "Y", "yes", "oui", "OH OUI!") :
        return answer
    else:
        print("Bon ben tant pis bisous!")

def throws():
    roll_number = 5
    dice = roll(roll_number)
    dice.sort()
    for i in range(len(dice)):
        print ("Dés",i + 1, ";", names[dice[i]])
    result = hand(dice)
    print "vous avez actuellement ", result

    while True:
        rerolls = input("Combien de dés souhaitez vous relancer?")
        try:
            if rerolls in (1, 2, 3, 4, 5):
                break
            except ValueError:
                pass
            print ("Tu dois rentrer  1 2 3 4 ou 5 bon si tu en lances 5 c'est que tu es vraiment mal barré")
            if rerolls== 0: 
                print("Vous terminez avec : "), result
            else: 
                roll_number = rerolls
                dice_rerolls = roll(roll_number)
                print("Entrez le numéro de dés que vous souhaitez relancer ")
                iterations = 0
                while iterations < rerolls:
                    iterations += 1
                    while True
                        selection= input("")
                        try:
                            if selection in (1, 2, 3, 4, 5):
                                break 
                        except ValueError
                            pass
                        print("On a dit de taper un chiffre entre 1 et 5 faut arréter de pertuber Romulad!")
                    dice_changes[iterations-1 ] = replacement
                    print("Vous avez changé de dé", selection) 


