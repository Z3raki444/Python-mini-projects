print("Welcome to the Quiz Game!")
print("---------------------------")

score = 0

# Question 1
answer = input("1. What is the capital of Germany? ")

if answer.lower() == "berlin":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is Berlin.")

# Question 2
answer = input("2. Who developed Python? ")

if answer.lower() == "guido van rossum":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is Guido van Rossum.")

# Question 3
answer = input("3. What does CPU stand for? ")

if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is Central Processing Unit.")

# Question 4
answer = input("4. What year was Python first released? ")

if answer == "1991":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is 1991.")

# Question 5
answer = input("5. What symbol is used for comments in Python? ")

if answer == "#":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is #.")

print("---------------------------")
print("Quiz finished!")
print("Your score:", score, "/ 5")