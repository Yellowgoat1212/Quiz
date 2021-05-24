#Question answers are defined 
Q1 = 'Walter Brown'
Q2 = 'Toronto'

score = 0

#Question 1

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

print(" Your totall score is",score)
