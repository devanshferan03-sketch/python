class calculator:
    def __init__(self , n):
        self.n = n
    def square(self):
        print(f"The square is : {self.n*self.n}")
    def cube(self):
        print(f"The cube is : {self.n *self.n*self.n}")
    def squareroot(self):
        print(f"The squareroot is : {self.n**0.5}")
    @staticmethod
    def hello():
        print("Hello There !")
num = int(input("enter a number:"))

calculator= calculator(num)
calculator.hello()
calculator.square()
calculator.cube()
calculator.squareroot()