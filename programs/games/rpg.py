import sys, os
from time import sleep
from math import ceil
from random import choice, choices, randint

def rpg():
    os.system('cls' if os.name == 'nt' else 'clear')

    global player
    player = Player(input('Username: '), get_multiplier(init(['Easy', 'Normal', 'Hard', 'Very Hard'])))

    turn()


def turn():

    if player.health <= 0:
        if died() == False:
            respawn()
        else:
            sys.exit(0)

    event = player_input(player, ['Wander', 'Areas', 'Potions', 'Settings'], 'Events:')
    
    match event:
        case 1:
            wander(player)
        case 2:
            travel(player)
        case 3:
            potions(player)
        case 4:
            settings()

    return turn()


def died():
    return player_input(player, ['Continue?', 'Quit.'], 'You died...') - 1

def respawn():
    player.level = 1
    player.exp_needed = 20
    player.health = 100
    player.maxHealth = 100
    player.defense = 0
    player.damage = 5
    player.speed = 3
    player.gold = 0
    player.area_multiplier = 1

def get_multiplier(difficulty):
    return round(0.33 + int(difficulty) / 3, 2)


def settings():
    choice = player_input(player, ['Cheats', 'Quit', 'Back'], 'Settings:')

    match choice:
        case 1:
            cheats()
        case 2:
            print()
            sys.exit(0)


def cheats():
    choice = player_input(player, ['Change Difficulty'], 'Cheats:')
    match choice:
        case 1:
            player.multiplier = get_multiplier(player_input(player, ('Easy', 'Normal', 'Hard', 'Very Hard'), 'Change Difficulty:'))

class Player():
    def __init__(self, name, multiplier):
        self._name = name
        self.level = 1
        self.exp_needed = 20
        self.health = 100
        self.maxHealth = 100
        self.defense = 0
        self.damage = 5
        self.speed = 3
        self.gold = 0
        self.multiplier = multiplier
        self.area_multiplier = 1

    def takeDamage(self, amount, message):
        if (amount - self.defense) <= 0:
            #! blocked all damage
            print(message)
            sleep(0.75)
            print(f'You blocked all of the damage.')
        else:
            #! remove health
            if self.health - (amount - self.defense) > 0:
                self.health -= (amount - self.defense)
            else:
                self.health = 0

            #! print message
            print(message)
            sleep(0.75)
            if 0 < amount - self.defense < amount:
                print(f"You blocked {self.defense} of the damage.")

        return

    def gainHealth(self, amount):
        if self.health + amount <= self.maxHealth:
            self.health += amount
        else:
            self.health = self.maxHealth
        return

    def gainExp(self, amount):
        sleep(0.5)
        if self.exp_needed <= amount:

            self.level += 1

            print(f'\nYou are now level {self.level}!')
            sleep(1)

            self.gold += self.level * 25
            print(f'Gained {25 * self.level} gold!')
            sleep(1)

            print(f'Health slightly restored!')
            sleep(1)

            self.maxHealth += 9 + self.level
            print(f'Max health increased to {self.maxHealth}!')
            sleep(1)

            self.gainHealth(ceil(self.maxHealth / 2))

            if self.level % 2 == 0:
                self.damage += ceil(3 + self.level / 3)
                print(f'Damage increased to {self.damage}!')
                sleep(1)
            
            if self.level % 3 == 0:
                self.speed += ceil(1 + self.level / 3)
                print(f'Speed increased to {self.speed}!')
                sleep(1)

            if self.level % 4 == 0:
                self.defense += ceil(2 + self.level / 3)
                print(f'Defense increased to {self.defense}!')
                sleep(1)
            
            check_area(self)

            self.exp_needed = round(10 + self.level * 8 * self.multiplier)
        else:
            self.exp_needed -= ceil(amount)
            print(f'\nYou gained {ceil(amount)} xp! {self.exp_needed} more to level up.')
            sleep(0.5)
        return

    @property
    def name(self):
        return self._name

def check_area(player):
    if player.level == 3:
        print('\nYou have unlocked the Underground!')
        sleep(1)
    if player.level == 5:
        print('\nYou have unlocked the Caves!')
        sleep(1)
    if player.level == 10:
        print('\nYou have unlocked the Icey Plains!')
        sleep(1)
    if player.level == 15:
        print('\nYou have unlocked the Volcano Plains!')
        sleep(1)
    if player.level == 20:
        print('\nYou have unlocked the Underworld!')
        sleep(1)
    if player.level == 25:
        print('\nYou have unlocked the Final Destination!')
        sleep(1)
    return

