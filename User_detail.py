#This program will get user details such as name and age. 

#In this code i'll be defining the user_details function with one pameter 

def user_details(name):
    greet = name
    print("Hello",greet)

#In this code it'll accept lower case but won't accept invalid answers 
while True:
    name = input ("Enter your name : ")
    if name.isalpha():
        break
    print("Please enter character A-Z only")
print("Hey",name)


#this code is going to be similar to name but won't accept lower case and won't accept alphabet
while True:
    age = input ("Enter your age : ")
    if age.isnumeric():
        break
    print("Please enter integer/numbers only")


user_details(name)
print("nice your",age,"awsome lets get right to the quiz.")
