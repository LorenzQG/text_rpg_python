import sys
import os

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

def clear():
    os.system("clear")

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

    choice = input("# ")

    match choice:
        case "1":
            warrior = Warrior()
            os.system("clear")
            showClass(warrior)

            classChoice = input("Do you want to be a Warrior? (y/n) ")

            if classChoice.lower() == "y":
                os.system("clear")
                playerClasse = warrior
                player = Player(playerName, warrior, playerRace)
            elif classChoice.lower() == "n":
                os.system("clear")
                classMenu()

        case "2":
            print("Mage")
        case "3":
            print("Archer")
        case "4":
            print("Thief")
        case "5":
            print("Return")
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
    os.system("clear")
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
            os.system("clear")
            showRace(human)
            receChoice = input("Do you want to be a Human? (y/n) ")

            if receChoice.lower() == "y":
                os.system("clear")
                playerRace = human
                classMenu(playerRace)
            elif receChoice.lower() == "n":
                os.system("clear")
                raceMenu()

        case "2":
            elf = Elf()
            os.system("clear")
            showRace(elf)
            receChoice = input("Do you want to be a Elf? (y/n) ")

            if receChoice.lower() == "y":
                os.system("clear")
                playerRace = elf
                classMenu(playerRace)
            elif receChoice.lower() == "n":
                os.system("clear")
                raceMenu()

        case "3":
            dwarf = Dwarf()
            os.system("clear")
            showRace(dwarf)
            receChoice = input("Do you want to be a Dwarf? (y/n) ")

            if receChoice.lower() == "y":
                os.system("clear")
                playerRace = dwarf
                classMenu(playerRace)
            elif receChoice.lower() == "n":
                os.system("clear")
                raceMenu()
            
        case "4":
            orc = Orc()
            os.system("clear")
            showRace(orc)
            receChoice = input("Do you want to be a Orc? (y/n) ")
            
            if receChoice.lower() == "y":
                os.system("clear")
                playerRace = orc
                classMenu(playerRace)
            elif receChoice.lower() == "n":
                os.system("clear")
                raceMenu()

        case "5":
            os.system("clear")
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
                os.system("clear")
                print("Load Game")
            case "3":
                print("About")
            case "4":
                print("Bye Bye")
                menu = False
                running = False
            case _:
                print("Invalid choice")

    while play:
        print("Play")
        
  
      


    
    