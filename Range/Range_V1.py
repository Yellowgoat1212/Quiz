while True:
    try:
        number=int(input('How range you want :'))#Giving the users options to how many questions they want.
        if number>len(nbaquiz) or number<=0:
            print('range 0-'+len(nbaquiz))
        else:
            total=number
            break
    except:
        print('Please enter a number from 1-10')#this is if the users make mistake on entering more range than expected.
