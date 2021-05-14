# this is a simple quiz
#initial score
Q1 = 'Walter Brown'
Q2 = 'Toronto'
Q3 = 'Micheal Jordan'
Q4 = 'Kareem Abdul-Jabbar'
Q5 = 'Ray Allen'

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

#Ask for year level
yrlvl = int(input("Enter your year level: "))

#Ask if they are ready to take the quiz
status = input("Are you ready to take the quiz :{}?:  \na. Yes \nb. No \n=>".format(name))

# what if the the user is not ready
if status == 'No' or status == 'no' or status == 'n' or status == 'N' :
   print("See you next time.")
# what if the user is ready?
if status == 'Yes' or status == 'yes' or status == 'y' or status == 'Y' or status == 'Ye' or status == 'ye' or status == 'A' or status == 'a':
    print("Welcome to the quiz.")

# set of questions that are asked
#question 1

    print("\nQuestion: 1 | score: {}".format(score))
    ans=input("Who was the Founder of the Nation Basketball Association?\na.Lavar Ball\nb.Walter Brown\nc.Stephen A.Smith : ").upper()
    if ans == 'WALTER BROWN' or ans == 'B':
        print('Awesome Correct')
        score +=2
    else:
       print("incorrect it's" ,Q1)
       print("better luck next Question ¯\_(ツ)_/¯ ")
       if score <=0:
            score =0
        

#Question 2
            
    print("\nQuestion: 2 | score: {}".format(score))
    ans=input("Where was the first NBA game conducted?\na.Chicage\nb.Washington DC\nc.Toronto : ").upper()
    if ans == 'TORONTO' or ans == 'C':
        print('Correct')
        score +=2
    else:
        print("incorrect it's" ,Q2)
        if score <=0:
            score =0
#Question 3
            
    print("\nQuestion: 3 | score: {}".format(score))
    
    ans=input("What player was named the G.O.A.T(Greatest of all time) that played for the Chicago Bulls in 1995?\na.Dennis Rodman\nb.Micheal Jordan\nc.Sccotie Pippen\nd.Derrick Rose : ")
    if ans == 'Micheal Jordan' or ans == 'micheal jordan'or ans == 'B' or ans == 'b':
        print('Correct')
        score +=2
    else:
        print("incorrect it's" ,Q3)
        if score <=0:
            score =0

#Question 4
            
    print("\nQuestion: 4 | score: {}".format(score))

    ans=input("What player is leading the NBA ALL-Time scoring?\na.Lebron James\nb.Kareem Abdul-Jabbar\nc.Karl Malone\nd.Kobe Bryant : ")
    if ans == 'Kareem Abdul-Jabbar' or ans == 'kareem abdul-jabbar'or ans == 'B' or ans == 'b':
        print('Correct')
        score +=2
    else:
        print("incorrect it's" ,Q4)
        if score <=0:
            score =0

#Question 5 
            
    print("\nQuestion: 5 | score: {}".format(score))

    ans=input("Who’s leading the NBa all-time 3 pointers made in the NBA right now?\na.Stephen Curry\nb.Ben Simmons\nc.Ray Allen\nd.Reggie Miller : ")
    if ans == 'Ray Allen' or ans == 'ray allen'or ans == 'C' or ans == 'c':
        print('Correct')
        score +=2
    else:
        print("incorrect it's" ,Q5)
        print("You did well but this question gotta be the easiest one ¯\_(ツ)_/¯")
        if score <=0:
            score =0
            

#It's time to calculate the user points
print(" Your totall score is",score)


