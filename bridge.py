class TaskApp():
    
    def __init__(self):
        self.actual_problems=[]

    def show_problems(self):
        return 'current:',*self.actual_problems
    
       
class TaskControll():
    
    def __init__(self,app):
        self.app=app

    def add_task(self,task):
        self.app.actual_problems.append(task)

    def dell_task(self,task):
        self.app.actual_problems.remove(task)    
        
    def show_problems(self):
        print(*self.app.show_problems())

   
        


def func():
    x1=TaskApp()
    y1=TaskControll(x1)
    y1.add_task('make buy')
    y1.show_problems()
    y1.dell_task('make buy')
    y1.show_problems()


func()
