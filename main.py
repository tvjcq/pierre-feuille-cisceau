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

choice_random = [
    "Pierre !",
    "Feuille !",
    "Cisceaux !"
]

# rock = "Pierre !"
# paper = "Feuille !"
# scissors = "Cisceaux"

robot_choice = ""

user = ""


def random_choice():
    global choice_random
    robot_choice = random.choice(choice_random)
    return robot_choice


def verif():
    global user
    user = input("Quel coup voulez vous jouez ?"
                 + " (1 = Pierre /"
                 + " 2 = Papier /"
                 + " 3 = Cisceaux) : ")
    if not user.isdigit():
        print("Rentre un chiffre du con")
        print()
        verif()
    elif not 1 <= int(user) <= 3:
        print("Rentre sois 1 sois 2 sois 3 mais pas un autre sale dindasse")
        print()
        verif()
    user = int(user)




# def who_wins(user, robot):

verif()
