#this program will ask range of questions the users want to answer
#this program uses a function called ask_rounds

def ask_rounds():
    rounds = int(input("enter the number of rounds you want to play : "))
    if rounds>=1:
        print("ok. so you want only",rounds)
    elif rounds==0:
        print(" You must enter a number for rounds")


#calling the function
ask_rounds() 
