f = open("poem.txt")
Content = f.read()
if("Twinkle" in Content):
    print("The word Twinkle is Present in the content")
else :
    print("the word Twinkle is not Present in content Content")
f.close()