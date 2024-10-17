class Employee:
    def __init__(self, name, designation, nationality, salary, project):
        self.name = name
        self.designation = designation
        self.nationality = nationality
        self.salary = salary
        self.project = project
    
    def show(self):
        print("Name:", self.name, "Designation:", self.designation, "Nationality:", self.nationality, "Salary:", self.salary)
    
    def work(self):
        print(self.name, "is working on", self.project)

# Creating 5 employees
employee1 = Employee("Jessa", "Software Engineer", "USA", 800, "NLP")
employee2 = Employee("John", "Data Scientist", "Canada", 900, "Machine Learning")
employee3 = Employee("Alice", "Project Manager", "UK", 1200, "Project Management")
employee4 = Employee("Bob", "QA Engineer", "Australia", 850, "Quality Assurance")
employee5 = Employee("Eva", "UX Designer", "Germany", 1000, "User Experience")

# Showing information and work for each employee
employee1.show()
employee1.work()

employee2.show()
employee2.work()

employee3.show()
employee3.work()

employee4.show()
employee4.work()

employee5.show()
employee5.work()
