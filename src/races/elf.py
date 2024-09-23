from races.race import Race 

class Elf(Race):
    def __init__(self):
        super().__init__("Elf", 80, 40, 10, 10, "Elves are a long-lived")
        