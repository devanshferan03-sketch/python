line = 1
with open("log.html") as f :
   lines = f.readlines()
lineno = 1
for line in lines :
   
    if("python" in line):
      print(f"Yes Python is present .line no :{lineno} ")
      break    
    lineno += 1
else:
     print("No python is not Present")
    # this for in which line Python is present in log.html
    
    