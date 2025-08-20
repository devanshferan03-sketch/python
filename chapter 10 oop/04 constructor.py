class Employee:
    
    langauge = "python" #this is a class attribute      
    salary = 5000000
    def __init__(self , name, salary,langauge):
        #this is dunder method it is automatically call  as in 03 self at last we call getinfo bt here we don't need to call saperately it call automatically it is dunder method
        self.name = name 
        self.salary= salary
        self.langauge = langauge
        print("I am Creating an Object")
    def getInfo(self):
        print(f"The langauge is {self.langauge}. The salary is {self.salary}")
        @staticmethod
        def greet():
             print("Good Morning")
            
harry = Employee("harrry" ,10000000,"AIML")
#harry.name = "Harry"
print(harry.name , harry.salary ,harry.langauge) 