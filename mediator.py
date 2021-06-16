class Realtor():
    
    def __init__(self):
        self.buyer=None
        self.seller=None
        self.discussion={}

    def add_seller(self,seller):
        self.seller=seller

    def add_buyer(self,buyer):
        self.buyer=buyer

    def comunication(self,header,text):
        self.discussion[header]=text
                     
    def make_deal(self):
        if self.discussion['answer']=='Yes':
            self.buyer.money-=self.discussion['proposal']
            self.seller.money+=self.discussion['proposal']
            print(self.discussion)
            print('apartment changed owner')

                                                  
class BaseClient():
    def __init__(self,realtor,money):
        self.money=money
        self.realtor=realtor
        

class Buyer(BaseClient):
    def request(self,value):
        if value<=self.money:
            self.realtor.comunication('proposal',value)
            

class Seller(BaseClient):
    def __init__(self,realtor,money,price):
        super().__init__(realtor,money)
        self.price=price

    def response(self):
        if self.realtor.discussion['proposal']>=self.price:
            self.realtor.comunication('answer','Yes')
        else:
            self.realtor.comunication('answer','No')
            

natalia=Realtor()
igor=Buyer(natalia,10)
jim=Seller(natalia,2,8)
natalia.add_buyer(igor)
natalia.add_seller(jim)
igor.request(9)
jim.response()
natalia.make_deal()


