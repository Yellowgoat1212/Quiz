def instructions():
    inst=input("Would like to read the instruction Enter Y or N : ").lower()#I have added .Lower() so the program can accept upper case
    if inst == 'yes' or inst == 'ye' or inst == 'yeah':
      print("==================================================================")

      print("Once you enter the quiz you'll have multiple choice to choose from A,B,C and D")
      print("Read the questions carefully and answer corretly. Good Luck")

      print("==================================================================")
    else:
        print("Ok. Lets begin the game.")
        
instructions()
