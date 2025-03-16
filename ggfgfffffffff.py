class Player():
    def __init__(self, a, b, c, d, f):
        self.name = a
        self.clothes = b
        self.health = c
        self.weapon = d
        self.impact  = f

    def print_info(self):
        print("Имя игрока:", self.name)
        print("Одежда игрока:", self.clothes)
        print("Здоровье игрока:", self.health)
        print("Оружие игрока:", self.weapon)
        print("Сила удара:", self.impact)

andrey = Player("Andrey", "Сoat", "100", "The shotgun", "Impact force")
andrey.print_info()