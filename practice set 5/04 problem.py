s = set ()
s.add(20)
s.add(20.0)
s.add('20')
#length of s after this operations?
print(s)#here o/p is {'20' ,20} because 20.0 is floating number
# while comparing int & floating python comparing their values and its same in python 1 ==1.0 

print(len(s))
