class programmer :
    company = "Microsoft"
    def __init__(self,name,salary,pin):
        self.name = name
        self.salary = salary
        self.pin = pin
        
p = programmer("Harry" , 5000000, 444803)
print(p.company,p.name ,p.salary , p.pin )  