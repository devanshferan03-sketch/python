a = ''' Dear <|Name|>,
You are selected
<|Date|> '''
print(a.replace("<|Name|>" , "Devansh").replace(  "<|Date|>" , "01/10/2027"))
#here fiest name is replace by devansh then i use .replace means in that name string replace date by 01/10/2027
print(a.replace("<|Name|>" , "Devansh")) #here i don't use .replace in same line so o/p will      Dear Devansh,
#You are selected
#<|Date|>             like date folder is same 
# # and this techniques is called chaining of .replace 
              