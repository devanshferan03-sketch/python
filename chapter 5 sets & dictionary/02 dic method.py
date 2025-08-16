d = { } #empty dictionary
marks = {
    "harry" :100,
    "shubham" :56,
    "rohan" :23,
    0 :"harry"
}
print(marks.items()) # it gives items in dictionary means written list of key:value pair
#and that key: value pair are in tuple form
print(marks.keys()) # all keys will print
print(marks.values())# al values willprint
marks.update({"harry":99, "renuka": 100})
# update is uses here as dictionary is mutable so in written dictionay will be change and harry marks change and in dictioary renuka is also adding
#{'harry': 99, 'shubham': 56, 'rohan': 23, 0: 'harry', 'renuka': 100} this wiil be o/p

print(marks)
print(marks.get("harry"))
print(marks["harry"])
#at 16 we get value of harry and in 17 also we get value but what is the difference
#so difference is in 16 if i write harry2 which is not prisent then it o/p will be none 
# but in 17 for harry2 the o/p will be error
#pop 
#popitem


