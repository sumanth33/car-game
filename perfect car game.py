started = False
while True :

    command = input(">>").lower()
    if command =="start" :
        if started  :
            print(" car has already started ")
        else :
            started  = True
            print("car started")

    elif command == "stop" :
        if not started  :
            print(" car has not started ")
        else :
            started = False
            print("stop the car")

    elif command == "help" :
        print (''' 
start>> start the car..
stop>> stop the car
quit>> exit the game ''')
    else :
        pass