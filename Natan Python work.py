# this is a simple quiz
#initial score
Q1 = 'Walter Brown'
Q2 = 'Toronto'
Q3 = 'Micheal Jordan'
Q4 = 'Kareem Abdul-Jabbar'
Q5 = 'Ray Allen'
Q6 = 'Russel Westbrook'


score = 0
#Ask for name
while True:
    name = input ("Enter your name : ")
    if name.isalpha():
        break
    print("Please enter character A-Z only")
print(name)

#Ask for age

while True:
    age = input ("Enter your age : ")
    if age.isnumeric():
        break
    print("Please enter numbers 5-80 only")
print(age)

#This code is if the end user need instrucation 
inst=input("Hey would like to read the instruction Enter Yes or NO : ").lower()

if inst ==  'Y' or inst  ==  'y' or  inst == 'Yes' or inst == 'yes':
    print("Once you enter the quiz you'll have multiple choice to choose from A,B,C and D")
    print("This Quiz is based on National Basketball Asscositon so you'll be questioned about the history and general knowledage behind the National Basketball Association")
    print("Last but no least ,read the questions carefully and answer the questions corretly Good Luck")   
else:
    print("Let start")

#Ask if they are ready to take the quiz
status = input("Are you ready to take the quiz :{}?:  \na. Yes \nb. No \n=>".format(name))

# what if the the user is not ready
if status == 'No' or status == 'no' or status == 'n' or status == 'N' :
   print("See you next time.")
   exit()
# what if the user is ready?
if status == 'Yes' or status == 'yes' or status == 'y' or status == 'Y' or status == 'Ye' or status == 'ye' or status == 'A' or status == 'a':
    print("======================================")
    print("Welcome to NBA Quiz program.Enjoy .")
    print("======================================")

# set of questions that are asked
#question 1

print("\nQuestion: 1 | score: {}".format(score))
ans=input("Who was the Founder of the Nation Basketball Association?\na.Lavar Ball\nb.Walter Brown\nc.Stephen A.Smith : ").upper()
if ans == 'WALTER BROWN' or ans == 'B':
    print('Awesome Correct')
    score +=1
else:
    print("incorrect it's" ,Q1)
    print("incorret  ")
    if score <=0:
        score =0
        

#Question 2
            
    print("\nQuestion: 2 | score: {}".format(score))
    ans=input("Where was the first NBA game conducted?\na.Chicago\nb.Washington DC\nc.Toronto : ").upper()
    if ans == 'TORONTO' or ans == 'C':
        print('Correct')
        score +=1
    else:
        print("incorrect it's" ,Q2)
        if score <=0:
            score =0
#Question 3
            
    print("\nQuestion: 3 | score: {}".format(score))
    
    ans=input("What player was named the G.O.A.T(Greatest of all time) that played for the Chicago Bulls in 1995?\na.Dennis Rodman\nb.Micheal Jordan\nc.Sccotie Pippen\nd.Derrick Rose : ")
    if ans == 'Micheal Jordan' or ans == 'micheal jordan'or ans == 'B' or ans == 'b':
        print('Correct')
        score +=1
    else:
        print("incorrect it's" ,Q3)
        if score <=0:
            score =0

#Question 4
            
    print("\nQuestion: 4 | score: {}".format(score))

    ans=input("What player is leading the NBA ALL-Time scoring?\na.Lebron James\nb.Kareem Abdul-Jabbar\nc.Karl Malone\nd.Kobe Bryant : ")
    if ans == 'Kareem Abdul-Jabbar' or ans == 'kareem abdul-jabbar'or ans == 'B' or ans == 'b':
        print('Correct')
        score +=1
    else:
        print("incorrect it's" ,Q4)
        if score <=0:
            score =0

#Question 5 
            
    print("\nQuestion: 5 | score: {}".format(score))

    ans=input("Who’s leading the NBa all-time 3 pointers made in the NBA right now?\na.Stephen Curry\nb.Ben Simmons\nc.Ray Allen\nd.Reggie Miller : ")
    if ans == 'Ray Allen' or ans == 'ray allen'or ans == 'C' or ans == 'c':
        print('Correct')
        score +=1
    else:
        print("incorrect it's" ,Q5)
        print("better luck,Next time :)")
        if score <=0:
            score =0
#Question 6
            
    print("\nQuestion: 6 | score: {}".format(score))

    ans=input("Who’s leading the NBA all-time tripple double?\na.Stephen Curry\nb.Oscar Robinson\nc.Lebron James\nd.Russel Westbrook : ")
    if ans == 'Russel Westbrook' or ans == 'russel westbrook'or ans == 'D' or ans == 'd':
        print('Correct')
        score +=1
    else:
        print("incorrect it's" ,Q6)
        print("better luck,Next time :)")
        if score <=0:
            score =0

#It's time to calculate the user points
print(" Your totall score is",score)
print("Thanks for trying my quiz feel free to come back soon")
