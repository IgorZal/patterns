import random

class Lottery():
    
    def __init__(self):
        self.players=[]
        self.win_number=None

    def add_player(self,player):
        self.players.append(player)

    def start_game(self):
        self.win_number=random.randint(1,10)
        
        for player in self.players:
            player.check_ticket(self)
            
        
class Player():
    
    def __init__(self,name):
        self.name=name
        self.ticket=random.randint(1,10)

    def check_ticket(self,lottery):
        if self.ticket==lottery.win_number:
            print(f'{self.name} - win')
        else:
            print(f'{self.name} - lost')


loto=Lottery()
p1=Player('andrea')
p2=Player('miguel')
p3=Player('abraham')
p4=Player('fabio')
loto.add_player(p1)
loto.add_player(p2)
loto.add_player(p3)
loto.add_player(p4)
loto.start_game()