import os

def init(options):

    os.system('cls' if os.name == 'nt' else 'clear')
    print('Difficulty:\n')
    for i, option in enumerate(options):
        print(f'{i+1}. {option}\n')

    choice = 0
    while choice > len(options) or choice < 1:
        try:
            choice = int(input(f'(1-{len(options)}): '))
        except ValueError:
            continue

    return choice

def player_input(player, options, message=None):

    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'\n{player.name} - Level: {player.level}; Health: {player.health}/{player.maxHealth}; Defense: {player.defense}; Damage: {player.damage}; Speed: {player.speed} Gold: {player.gold}')
    
    if message:
        print(f'\n{message}\n')

    for i, option in enumerate(options):
        print(f'{i+1}. {option}\n')

    choice = 0
    while choice > len(options) or choice < 1:
        try:
            choice = int(input(f'(1-{len(options)}): '))
        except ValueError:
            continue

    return choice

def potions(player):

    global current_player
    current_player = player

    choice = player_input(current_player, ['Restoration Potion', 'Health Potion', 'Speed Potion', 'Battle Potion', 'Shield Potion', 'Exp Potion', 'Bong', 'Back'], 'Potions:')-1

    match choice:
        case 0:
            confirm_potion('Restoration Potion', 'Heals your health by 50 (Used Instantly)', 150)
        case 1:
            confirm_potion('Health Potion', 'Increases you Max Health by 10 (Used Instantly)', round(40 + current_player.maxHealth - 100))
        case 2:
            confirm_potion('Speed Potion', 'Increases your speed by 3 (Used Instantly)', round(75 + current_player.speed * 25))
        case 3:
            confirm_potion('Battle Potion', 'Increases your damage by 4 (Used Instantly)', round(current_player.damage * 12.5))
        case 4:
            confirm_potion('Shield Potion', 'Increases your defense by 3 (used Instantly)',round(100 + current_player.defense * 25))
        case 5:
            confirm_potion('Exp Potion', 'Gives you by 50 percent of your needed exp (Used Instantly)', round(200 + 25 * current_player.level))
        case 6:
            confirm_potion('Bong', 'Warning, this may have undesirable effects (Used Instantly)', 500)
        case 7:
            return

    return

def confirm_potion(name, description, cost):

    choice = player_input(current_player, ['Buy', 'Back'], f'{name}: {description}: {cost} gold.')

    match choice:
        case 1:
            if current_player.gold >= cost:
                current_player.gold -= cost
                if name == 'Exp Potion':
                    print(f'\nYou have bought a {name}.')
                else:
                    print(f'\nYou have bought a {name}.\n')
                sleep(1)
                match name:
                    case 'Health Potion':
                        current_player.maxHealth += 10
                        print(f'Gained 10 Max Health')
                        sleep(2)
                    case 'Restoration Potion':
                        current_player.gainHealth(50)
                        print(f'Gained 50 health!')
                        sleep(2)
                    case 'Exp Potion':
                        current_player.gainExp(current_player.exp_needed / 2)
                        sleep(2)
                    case 'Battle Potion':
                        current_player.damage += 4
                        print(f'Gained 4 damage!')
                        sleep(2)
                    case 'Speed Potion':
                        current_player.speed += 3
                        print(f'Gained 3 speed!')
                        sleep(2)
                    case 'Shield Potion':
                        current_player.defense += 3
                        print(f'Gained 3 Defense!')
                        sleep(2)
                    case 'Bong':
                        randMaxHealth = randint(-20, 40)
                        if randMaxHealth > 0:
                            current_player.maxHealth += randMaxHealth
                            print(f'Max Health increased by {randMaxHealth}!')
                        else:
                            if current_player.maxHealth + randMaxHealth > 0:
                                current_player.maxHealth += randMaxHealth
                            else:
                                current_player.maxHealth = 1
                            print(f'Lost {-randMaxHealth} Max Health.')
                        sleep(1)

                        randHealth = randint(-20, 40)
                        if randHealth > 0:
                            current_player.gainHealth(randHealth)
                            print(f'Restored {randHealth} health!')
                        else:
                            current_player.health += randHealth
                            print(f'Lost {-randHealth} health.')
                        sleep(1)
                        
                        randDamage = randint(-8, 15)
                        if randDamage > 0:
                            current_player.damage += randDamage
                            print(f'Damage increased by {randDamage}!')
                        else:
                            if current_player.damage + randDamage > 0:
                                current_player.damage += randDamage
                            else:
                                current_player.damage = 1
                            print(f'Lost {-randDamage} damage.')
                        sleep(1)
                        
                        randSpeed = randint(-4, 8)
                        if randSpeed > 0:
                            current_player.speed += randSpeed
                            print(f'Speed increased by {randSpeed}!')
                        else:
                            if current_player.speed + randSpeed > 0:
                                current_player.speed += randSpeed
                            else:
                                current_player.speed = 1
                            print(f'Lost {-randSpeed} speed.')
                        sleep(1)

                        randDefense = randint(-3, 5)
                        if randDefense > 0:
                            current_player.defense += randDefense
                            print(f'Defense increased by {randDefense}!')
                        else:
                            if current_player.defense + randDefense > 0:
                                current_player.defense += randDefense
                            else:
                                current_player.defense = 0
                            print(f'Lost {-randDefense} defense.')
                        sleep(1)

                        randGold = randint(-250, 500)
                        if randGold > 0:
                            current_player.gold += randGold
                            print(f'Gained {randGold} extra gold!')
                        else:
                            if current_player.gold + randGold > 0:
                                current_player.gold += randGold
                            else:
                                current_player.gold = 0
                            print(f'Lost {-randGold} extra gold.')
                        sleep(3)
                        

            else:
                print(f'\nYou need {cost - current_player.gold} more gold.')
                sleep(2)

    return potions(current_player)

