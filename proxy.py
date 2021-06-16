class SeniorCashier():
    
    def __init__(self, client):
        self.client=client
        self.cash=self.client.cash

    def donation(self):
        print(f'sent {self.cash}')

    def exchange_money(self):
        print(f'IN:{self.cash} UA, OUT:{self.cash/25} USA')

        
class TraineeCashier():
    
    def __init__(self, client, mentor):
        self.client=client
        self.cash=self.client.cash
        self.mentor=mentor

    def donation(self):
        print('switch')
        self.mentor.donation()

    def exchange_money(self):
        if  self.cash<=1000:
            print(f'IN:{self.cash} UAH, OUT:{self.cash/25} USA')
            
        else:
            print('switch')
            self.mentor.exchange_money()

               
class Client():
    
    def __init__(self,cash):
        self.cash=cash


client1=Client(1200)
worker1=SeniorCashier(client1)
worker2=TraineeCashier(client1,worker1)
worker2.exchange_money()


