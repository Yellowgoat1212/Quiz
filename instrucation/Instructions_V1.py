#This version will give user muiltple choice to choose if they want instrucation or no
inst=input("Hey would like to read the instruction Enter Yes or NO : ")

if inst ==  'Y' or inst  ==  'y' or  inst == 'Yes' or inst == 'yes':#I have placed multiple options just incase users enter upper case answers or short words 
    print("<=========================================================================================================================================================================>")
    print("Welcome to NBA Quiz program. Quiz will be a multichoice quiz, giving you option answers to choose from alphabtical order. Please follow the instructions and enjoy playing the quiz.")
    print("<=========================================================================================================================================================================>")
    print("Once you enter the quiz you'll have multiple choice to choose from A,B,C and D")
    print("This Quiz is based on National Basketball Asscositon so you'll be questioned about the history and general knowledage behind the National Basketball Association")
    print("Last but no least ,read the questions carefully and answer the questions corretly Good Luck")
else:
    print("Let's began")#If user's enter no the program automically prints Let's began the quiz
