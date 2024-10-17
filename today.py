class employee :
    def __init__(self,name,salary,project):
        self.name=name 
        self.salary=salary
        self.project=project
        
    def show(self):
        print("Name:", self.name, 'Salary:', self.salary)
        
    def work(self):
        print(self.name,'is working on',self.project)
        

emp=employee('Jessa',8000,'NLP')
emp1=employee('Sharon',4000,'AI')
emp2=employee('Kevin',10000,'CSK')

emp.show()
emp.work()
emp1.show()
emp1.work()
emp2.show()
emp2.work()
    
    