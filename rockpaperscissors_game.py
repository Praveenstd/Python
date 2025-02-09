import random

choices = ('r','p','s')
emojis ={'r':'🪨','p':'📃','s':'✂️'}
while True:
    player_choice=input(("rock, paper or scissors?(r/p/s) "))
    if player_choice not in choices:
        print("Invalid choice..!") 
        continue

    computer_choice = random.choice(choices)

    print(f"You choose {emojis[player_choice]} ")
    print(f"Computer choose {emojis[computer_choice]}")


    if player_choice == computer_choice:
        print("Tie...!")
    elif (
        (player_choice == 'r' and computer_choice== 's') or 
        (player_choice == 'p' and computer_choice== 'r') or
        (player_choice == 's' and computer_choice== 'p')):
        print("You Win..!")
    else:
        print("You Lose..")

    should_continue = input('Wanna play again ? (y/n): ').lower()
    if should_continue == 'n':
        break
    
    

print("Thanks for Playing 😊😍😍😍")