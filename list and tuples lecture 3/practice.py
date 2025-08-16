#wap to ask the user to enter name sof their 3 fsvourite movies and store them in list
movies1 = input("a:")
movies2 = input("b:")
movies3 = input("c:")

movies = []
movies.append(movies1)
movies.append(movies2)
movies.append(movies3)
print(movies)

#wap to check if alist contains a palindrome of elements

list1 = [ 1,2,3,2,1]
copy = list1.copy()
reverse = copy.reverse()

if(copy == reverse):
   print("this  is a palindrome")