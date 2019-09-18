# Create a function, isEven, that takes in an integer as an argument
# and returns true if the integer is even, false if odd

def isEven (number1):
    #define function
    if (number1 % 2 == 0):
        # modulus operator (%) shows remainder after dividing by 2
        # if remainder = 0, then integer must be even
        print('The integer is even.')
    else:
        print('The integer is odd.')

number1 = int(input('Enter a number:'))
# this is the first thing to run
# collects input for number

print (isEven(number1))
# running the function
