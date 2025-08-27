arr = [ 12, 3,100,110,300, 45,52, 56]
largest = arr[0]
for num in arr:
    if(num > largest):
        largest= num
    
print(largest)
secondlargest = arr[0]
for num1 in arr:
    if(num1 >secondlargest and num1 != largest ):
        secondlargest = num1
print(secondlargest)

thirdlargest =arr[0]
for num2 in arr :
    if(num2 > thirdlargest and num2 != largest and num2 !=secondlargest):
        thirdlargest = num2
print(thirdlargest)
print(arr.sort(),arr)