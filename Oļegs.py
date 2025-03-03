class Person:
    def __init__(self, name, surname,  age, height):
        self.height = height
        self.name = name
        self.surname = surname
        self.age = age
        
    def getName(self) -> str:
        return self.name
    
    def getSurname(self) -> str:
        return self.Surname
    
    def getAge(self) -> str:
        return self.age
    
    def getHeighr(self) -> float:
        return self.height
    
    def greet(self):
        print(f"Hello{self.name}")
        print(f"I am {self.age} y.o.")
        
    def __str__(self):
        return f"{self.name} {self.surname} {self.age} {self.height}"
    
person1 = Person("Bob1", "Who", 88, 1.30)
person2 = Person("Bob2", "Who", 16, 1.60)
person3 = Person("Bob3", "Who", 20, 1.95)

personList = [person1, person2, person3]


for i in range(0, len(personList)):
    if personList[i].getAge() >= 18:
        print("Atļauts ienākt")
        print(f"Sveiki, {personList[i].getName()}!")
    else:
        print("Nav atļauts ienākt")



