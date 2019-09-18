# Create program that allows user to create username and PW then log in using that
# Prompt user to set UN and PW and save variables
# Create passwordChecker that takes a UN attempt and PW attempt as parameters and checks to see if they match
# Prompt user to enter UN and PW, use passwordChecker to confirm correct login info

username = str(input('Create a new username:'))
password = str(input('Create a new password:'))

def passwordChecker(usernameAttempt,passwordAttempt):
    if ((usernameAttempt == username) and (passwordAttempt == password)):
        print ('Login successful!')
    else:
        print ('Login failed.')

usernameAttempt = str(input('Enter your username:'))
passwordAttempt = str(input('Enter your password:'))

print (passwordChecker(usernameAttempt,passwordAttempt))
