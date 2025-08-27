from random import randint

class Train :
    def book(self , TrainNO, fro , to):
        print(f"Ticket is booked in train no :{TrainNO} From{fro} to{to}")
       
    def getstatus(self , TrainNo):
      print(f"train no :{TrainNo} is on time")  
    def getFare(self , TrainNo ,fro , to):
        print(f"Ticket fare in train no :{TrainNo} From{fro} to{to} is {randint(1,600)}")
      
      
      
#taking input from users
train_no = int(input("Enter The Train No :"))
fro =str(input("Enter the Departure station:"))
to = str(input("Enter the Destination Station:"))


myTrain = Train()
myTrain.book(train_no,fro,to)
myTrain.getstatus(train_no)
myTrain.getFare(train_no , fro , to)
      
      