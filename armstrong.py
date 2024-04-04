upper = int(input("Enter the upper limit: "))
lower = int(input("Enter the lower limit: "))

def armstrong_():
    found = False
    for num in range(lower, upper + 1):
        sum = 0
        order = len(str(num))
        temp = num
        while temp > 0:
            digit = temp % 10
            sum += digit ** order
            temp //= 10
        if num == sum:
            found = True
            print(num)
    if not found:
        print("No Armstrong numbers found in the specified range.")

if upper <= lower:
    print("Error due to the higher value of lower than upper")
else:
    armstrong_()
