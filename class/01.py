# Class

class GameCharacter :
    
    # constructor
    # self 代表我们在搓次角色
    def __init__(self, name, hp, mana):
        self.name = name
        self.hp = hp
        self.mana = mana

    # method
    def sizeUp(self):
        self.hp = self.hp * 1.5
        return self.hp

    def manaUp(self):
        self.mana = self.mana * 2
        return self.mana

    def items(self):
        self.hp = 50 + self.sizeUp()
        self.mana = 50 + self.manaUp()


player1 = GameCharacter('sungjinwoo', 100, 200)
player1.sizeUp()
print(player1.hp)

print('after item')

player1.items()
print(player1.hp)
print(player1.mana)