#tuple is immutable just like string 
tup = ( 12,23,45,6,78,9)
print(type(tup))
print(tup[0])
print(tup[3])

tup = () # tuple can be empty
print(tup)
print(type(tup))

#slicing in tuple

tup = (1,2,3,4)
print(tup[1:3])

#methods in tuples

tup = (1,3,8,2,4,5)
tup.index(2) #return index if first occurrence 
print(tup.index(2)) # here 2 is element and output will beindex means 3
tup.count(2) # count how many time 2 element appears
print(tup.count(2))

