# Create function that takes 3 integers and returns the greatest

def largestInt (num1, num2, num3):
    # define function and parameters
    if ((num1 > num2) and (num1 > num3)):
        print('The largest integer is num1:', num1)
    elif ((num2 > num1) and (num2 > num3)):
        print('The largest integer is num2:', num2)
    if ((num3 > num1) and (num3 > num2)):
        print('The largest integer is num3:', num3)
    else:
        pass
    # comparing the numbers that are entered in

num1 = int(input('Enter a number:'))
num2 = int(input('Enter a number:'))
num3 = int(input('Enter a number:'))
# this is the first thing to run
# gathering the integers to use for the parameters in above funtion

print (largestInt(num1, num2, num3))
# call function to actually run and find the largest integer