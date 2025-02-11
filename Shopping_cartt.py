print("🛍️✨ ***** WELCOME TO MY SHOPPING CART ***** ✨🛍️")
print("🛒🚶‍♂️🚶‍♀️ Let's go shopping!")

foods = []
prices = []
total = 0

while True:
    print("\n🛍️ Options: ")
    print("1️⃣ Add item")
    print("2️⃣ View cart")
    print("3️⃣ Checkout (q to quit)")

    choice = input("Enter your choice: ")

    if choice.lower() == "q" or choice == "3":
        break
    elif choice == "1":
        food = input("🍔 Enter a food to buy (q to quit): ")
        if food.lower() == "q":
            break
        else:
            price = float(input(f"💰 Enter the price of {food}: ₹"))
            foods.append(food)
            prices.append(price)
            print(f"✅ {food} added to cart!")
    elif choice == "2":
        print("\n🛒 ----- YOUR CART ----- 🛒")
        for food, price in zip(foods, prices):
            print(f"🛍️ {food} - ₹{price}")
        print(f"💵 Total so far: ₹{sum(prices)}")
    else:
        print("❌ Invalid choice! Please select a valid option.")

print("\n🎉🛒 ----- FINAL BILL ----- 🛒🎉")
for food, price in zip(foods, prices):
    print(f"🛍️ {food} - ₹{price}")
print(f"💰 Your total is: ₹{sum(prices)}")
print("🙏 Thanks for shopping! Have a great day! 😊")
