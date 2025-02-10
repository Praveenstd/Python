# compound intreset calculator 

principle = 0
time = 0
rate = 0

while True:
    principle = float(input("Enter the principle Amount :"))
    if principle < 0:
        print("Principle Amount cant be less than zero ")
    else:
        break

while True:
    time = float(input("Enter the Time in Years :"))
    if time < 0:
        print("Time cant be less than  zero")
    else:
        break
        

while True:
    rate = float(input("Enter the Intrest rate  :"))
    if rate < 0:
        print("Intrest Rate  cant be less than zero")
    else:
        break

print(principle)
print(rate)    
print(time)

total = principle *pow((1+ rate/100),time)
print(f"Balance after {int(time) } years : ${total:.2f}")