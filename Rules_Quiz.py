#This version will give user muiltple choice to choose if they want rules or no
print("======================================================================================================================================================================")
print("Welcome to NBA Quiz program. Program will be a multichoice quiz giving you option answers to choose from. Please follow the instructions and enjoy playing the quiz.")
print("======================================================================================================================================================================")

def instructions():
    inst=input("Hey would like to read the instruction Enter Yes or NO : ").lower()
    if inst == 'Yes' or inst == 'YES' or inst == 'Y' or inst == 'ye':
        print("Once you enter the quiz you'll have multiple choice to choose from A,B,C and D")
        print("Read the questions carefully and answer corretly Good Luck")
    else:
        print("Ok. Lets begin the game.")
instructions()
