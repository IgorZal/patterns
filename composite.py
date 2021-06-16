from abc import ABC, abstractmethod

class Title(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def draw(self):
        pass
    

class Text(Title):

    def __init__(self,txt="Some Text"):
        self.txt=txt

    def draw(self):
        print(self.txt,end='')


class Background(Title):

    def __init__(self,color="white"):
        self.color=color

    def draw(self):
        print(f'[{self.color}]')

 
class Header(Title):

    def __init__(self):
        self.component=[]
 
    def draw(self):
        for obj in self.component:
            obj.draw()
 
    def add(self, obj):
        if isinstance(obj, Title) and not obj in self.component:
            self.component.append(obj)
 
    def remove(self, obj):
        index = self._children.index(obj)
        del self._children[index]
 
 
h1=Header()
h1.add(Text())
h1.add(Background())
h1.draw()

# Изображение
# Линия
# Прямоугольник
# Текст