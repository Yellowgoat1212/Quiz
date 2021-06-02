while True:
    try:
        number=int(input('How range you want :'))
        if number>len(nbaquiz) or number<=0:
            print('range 0-'+len(nbaquiz))
        else:
            total=number
            break
    except:
        print('Place type number')
