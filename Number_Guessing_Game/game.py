import random

num = random.randint(1,10)

guess = 0

while guess != num:
    guess = int(input("Enter your guessed number: "))

    if(guess>num) :
        print("Guessed too high.🙂")
    elif (guess<num) :
        print("Guessed too low.😑")
    else :
        print("Congo.You guessed it right.🎉")
        print("The number was ", num)
        break
    
print("Thanks for playing.😎")