import random

def runGame():
    print ("************************************")
    print ("***     Welcome to the Game !    ***")
    print ("************************************")
    # secretNumber = int(random.random() * 100) # 0.0 1.0

    secretNumber = int(random.randrange(1,101))

    totalRequest = 3


    for request in range(1, totalRequest +1):
        print("Request {} of {}".format(request, totalRequest))
        requestNumber = int(input("Input a number between 1 and 100: "))

        if(requestNumber > 100 or requestNumber < 1 ):
            print("Number invalid, please input a number betweem 1 amd 100")
            continue

        if (secretNumber == int(requestNumber) ):
            print("You win !!")
            break
        elif(request == totalRequest):
            print("You lose !! The Number was {0}".format(secretNumber))
        else:
            print("Try again...")