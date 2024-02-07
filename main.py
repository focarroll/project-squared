#ignore
import os

# import your functions here (example):

#    #folder  #file name        #function name
from programs.utilities.calculator import calculator
from programs.misc.hello import hello
from programs.games.rpg import rpg
from programs.games.quizGame import quizGame

#Catagories for programs:
catagories = ["Miscellaneous",
              "Utilities",
              "Games"]

#add your imported function here:
misc = [hello]

utilities = [calculator]

games = [rpg, quizGame]

def main():
    while (True):
        clear_screen()

        # Choose Catagory
        print("Choose a catagory: \n")

        #show all catagory options
        for i, option in enumerate(catagories):
            print(f'{i+1}. {option}\n')

        #validate input is in range
        choice = -1
        while choice >= len(catagories) or choice < 0:
            try:
                choice = int(input(f'(1-{len(catagories)}): ')) - 1
            except ValueError:
                continue
        
        clear_screen()
        
        # Choose Program
        print("Choose a program: \n")

        programs = None
        match (choice):
            case 0:              
                programs = misc
            case 1:
                programs = utilities
            case 2:
                programs = games

        #show all programs options in catagory
        for i, option in enumerate(programs):
            print(f'{i+1}. {option.__name__}.py\n')

        print(f'{len(programs)+1}. Back\n')
        
        #validate input is in range
        choice = -1
        while choice > len(programs) or choice < 0:
            try:
                choice = int(input(f'(1-{len(programs)+1}): ')) - 1
            except ValueError:
                continue

        if choice == len(programs):
            continue

        #clear_screen()

        programs[choice]()

        return

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == "__main__":
    main()