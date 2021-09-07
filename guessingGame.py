import random

number = random.randint(1,100)
chances = 0
chancesLeft = 5

while chances<5:
    guess = int(input("Guess a number between 1-100: "))
    if guess<number:
        print("Your guess was too low, Enter a number higher than",guess)
        chances+=1
        chancesLeft-=1
        print('Chances Left : ',chancesLeft)
    elif guess>number:
        print("Your guess was too high , Enter a number less than",guess)
        chances+=1
        chancesLeft-=1
        print('Chances Left : ',chancesLeft)
    else:
        print('YOU WON!')
        break
if not chances<5:
    print("YOU ARE OUT OF CHANCES")
    print("The number is:",number)