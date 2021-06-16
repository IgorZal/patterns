class Notepade():
    
    genre=['snake','camel']
    
    def __init__(self,text='',defaultstyle='snake'):
        self.text=text
        self.style=defaultstyle

    def translate(self,txt):
        if self.style=='snake':
            self.text=SnakeStrategy.transfer(txt)

        else:
            self.text=CamelStrategy.transfer(txt)

    def switch_style(self):
        ind=Notepade.genre.index(self.style)-1
        self.style=Notepade.genre[ind]
                   
    def show_text(self):
        print(self.text)
        

class SnakeStrategy():
    @staticmethod
    def transfer(txt):
        txt=txt.lower().replace(' ','_')
        return txt


class CamelStrategy():
    @staticmethod
    def transfer(txt):
        txt=txt.split(' ')
        txt_cap=list(map(lambda x:x.title(),txt))
        txt=''.join(txt_cap)
        return txt

user1=Notepade()
user1.translate('Some text')
user1.show_text()
user1.switch_style()
user1.translate('Some text')
user1.show_text()

