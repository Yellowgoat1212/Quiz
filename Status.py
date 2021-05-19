
#Ask if they are ready to take the quiz multipe choice 
status = input("Are you ready to take the quiz enter Yes or No :{}?:  \na. Yes \nb. No \n=>")

# what if the the user is not ready
if status == 'No' or status == 'no' or status == 'n' or status == 'N' or status == 'Nah' or status == 'nah' :
   print("See you next time.")
# ]
elif status == 'Maybe' or status == 'maybe' :
     print("Please enter Yes/No")
     
# what if the user is ready?
if status == 'Yes' or status == 'yes' or status == 'y' or status == 'Y' or status == 'Ye' or status == 'ye' or status == 'A' or status == 'a':
    print("Welcome to the quiz.")