def travel(player):
    area = player_input(player, ['Grasslands (Level 1)', 'Underground (Level 3)', 
                                'Caves (Level 5)', 'Icey Plains (Level 10)', 
                                'Volcano Fields (Level 15)', 'Underworld (Level 20)', 
                                'Final Destination (Level 25)', 'Back'], 'Areas:')

    global current_player
    current_player = player

    match area:
        case 1:
            change_area(1, 'Grasslands', 1)
        case 2:
            change_area(3, 'Underground', 2)
        case 3:
            change_area(5, 'Caves', 4)
        case 4:
            change_area(10, 'Icey Plains', 7)
        case 5:
            change_area(15, 'Volcano Fields', 11)
        case 6:
            change_area(20, 'Underworld', 16)
        case 7:
            change_area(25, 'Final Destination', 22)
    
def change_area(level, name, multiplier):
    if current_player.area_multiplier == multiplier:
        print('\nYou are already in this area.')

    elif current_player.level >= level:
        print(f'\nYou have entered the {name}. Good luck!')
        current_player.area_multiplier = multiplier

    else:
        print('\nYou need higher level to enter this area.')

    sleep(2)
    return travel(current_player)


def wander(player):
    rand = choices(range(0, 5), weights=(15, 10, 10, 10, 45))[0]

    global current_player
    current_player = player

    match rand:
        case 0:
            gold()
        case 1:
            trapped()
        case 2:
            health()
        case 3:
            place()
        case 4:
            battle(round(randint(2, round(3 + current_player.area_multiplier / 4 * player.multiplier))))


def battle(numEnemies):
    enemies = {}
    for i in range(numEnemies):
        
        enemyLevel = abs(round(randint(current_player.area_multiplier * 3 - 3, current_player.area_multiplier * 3 + 3) * current_player.multiplier))
        if enemyLevel == 0:
            enemyLevel = 1

        health = abs(round(randint(ceil(4 * enemyLevel - 10), ceil(4 * enemyLevel + 10))))
        if health == 0:
            health = 1
        
        damage = abs(round(randint(ceil(2 * enemyLevel - 10), ceil(2 * enemyLevel + 10))))
        if damage == 0:
            damage = 1

        enemies[i] = {
        "name": f'{enemy_names()}',
        "level": enemyLevel,
        "health": health,
        "damage": damage,
        "dead": False
        }

    print(f'\nYou encountered {numEnemies} enemies. Get ready for battle!')
    sleep(1)

    avgLevel = 0
    for i in range(len(enemies)):
        avgLevel += enemies[i]["level"]
    avgLevel /= numEnemies
 
    if current_player.speed < avgLevel:
        print('\nThe enemies have a faster speed than you and attack first.\n', end='')
        turn = False
    else:
        print('You have a faster speed than the enemies and go first!\n')
        turn = True
    sleep(2)
    
    while current_player.health > 0 and check_dead(enemies) == False:       
        if turn == True:
            s = '\nEnemies:\n\n'
            for i in range(len(enemies)):
                if enemies[i]["health"] > 0:
                    s += f'{enemies[i]["name"]} - Level: {enemies[i]["level"]}; Health: {enemies[i]["health"]}; Damage: {enemies[i]["damage"]}\n\n'
                
            choice = player_input(current_player, ['Attack', 'Potions', 'Run'], f'{s}\nActions:')
            match choice:
                case 1:
                    print()
                    for i in range(len(enemies)):
                        enemies[i]["health"] -= current_player.damage
                        if enemies[i]["health"] <= 0 and enemies[i]["dead"] == False:
                            print(f'You killed the {enemies[i]["name"]}!')
                            sleep(1)
                            enemies[i]["dead"] = True
                        elif enemies[i]["dead"] == False:
                            print(f'You dealt {current_player.damage} damage to the {enemies[i]["name"]}.')
                            sleep(1)
                case 2:
                    potions(current_player)
                    continue
                case 3:
                    rand = randint(0, 1)
                    if rand == True:
                        print('\nYou successfully ran away!\n')
                        sleep(2)
                        return
                    else:
                        print('\nYou were unsuccessful when trying to run away.')
                        sleep(2)
        elif turn == False:
            global first
            first = True
            print()
            for i in range(len(enemies)):
                take_damage(enemies[i], first)
            sleep(1)
        turn = not turn

    if check_dead(enemies) == True:
        amount = ceil(randint(round(10 * current_player.area_multiplier), round(20 * current_player.area_multiplier)) / current_player.multiplier * numEnemies)
        current_player.gold += amount       
        print(f'\nThe enemies dropped {amount} gold!')
        sleep(0.5)
        current_player.gainExp(ceil(amount / 5))
        sleep(2)


