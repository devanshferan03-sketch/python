name = "harry"
print(len(name))
print(name.endswith("rry"))#here o/p is true cause string"harry" is end with rry
#if i put ("rrya") then its o/p will be false cause a is not present at end
print(name.startswith("h"))#same like endwith 
#here H is not consider if we write H it wiil false because in string small h is written
print(name.capitalize())#it will capitalize first character
print(name.count("r"))
print(name.find("r"))#find the word and written index of first occurance like here o/p is 2
print(name.replace("a","m"))# here a is replace by m
