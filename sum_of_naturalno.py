num = 6

if num<0:
    print("Please enter posotive number")
else:
    sum = 0
    while num > 0:
        sum += num
        num -=1
    print("The num is:",sum)