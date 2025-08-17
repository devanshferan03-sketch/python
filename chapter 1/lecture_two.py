#string function 

#string end with function ("er.")  #return true and false 

str = "i am studyong with apna college"
print(str.endswith("ege"))


#capitalize function 
#str.capitalize
str = "i am studyong with apna college"
str = (str.capitalize())
print(str)


# replace function 
str = "i am studyong with apna college"
print(str.replace("o","a"))

#find function
# it search fpr a string means its find is thos word exist in my string or not 
# and if it is exist then in string where it is exist first time its stzrting index will appears
str = "i am studyong with apna college"
print(str.find("with"))

# count function
# word exist in string how many time it count

str = "i am studyong with apna college"
print(str.count("a")) 


# practice question


#wap to input user first name and print its length

int = input("enter your name ")
print("length of your name is", len(int))

#wap to find the occureance of '$'in a string.

str = "hi i am the $ and $ name"
print(str.count("$"))







#conditional statements 

#if-elif-else 
num = 1

if(num > 2):
    print("greater than 2")
if(num > 3):
    print("greater than 3")

else :
    print("this is wrong")


    #nesting means write if statement inside if statement means writing one statement in another statement 

age = 90

if(age >= 18):
    if(age >= 80):
        print("can not drive")
    else:
        print("can drive")


#let practice 

#wap to check number enter is  odd or even

num = int(input("enter number: ")) 
rem = num % 2

if(rem == 0):
    print("even")
else:
    print("odd")