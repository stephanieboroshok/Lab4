# Create function that takes 3 integers and returns the greatest

def largestInt (num1, num2, num3):
    if ((num1 > num2) and (num1 > num3)):
        print('The largest integer is num1:', num1)
    elif ((num2 > num1) and (num2 > num3)):
        print('The largest integer is num2:', num2)
    if ((num3 > num1) and (num3 > num2)):
        print('The largest integer is num3:', num3)
    else:
        pass
num1 = int(input('Enter a number:'))
num2 = int(input('Enter a number:'))
num3 = int(input('Enter a number:'))

print (largestInt(num1, num2, num3))