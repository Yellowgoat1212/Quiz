from random import shuffle#imports random for question
#varibles
index = 0
score = 0
optnum = 0

#Ask for name
def greet():
    global name
    while True:
        name = input ("Enter your name please : ")
        if name.replace(' ','').isalpha():
            break
        print("Please enter character A-Z only")
    print("Hello",name)

#Ask for age using while True 
def age():
    while True:
        age = input ("Enter your age : ")
        if age.replace(' ','').isnumeric():
            break
        print("Please enter integer only")
    print("Your age is",age)

#This code is if the end user need instrucation 
def ins():
    inst=input("\nHey would like to read the instruction Enter Yes or any other key to continue without the rules : ").lower()

    if inst  ==  'y' or   inst == 'yes' or inst == 'ye':
        print("===========================================================================================================")
        print("* Once you enter the quiz you'll have multiple choice to choose from A,B,C and D")
        print("* This Quiz is based on National Basketball Asscositon")
        print("* so you'll be questioned about the history and general knowledage behind the National Basketball Association")
        print("* Last but no least ,read the questions carefully and answer the questions corretly Good Luck")
        print("=============================================================================================================")

    else:
        print("Let's start")

#Ask if they are ready to take the quiz
def status():
    status = input("\nAre you ready to take the quiz :{}?:  \na. Yes \nb. No \n=>".format(name))


    # option of answer the end users may input
    if status == 'Yes' or status == 'yes' or status == 'yeah' or status == 'y' or status == 'ye' or status == 'A' or status == 'a':
        print(" You  may continue ")

    # what if the the user is not ready
    else:
        print("See you next time.")
        exit()
        

def rounds():#Ask for rounds,how many rounds the end users may like.
    global r , total
    while True:
        try:
            r = int(input("\nPlease enter how many rounds do you want to play there are a total of 10 round at max. : "))#correcting end users the maxmine rounds.
            if 0<r<=10:
                break
            else:
                print("Please enter the rounds in 1-10 only")
        except:
            print('Please enter rounds in numbers only (The max is 10)')#if users enter any number above 10 the program correct the users


    



print("==========================================================")#Welcome the user once they're ready to take the quiz
print("------------Welcome to NBA Quiz program-------------------")
print("-------------This quiz is made by Natan Tsegay------------")
print("==========================================================")
greet()
age()
ins()
status()
rounds()
#Using dictionary for questions and for the right answers
nbaquiz = [
        ["\nWho was the Founder of the Nation Basketball Association?",
          {'answer':'c','option':'a)Steven A.Smith\nb)Adam Silver\nc)Walt Brown\nd)Lavar Ball'}],

        ["\nWhere was the first NBA game conducted?",
         {'answer':'a','option':'a)Toronto\nb)Washington\nc)Boston\nd)kentucky'}],

        ["\nWhat player was named the G.O.A.T(Greatest of all time) that played for the Chicago Bulls in 1995?",
         {'answer':'b','option':'a)Dennis Rodman\nb)Micheal Jordan\nc)Luol Deng\nd)Derrick Rose'}],

        ["What player is leading the NBA ALL-Time scoring?",
         {'answer':'a','option':'a)Kareem Abdul-Jabbar\nb)Karl Malone\nc)Micheal Jordan\nd)Kobe Bryant'}],

        ["Who’s leading the NBa all-time 3 pointers made in the NBA right now?",
         {'answer':'c','option':'a)Stephen Curry\nb)Ben Simmons\nc)Ray Allen\nd)Reggie Miller'}],

        ["Who is leading the NBA all-time assist in the NBA?",
         {'answer':'d','option':'a)Stephen Curry\nb)Steve Nash\nc)Chris Paul\nd)John Stocktan'}],

        ["Who's leading the NBA all-time championship won?",
         {'answer':'c','option':'a)Sam Jones\nb)John Havlicek\nc)Bill Russell\nd)Satch Sanders'}],

        ["Which of these players played for the Celtics?",
         {'answer':'d','option':'a)Dwyane Wade\nb)Carmelo Anthony\nc)Chris Bosh\nd)Ray Allen '}],

        ["which team won the nba 2020 championship finals?",
          {'answer':'a','option':'a)Los Angles Lakers\nb)Boston Celtics\nc)Toronto Raptor\nd)Miami Heat'}],

        ["who won the most valuable player and defense of the year in the nba 2020?",
          {'answer':'c','option':'a)Lebron James\nb)Joel Embiid\nc)Giannis Antetokounmpo\nd)Jimmy Butler'}],
]
shuffle(nbaquiz)#shuffle for random questions. 



while r>0:
    data = nbaquiz[0]
    i = data[0]
    data = data[1]
    answer = data["answer"]
    option = data['option']


    total=r


    print(i)#printing questions
    print(option)#printing options


    while True:#while True loop
        useranswer = input("Enter your answer here please : ") #asking for inputs
        if useranswer == 'a' or useranswer == 'b' or useranswer == 'c' or useranswer == 'd':#this is user answer where there wide range of option to pick 
            if useranswer == answer:#checking user answer 
                print("=====================")
                print("Correct!")
                print("=====================")
                score += 1
                print("*********************************")
                print("    Your score is",score         )#printing score 
                print("*********************************")
            else:
                print("============================= ")
                print("Oops your answer is wrong     ")#correcting the users by show them the answer and show the score didn't increase
                print("       The answer is",answer  )#showing right answer
                print("*******************************")
                print("  You score is",score           )
                print("============================= ")
            del nbaquiz[0]#deleting the question to not repeat the question 
            r-=1
            break#breaking the loop
        else:
            print("===========================")
            print("Please enter a,b,c,or d")#this happens if the user inputs characters or if they input blank.
            print("===========================")


                                
print("\nYou've scored",score,"out of",total,"questions")#showing the result after the quiz end.
print("your score in percentage",round(score/10*100,2),"%")#show round score.
print("You have ended the quiz succesfully, Congrats.")#congratulating user
print("********************************************************************************************")
print("\nIf there is anything that has affected you in anyway email me 19322@students.mrgs.school.nz")#This is a disclaimer if i have done any harm or offened anyone with anything to let me via email.
print("********************************************************************************************")
print("You have ended the quiz succesfully, Congrats.")
exit()#exit to finish the quiz