def take_damage(enemy, first):
    if enemy["dead"] == False:
        if first == True:
            first = False
        else:
            print()
        current_player.takeDamage(enemy["damage"], f'{enemy["name"]} dealt {enemy["damage"]} damage to you.')
        sleep(1)


def enemy_names():
    match current_player.area_multiplier:
        case 1:
            return choice(['Slime', 'Chicken', 'Wanderer', 'Bunny'])
        case 2:
            return choice(['Bat', 'Bear', 'Spider', 'Wolf'])
        case 4:
            return choice(['Zombie', 'Skeleton', 'Vampire', 'Werewolf'])
        case 7:
            return choice(['Mammoth', 'Yeti', 'Krampus', 'Giant Wolf'])
        case 11:
            return choice(['Dragon', 'Pheonix', 'Ogre', 'Golem'])
        case 16:
            return choice(['Minotaur', 'Demon', 'Griffin', 'Centuar'])
        case 22:
            return choice(['Grim Reaper', 'Deathtaker', 'Hydra', 'Chimera'])


def check_dead(enemies):
    for i in range(len(enemies)):
        if enemies[i]["health"] > 0:
            return False
    return True


def gold():
    amount = ceil(randint(round(10 * current_player.area_multiplier), round(20 * current_player.area_multiplier)) / current_player.multiplier)
    current_player.gold += round(amount)
    print(f'\nYou wandered around and found {amount} gold!')
    sleep(0.5)
    current_player.gainExp(ceil(amount / 5))
    sleep(2)


def trapped():
    amount = round(randint(round(5 * current_player.area_multiplier), round(10 * current_player.area_multiplier)) * current_player.multiplier)
    current_player.takeDamage(amount, f'\nOh No! You fell into a trap and took {amount} damage.')
    sleep(2)


def health():
    amount = ceil(randint(round(10 * current_player.area_multiplier), round(20 * current_player.area_multiplier)) / current_player.multiplier) + current_player.level * 2
    current_player.gainHealth(amount)
    print(f'\nYou found a Nurse who healed your health by {amount}!')
    sleep(2)


def place():
    if player_input(current_player, ['Yes', 'No'], 'You found a cabin. Will you attempt to loot it?')-1 == False:
        sleep(0.5)
        numb = choices(range(0, 3), weights=(50, 30, 20))[0]
        match numb:
            case 0:
                amount = ceil(randint(round(15 * current_player.area_multiplier), round(30 * current_player.area_multiplier)) / current_player.multiplier)
                print(f'\nYou found {amount} gold!')
                sleep(0.5)
                current_player.gold += amount
                current_player.gainExp(ceil(amount / 5))
            case 1:
                print(f'\nYou found nothing...')
            case 2:
                amount = round(randint(round(7.5 * current_player.area_multiplier), round(15 * current_player.area_multiplier)) * current_player.multiplier)
                current_player.takeDamage(amount, f'\nYou were attacked and took {amount} damage.')
        sleep(2)