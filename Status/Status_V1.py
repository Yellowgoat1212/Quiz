#Ask if they are ready to take the quiz
status = input("Are you ready to take the quiz :{}?:  \na. Yes \nb. No \n=>")

# what if the the user is not ready
if status == 'No' or status == 'no' or status == 'n' or status == 'N' :
    print("See you next time.")
# what if the user is ready?
if status == 'Yes' or status == 'yes' or status == 'y' or status == 'Y' :
    print("Welcome to the quiz.")
