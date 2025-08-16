n = int(input("enter a number :"))
product = 1
for i in range(1,n+1):#here range n tak jayega n+1-1 = n 

    product = product * i#here 1 is multiplied first 1,2,3,...upto n
    
print(f"the factorial of {n} is {product}")