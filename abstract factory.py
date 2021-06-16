from abc import ABC, abstractmethod

class AbstarctDepatment(ABC):
    
    @abstractmethod
    def teach_bachelor(self,name):
        pass
    @abstractmethod
    def teach_master(self,name):
        pass
    
    
class Engeneering(AbstarctDepatment):
    
    def teach_bachelor(self,name):
        return EngineerB(name,department="engeneering",degree="bachelor")

    def teach_master(self,name):
        return EngineerM(name,department="engeneering",degree="master")
    

class Philosphy(AbstarctDepatment):
    
    def teach_bachelor(self,name):
        return PhylosopherB(name,department="philosphy",degree="bachelor")

    def teach_master(self,name):
        return PhylosopherM(name,department="philosphy",degree="master")

       
class AbstractStudent(ABC):
    
    def __init__(self,name,department,degree):
        self.name=name
        self.department=department
        self.degree=degree
        
    def show_info(self):
        print(self.name,self.department,self.degree,sep='\n')
        

class EngineerB(AbstractStudent):
    pass

class EngineerM(AbstractStudent):
    pass

class PhylosopherB(AbstractStudent):
    pass

class PhylosopherM(AbstractStudent):
    pass  
    
xp=Engeneering()
student1=xp.teach_bachelor('luis suarez')
student1.show_info()
