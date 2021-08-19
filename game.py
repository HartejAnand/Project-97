import random
number=random.randint(0,9)
tries=0

if(tries==0):
    answer1=int (input("guess a number between 0 and 9: "))
    print(answer1)
    if(answer1==number):
        print("YOU GUESSED IT! FIRST TRY!")
    else:
        tries=tries+1
        if(answer1>number):
            print("too high")
        elif(answer1<number):
            print("too low")


if(tries==1):
    answer2=int (input("Try again: "))
    print(answer2)
    if(answer2==number):
        print("YOU GOT IT!!")
    else:
        tries=tries+1
        if(answer2>number):
            print("too high")
        elif(answer2<number):
            print("too low")


if(tries==2):
    answer3=int (input("One last time: "))
    print(answer3)
    if(answer3==number):
        print("Great Job!")
    else:
        print("Strike 3, you're out! The correct answer was:")
        print(number)