import sys
import os
import time

#Classes import
from classDir.classe import Classe
from classDir.warrior import Warrior
from classDir.mage import Mage
from classDir.archer import Archer
from classDir.thief import Thief

#Races import
from races.human import Human
from races.elf import Elf
from races.dwarf import Dwarf
from races.orc import Orc

#Player import
from player import Player

running = True
menu = True
play = False
about = False

playerName = ""
player = None

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def drawLine():
    print("**===========_****_===========**")

def about():
    print("About")
    print("This is a simple text based game")
    print("Version: 0.1")
    print("Author: Lorenzo Q. Gonçalves")
    print("Github: https://github.com/LorenzQG")


#Show class function
def showClass(classe):
    drawLine()
    print(f"Name: {classe.name}")
    drawLine()

#Class menu function
def classMenu(playerRace):
    drawLine()
    print("Select a class")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer")
    print("4. Thief")
    print("5. Return")
    drawLine()
    
    global player
    choice = input("# ")

    match choice:
        case "1":
            warrior = Warrior()
            clear()
            showClass(warrior)

            classChoice = input("Do you want to be a Warrior? (y/n) ")

            if classChoice.lower() == "y":
                clear()
                playerClasse = warrior
                player = Player(playerName, warrior, playerRace)
            elif classChoice.lower() == "n":
                clear()
                classMenu()

        case "2":
            mage = Mage()
            clear()
            showClass(mage)

            classChoice = input("Do you want to be a Mage? (y/n) ")

            if classChoice.lower() == "y":
                clear()
                playerClasse = mage
                player = Player(playerName, mage, playerRace)
            elif classChoice.lower() == "n":
                clear()
                classMenu()

        case "3":
            archer = Archer()
            clear()
            showClass(archer)

            classChoice = input("Do you want to be a Archer? (y/n) ")

            if classChoice.lower() == "y":
                clear()
                playerClasse = archer
                player = Player(playerName, archer, playerRace)
            elif classChoice.lower() == "n":
                clear()
                classMenu()

        case "4":
            thief = Thief()
            clear()
            showClass(thief)

            classChoice = input("Do you want to be a Thief? (y/n) ")

            if classChoice.lower() == "y":
                clear()
                playerClasse = thief
                player = Player(playerName, thief, playerRace)
            elif classChoice.lower() == "n":
                clear()
                classMenu()

        case "5":
            clear()
            raceMenu()

        case _:
            print("Invalid choice")

#Show race function
def showRace(classe):
    drawLine()
    print(f"Name: {classe.name}")
    print(f"Health: {classe.health}")
    print(f"Mana: {classe.mana}")
    print(f"Attack: {classe.attack}")
    print(f"Defense: {classe.defense}")
    drawLine()
    print("History")
    print(f"{classe.history}")

#Race menu function
def raceMenu():
    main = False
    clear()
    drawLine()
    print("Select a race")
    print("1. Human")
    print("2. Elf")
    print("3. Dwarf")
    print("4. Orc")
    print("5. Return")
    drawLine()

    choice = input("# ")
    
    match choice:
        case "1":
            human = Human()
            clear()
            showRace(human)
            receChoice = input("Do you want to be a Human? (y/n) ")

            if receChoice.lower() == "y":
                clear()
                playerRace = human
                classMenu(playerRace)
            elif receChoice.lower() == "n":
                clear()
                raceMenu()

        case "2":
            elf = Elf()
            clear()
            showRace(elf)
            receChoice = input("Do you want to be a Elf? (y/n) ")

            if receChoice.lower() == "y":
                clear()
                playerRace = elf
                classMenu(playerRace)
            elif receChoice.lower() == "n":
                clear()
                raceMenu()

        case "3":
            dwarf = Dwarf()
            clear()
            showRace(dwarf)
            receChoice = input("Do you want to be a Dwarf? (y/n) ")

            if receChoice.lower() == "y":
                clear()
                playerRace = dwarf
                classMenu(playerRace)
            elif receChoice.lower() == "n":
                clear()
                raceMenu()
            
        case "4":
            orc = Orc()
            clear()
            showRace(orc)
            receChoice = input("Do you want to be a Orc? (y/n) ")
            
            if receChoice.lower() == "y":
                clear()
                playerRace = orc
                classMenu(playerRace)
            elif receChoice.lower() == "n":
                clear()
                raceMenu()

        case "5":
            clear()
            menu = True
            play = False
        case _:
            print("Invalid choice")

while running:
    clear()

    while menu:
        drawLine()
        print("||" + "*" * 11 + "_Menu_" + "*" * 11 + "||")
        print("|| 1. New Game                ||")
        print("|| 2. Load Game               ||")
        print("|| 3. About                   ||")
        print("|| 4. Quit                    ||")
        drawLine()

        choice = input("# ")

        match choice:
            case "1":
                playerName = input("Enter your name: ")
                raceMenu()
                menu = False
                play = True
            case "2":
                clear()
                print("Load Game")
            case "3":
                clear()
                about()
            case "4":
                print("Bye Bye")
                menu = False
                running = False
            case _:
                print("Invalid choice")

    while play:
        drawLine()
        print("Welcome to the world of Senachia")
        time.sleep(2)
        clear()
        print("You are a hero in the making")
        time.sleep(2)
        clear()
        print("You are in the city of Eldoria")
        time.sleep(2)
        clear()
        print("You are in the tavern")
        time.sleep(2)
        clear()
        print("1. Show stats")
        print("2. Inventory")
        print("3. Quests")
        print("4. Exit")
        print("5. Save game")

        choice = input("# ")


        match choice:
            case "1":
                clear()
                drawLine()
                player.stats()
                drawLine()
                input("Press enter to continue")
            case "2":
                print("Inventory")
            case "3":
                print("Quests")
            case "4":
                print("Bye Bye")
                play = False
                running = False
            case "5":
                print("save game")
                
            case _:
                print("Invalid choice")


        
  
      


    
    