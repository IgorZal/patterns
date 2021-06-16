from abc import ABC, abstractmethod

class Picture:
    
    def __init__(self,genre):
        self.genre=genre
        self.canvas=None
        self.frame=None
    
    def spec(self):
        print(f"Picture:{self.genre},{self.canvas},{self.frame}")

                      
class Canvas:
    paint1="oil"
    paint2="aquarelle"


class Frame:
    size1="40x50"
    size2="60x90"
    material1="wood"
    material2="plastic"


class AbstractArtist(ABC):
    
    @abstractmethod
    def draw_image(self):
        pass

    @abstractmethod
    def install_frame(self):
        pass

    
class LandscapeArtist(AbstractArtist):
    
    def __init__(self):
        self.picture=Picture("landscape")

    def draw_image(self):
        self.picture.canvas=Canvas.paint2

    def install_frame(self):
        self.picture.frame=[Frame.size2,Frame.material1]

    def finish(self):
        return self.picture
    
        
class PortraitArtist(AbstractArtist):
    
    def __init__(self):
        self.picture=Picture("portrait")

    def draw_image(self):
        self.picture.canvas=Canvas.paint1

    def install_frame(self):
        self.picture.frame=[Frame.size1,Frame.material2]

    def finish(self):
        return self.picture


class ArtDealer:
    def __init__(self):
        self.artist=None

    def set_artist(self,artist):
        self.artist=artist

    def process(self):
        self.artist.draw_image()
        self.artist.install_frame()
        

def func():
    dilok=ArtDealer()
    maslov=PortraitArtist()
    dilok.set_artist(maslov)
    dilok.process()
    x=maslov.finish()
    x.spec()
        
    
func()    
