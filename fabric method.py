class SeaTransport:
    
    feature=None
    def show_feature(self):
        return self.feature
    

class Yacht(SeaTransport):
    
    feature="sail"
    

class Battleship(SeaTransport):
    
    feature="Big gun"
    
    
class FishingBoat(SeaTransport):
    
    feature="rod"
    

class TransportFactory():
    
    catalog={}
    def create_transport(self,type_):
        return self.catalog[type_]()
    
            
class SeaTranportFactory(TransportFactory):
    catalog={"yacht_type":Yacht,"battle_type":Battleship,"fishing_type":FishingBoat}   



app=SeaTranportFactory()
print(app.create_transport("fishing_type").show_feature())

