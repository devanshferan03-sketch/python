class Employee:
    
    langauge = "python" #this is a class attribute      
    salary = 5000000
harry = Employee()
harry.langauge= "java" # This is an instance attribute
print(harry.salary , harry.langauge)
#here java is print as harry.langauge not python will print 
#because Note : it is instant attributes and instant attribute takes preference over class attributes for assign an retrival
#if we here comment out harry.langauge = java then python is written in out put because there will be no any instance attribute
