#c/5 = (f-32)/9
#c =5 * (f-32)/9
def f_to_c(f):
    return 5 * (f-32)/9
f = int(input("Enter Temperarure in F"))
c = f_to_c(f)
print(f"{c } ° c")