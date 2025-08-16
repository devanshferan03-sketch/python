#nested dictionaries

student = {
    "names" : "devansh",
    "subjects" : {
        "phy" : 97,
        "maths" : 99
    }
}

print(student["subjects"]["phy"])

 
#dictionary methods
#myDict.key
print(student.keys())

print(list(student.keys()))
print(len(student))
print(len(list(student.keys())))

#mydic.values() #retuen all value

print(student.values())
print(list(student.values()))

#mydic.items() #returns all(key,val) pair as tuples
print(student.items())
print(list(student.items()))
pairs = list(student.items())
print(pairs[0])
#mydic.get("key") #return key according to value
print(student.get("names"))  
print(student["names"])

