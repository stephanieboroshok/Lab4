# Create program that allows user to create username and PW then log in using that
# Prompt user to set UN and PW and save variables
# Create passwordChecker that takes a UN attempt and PW attempt as parameters and checks to see if they match
# Prompt user to enter UN and PW, use passwordChecker to confirm correct login info

username = str(input('Create a new username:'))
password = str(input('Create a new password:'))
#user creates UN and PW here

def passwordChecker(usernameAttempt,passwordAttempt):
    #define function
    if ((usernameAttempt == username) and (passwordAttempt == password)):
        print ('Login successful!')
    else:
        print ('Login failed. Try again.')
    #check to see if UN and PW are correct

usernameAttempt = str(input('Enter your username:'))
passwordAttempt = str(input('Enter your password:'))
# user enters UN and PW

print (passwordChecker(usernameAttempt,passwordAttempt))
#call and run the function
