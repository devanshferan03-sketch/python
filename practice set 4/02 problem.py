marks = []
f1 = int(input("enter marks here :"))
marks.append(f1)
f2 = int(input("enter marks here :"))
marks.append(f2)
f3 = int(input("enter marks here :"))
marks.append(f3)
f4 = int(input("enter marks here :"))
marks.append(f4)
f5 = int(input("enter marks here :"))
marks.append(f5)
f6 = int(input("enter marks here :"))
marks.append(f6)
marks.sort() # as i do first without using int means dirstect input use kiya tha to sort 
# nahi hua because of ye string ki tarah behave karage
# #only first number he sort hua like 223 and 1223 to pahale 1223 a raha tha because first no 1 is small than 2 
# so we use int for inter now o/p will be coreect and sort like integer 
print(marks)
