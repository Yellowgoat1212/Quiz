#This version will give user muiltple choice to choose if they want rules or no
print("=================================")
print("Welcome to NBA Quiz program.")
print("=================================")

def instructions():
  while True:
    inst=input("Would like to read the instruction Enter Y or N : ").lower()#I have added .Lower() so the program can accept upper case
    if inst == 'yes' or inst == 'ye' or inst == 'yeah':
      print("==================================================================")

      print("Once you enter the quiz you'll have multiple choice to choose from A,B,C and D")
      print("Read the questions carefully and answer corretly. Good Luck")

      print("==================================================================")
      break
    elif inst == 'Maybe' or inst == 'maybe' or inst == '':#If users enter maybe the program repeats itself
      print("Please enter Yes/No") 

    else:
        print("Ok. Lets begin the game.")
        break
instructions()
