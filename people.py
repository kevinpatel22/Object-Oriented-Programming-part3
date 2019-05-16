class Person:

    def __init__(self, name):
        self.name = name
    
    def greeting(self):
        print(f"Hi, my name is {self.name}")

class Student(Person):

    def learn(self):
        print('I get it!')

class Instructor(Person):

    def teach(self):
        print('An object is an instance of a class')
    
nadia = Instructor('Nadia')
nadia.greeting()
nadia.teach()
print()
chris = Student('Chris')
chris.greeting()
chris.learn()

# chris.teach()
#Teach method won't work on student instance beacuse there is no relation between student and teacher itself. 
# Both are independent children of Person parent