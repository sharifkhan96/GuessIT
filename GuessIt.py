import random


random_num = random.randint(1, 100)
while True:
    guess = int(input('Enter a number between 1-100: '))

    try:
        if guess > random_num:
            print("Too high, try again!!")
        elif guess < random_num:
            print("Too low, try again!! ")
        else:
            print("Contragualations, you guess it!!!")
            break
    except ValueError:
        print("Invalid Number, try again. ")



