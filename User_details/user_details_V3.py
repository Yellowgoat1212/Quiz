#Asking name this time we can enter last name and press space without errors being dictated. 
while True:
    name = input ("Enter your name : ")
    if name.replace(' ','').isalpha():
        break
    print("Please enter character A-Z only")
print("Hello",name)

#This is similar as name if users accidentally press space they program won't dictated any error like the previous version
while True:
    age = input ("Enter your age : ")
    if age.replace(' ','').isnumeric():
        break
    print("Please enter integer only")
print("Your age is",age)
