# Python Quiz Game

# List of questions
questions = ("How many elements are in the periodic table?: ",
             "Which animal lays the largest eggs?: ",
             "What is the most abundant gas in Earth's atmosphere?: ",
             "How many bones are in the human body?: ",
             "Which planet in the solar system is the hottest?: ")

# Multiple choice options
options = (("A. 116", "B. 117", "C. 118", "D. 119"),
           ("A. Ostrich", "B. Crocodile", "C. Eagle", "D. Penguin"),
           ("A. Oxygen", "B. Nitrogen", "C. Carbon Dioxide", "D. Hydrogen"),
           ("A. 200", "B. 206", "C. 215", "D. 189"),
           ("A. Venus", "B. Mercury", "C. Mars", "D. Jupiter"))

# Correct answers
answers = ("C", "A", "B", "B", "A")

# User's guesses
guesses = []

score = 0  # Track user's score

# Loop through questions
for index in range(len(questions)):
    print("\n" + questions[index])  # Print question
    for option in options[index]:  # Print answer choices
        print(option)

    guess = input("Enter your answer (A, B, C, or D): ").upper()
    
    while guess not in ["A", "B", "C", "D"]:
        print("Invalid input! Please enter A, B, C, or D.")
        guess = input("Enter your answer (A, B, C, or D): ").upper()
    
    guesses.append(guess)  # Store user guess

    if guess == answers[index]:  # Check answer
        print("✅ Correct!")
        score += 1
    else:
        print(f"❌ Wrong! The correct answer was {answers[index]}.")

# Final score and feedback
print("\n🎯 Quiz Completed! 🎯")
print(f"Your final score: {score}/{len(questions)}")

# Show correct answers vs user guesses
print("\nYour Answers vs Correct Answers:")
for i in range(len(questions)):
    print(f"Q{i+1}: {questions[i]}")
    print(f"Your Answer: {guesses[i]}  |  Correct Answer: {answers[i]}")
    print("-" * 40)

# Final message based on performance
if score == len(questions):
    print("🏆 Excellent! You got everything right! 🎉")
elif score >= len(questions) // 2:
    print("😊 Good job! You got more than half correct.")
else:
    print("😢 Keep practicing! You'll get better!")

