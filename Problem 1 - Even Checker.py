# Create a function, isEven, that takes in an integer as an argument
# and returns true if the integer is even, false if odd

def isEven (number1):
    number1 = int(input('Enter a number:'))

number1 = int(input('Enter a number:'))
if (number1%2 == 0):
    # modulus operator (%) shows remainder after dividing by 2
    # if remainder = 0, then integer must be even
    print ('The integer is even.')
else:
    print ('The integer is odd.')