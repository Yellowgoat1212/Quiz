#asking users if they're ready for the quizr
def status():
    status = input("Are you ready to take the quiz :{}?:  \na. Yes \nb. No \n=>")

# what if the the user is not ready
    if status == 'No' or status == 'no' or status == 'n' or status == 'N' :
        print("See you next time.")
# what if the user is ready?
    elif status == 'Yes' or status == 'yes' or status == 'y' or status == 'Y' or status == 'Ye' or status == 'ye' or status == 'A' or status == 'a':
        print("Welcome to the quiz.")

status()

