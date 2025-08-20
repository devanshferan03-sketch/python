class Employee:
    
    langauge = "python" #this is a class attribute      
    salary = 5000000
    def getInfo(self):
        print(f"The langauge is {self.langauge}. The salary is {self.salary}")
        @staticmethod
        def greet():#Here @staticmethod means it doesn't required any object like self if we don't use staticmethod then it  required 
            #object and it will be written as #def greet(self) so we direst write@staticmethid 
            print("Good Morning")
         
harry = Employee()
harry.langauge= "java" # This is an instance attribute

harry.getInfo()
Employee.getInfo(harry)#This and harry.getInfo() same 