def show_balance():
    print("*************************")
    print(f"Your Account Balance is{balance:.2f}")

def deposit():
    amount=float(input("Enter Amount To Be Deposited"))
    if amount<0:
        print("*************************")
        print("YOU CANT DEPOSIT NEGATIVE AMOUNT")
        print("*************************")
        return 0
    else:
        return amount
def withdraw():
    amount=int(input("Enter Amount To Be Withdrawn:"))
    if amount<0:
        print("*************************")
        print("you can take negative amount ,it doesnt exist")
        print("*************************")
    elif amount>balance:
        print("*************************")
        print("Insuffecient funds")
        print("*************************")
    else:
        return amount

balance=0
is_running=True

while is_running:
    print("*************************")
    print("     Banking Program     ")
    print("1.Show Balance")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Exit")
    print("*************************")

    choice=int(input("Enter Your choice (1-4)"))
    if choice==1:
        show_balance()
    elif choice==2:
        balance+=deposit()
    elif choice==3:
        balance-=withdraw()
    elif choice==4:
        is_running=False
    else:
        print("Enter a valid choice")

print("Thankyou have a nice day")