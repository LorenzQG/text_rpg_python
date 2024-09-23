from races.human import Human
from races.elf import Elf
from races.dwarf import Dwarf
from races.orc import Orc

from classDir.warrior import Warrior
from classDir.mage import Mage
from classDir.archer import Archer
from classDir.thief import Thief


class Player:
    def __init__(self, name, playerClass, playerRace):
        self.name = name
        self.playerClass = playerClass
        self.playerRace = playerRace
        self.health = self.playerRace.health * self.playerClass.multHp
        self.mana = self.playerRace.mana * self.playerClass.multMan
        self.attack = self.playerRace.attack * self.playerClass.multAtk
        self.defense = self.playerRace.defense * self.playerClass.multDef
        
        
    def stats(self):
         print(f"Name: {self.name}")
         print(f"Class: {self.playerClass.name}")
         print(f"Race: {self.playerRace.name}")
         print(f"Health: {self.health}")
         print(f"Mana: {self.mana}")
         print(f"Attack: {self.attack}")
         print(f"Defense: {self.defense}")
           
