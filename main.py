#ignore
import os

# import your functions here (example):

#    #folder  #file name        #function name
from programs.calculator import calculate
from programs.hello import hello

#add your imported function here:
programs = [hello, 
            calculate]

def main():
    #clear screen
    os.system('cls' if os.name == 'nt' else 'clear')

    print("Choose a program: \n")

    #show all program options
    for i, option in enumerate(programs):
        print(f'{i+1}. {option.__name__}.py\n')

    #validate input is in range
    choice = 0
    while choice > len(programs) or choice < 1:
        try:
            choice = int(input(f'(1-{len(programs)}): '))
        except ValueError:
            continue

    os.system('cls' if os.name == 'nt' else 'clear')
    
    #execute programs
    programs[choice-1]()

if __name__ == "__main__":
    main()