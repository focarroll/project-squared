#ignore
import os

# import your functions here (example):

#    #folder  #file name        #function name
from programs.utilities.calculator import calculator
from programs.misc.hello import hello
from programs.misc.words import word
from programs.games.rpg import rpg

#Catagories for programs:
catagories = ["Miscellaneous",
              "Utilities",
              "Games"]

#add your imported function here:
misc = [hello, 
        word]

utilities = [calculator]

games = [rpg]

def main():
    #clear screen
    while (True):
        # Choose Catagory
        os.system('cls' if os.name == 'nt' else 'clear')

        print("Choose a catagory: \n")

        #show all catagory options
        for i, option in enumerate(catagories):
            print(f'{i+1}. {option}\n')

        print(f'{len(catagories)+1}. Back\n')

        #validate input is in range
        catagory = get_input(catagories)
        
        # Choose Program
        clear_screen()
        
        print("Choose a program: \n")

        programs = None
        match (catagory):
            case 0:              
                programs = misc
            case 1:
                programs = utilities
            case 2:
                programs = games

        #show all programs options in catagory
        for i, option in enumerate(programs):
            print(f'{i+1}. {option.__name__}.py\n')
        

        #validate input is in range
        program = get_input(programs)

        if (program == len(programs)):
            continue

        clear_screen()

        programs[program]()

        return

def get_input(options, back=False):
    choice = -1
    while choice > len(options) or choice < 0:
        try:
            choice = int(input(f'(1-{len(options)}): ')) - 1
            if back:
                return 

        except ValueError:
            continue
    
    
    return choice
        
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == "__main__":
    main()