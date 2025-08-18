f = open("file.txt")
print(f.read())
f.close()



# The same can be written using with satement like This
with open("file.txt") as f :
    print(f.read())
    # you don't have to explicitly colse the file 