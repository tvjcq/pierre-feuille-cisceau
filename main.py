##################################################
#                                                #
#                                                #
#   ██████╗  ██████╗ ██████╗ ██████╗ ██╗   ██╗   #
#   ██╔══██╗██╔═══██╗██╔══██╗██╔══██╗╚██╗ ██╔╝   #
#   ██████╔╝██║   ██║██████╔╝██████╔╝ ╚████╔╝    #
#   ██╔══██╗██║   ██║██╔══██╗██╔══██╗  ╚██╔╝     #
#   ██████╔╝╚██████╔╝██████╔╝██████╔╝   ██║      #
#   ╚═════╝  ╚═════╝ ╚═════╝ ╚═════╝    ╚═╝      #
#                                                #
#                                                #
##################################################

import random
import time

choice_random = [
    "Pierre !",
    "Feuille !",
    "Cisceaux !"
]

rock = "Pierre !"
paper = "Feuille !"
scissors = "Cisceaux !"

robot_choice = ""

user_choice = ""


def random_choice():
    global choice_random
    robot_choice = random.choice(choice_random)
    if robot_choice == "Feuille !" :
        robot_choice = paper
    elif robot_choice == "Cisceaux !" :
        robot_choice = scissors
    else:
        robot_choice = rock
    return robot_choice


def verif():
    while True :
        global user_choice
        user_choice = input("Quel coup voulez vous jouez ?"
                     + " (1 = Pierre /"
                     + " 2 = Feuille /"
                     + " 3 = Cisceaux) : ")
        if not user_choice.isdigit():
            print("Rentre un chiffre !")
        elif not 1 <= int(user_choice) <= 3:
            print("Rentre sois 1 sois 2 sois 3 mais pas un autre !")
        else:
            user_choice = int(user_choice)
            break





def who_wins():
    global user_choice
    global robot_choice
    global rock
    global paper
    global scissors
    print(robot_choice)
    if robot_choice == rock :
        if user_choice == 2 :
            print("Tu as gagné !")
        elif user_choice == 3 :
            print("Tu as perdu.")
        else :
            print("Egalité.")
    elif robot_choice == paper :
        if user_choice == 3 :
            print("Tu as gagné !")
        elif user_choice == 1 :
            print("Tu as perdu.")
        else :
            print("Egalité.")
    else :
        if user_choice == 1 :
            print("Tu as gagné !")
        elif user_choice == 2 :
            print("Tu as perdu.")
        else :
            print("Egalité.")




robot_choice = random_choice()
verif()
who_wins()
while True:
    replay = input("On rejoue ? (Y/N)")
    if replay.upper() == "Y":
        robot_choice = random_choice()
        verif()
        who_wins()
    elif replay.upper() == "N":
        print("A la prochaine !")
        time.sleep(2)
        break
    else:
        print("Y ou N")
