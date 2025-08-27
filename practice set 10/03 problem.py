class Demo:
    a = 4
    
o = Demo()
print(o.a)#print class attribute because instance attribute is not presnt
o.a = 0#here instance attribute is set
print(o.a) #print instance attribute because instance attribute is present
print(Demo.a) #print the class attribute