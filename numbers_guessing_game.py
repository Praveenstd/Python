import random
number_to_guess=random.randint(1,100)  #computer stores a random number between 1 and 100

while True:
    try:
        guess=int(input("Enter a Number between (1-100): "))

        if guess<number_to_guess:
            print("Too Low")
        elif guess>number_to_guess:
            print("Too High!")
        else:
            print("Congratulations !You guessed the number.")
            break
    except ValueError:
        print("Enter a valid number !")