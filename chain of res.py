from abc import ABC, abstractmethod

class AbstarctHandler(ABC):
    
    @abstractmethod
    def handle(self, fname):
        pass
 

class DocHandler(AbstarctHandler):

    def handle(self, fname):
        if fname.split('.')[1]=='doc':
            return 'Word Document'


class XlsxHandler(AbstarctHandler):
    
    def handle(self, fname):
        if fname.split('.')[1]=='elsx':
            return 'Exel Document'
 
 
class File:
    def __init__(self):
        self._handlers=[]
 
    def add_handler(self, h):
        self._handlers.append(h)
 
    def open(self, fname):
        for h in self._handlers:
            response=h.handle(fname)
            if response:
                print(f'{response} open')
                break
        else:
            print("Unknown format")
 
 
file1 = File()
file1.add_handler(DocHandler())
file1.add_handler(XlsxHandler())
file1.open('yandex.ru') 
file1.open('mytable.elsx') 
