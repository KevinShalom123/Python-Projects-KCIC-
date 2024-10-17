class  Student:
    def __init__(self, name, department, age, year, nationality):
        self.name = name
        self.department = department
        self.age = age
        self.year = year
        self.nationality = nationality
    
    def show(self):
        print("Name:", self.name, "Department:", self.department, "Age:", self.age, "Year:", self.year)
    
    def work(self):
        print(self.name, "is from", self.nationality)

# Creating 5 employees
student1 = Student("Jessa", "Software Engineer", "USA", 800, "NLP")
student2 = Student("John", "Data Scientist", "Canada", 900, "Machine Learning")
student3 = Student("Alice", "Project Manager", "UK", 1200, "Project Management")
student4 = Student("Bob", "QA Engineer", "Australia", 850, "Quality Assurance")
student5 = Student("Eva", "UX Designer", "Germany", 1000, "User Experience")

# Showing information and work for each employee
student1.show()
student1.work()

student2.show()
student2.work()

student3.show()
student3.work()

student4.show()
student.work()

student5.show()
em5.work()
