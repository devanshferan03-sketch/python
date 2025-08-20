class Employee:
    
    langauge = "python" #this is a class attribute      
    salary = 5000000
harry = Employee()
harry.name = "Devansh" # This is an object attribute
print(harry.name ,harry.salary , harry.langauge)
rohan = Employee()
rohan.name = "Rohan"
print(rohan.name  ,rohan.salary , rohan.langauge)

#Here name is object attribute and salary and language are class
#attributes as they directly belong to the class 