friends = ["Apple", "Orange",5 ,345.06 , False, "Aakash" , "Rohan"]
print(friends)
friends.append("harry") # here append means add harry at last of list

print(friends)#here as we knw list is mutable so here list is change 
#but in string we can't change it
l1 = [ 1,34,55,33,23]
l1.sort()#.sort means l1 is is make in assending order
print(l1)
l1.reverse() #here list will be written in reverse like [23,33.....]

print(l1)
l1.insert(3,99) #here if we want insert or put any number at list at specific 
#index we use insert(index,number you put)  here at index 3 we put number 99
print(l1)
l1.pop(3)# so here pop(3) means the value at index 3 will pop out means deleted
print(l1)
#print(l1.pop(3))#and if we write print(l1.pop(3)) so here only 3^rd index will be written 
l1.remove(23) # it will remove 23 from the list
print(l1)

 