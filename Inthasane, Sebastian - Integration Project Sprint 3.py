# Sebastian Inthasane
# COP1500 Integration Project

print("Hello, welcome to Car Enthusiast Trivia!")
print("\n")

name = input("Get ready to start your engine! Enter your name here: ")
print("\n")

print("Hello fellow car enthusiast ", name, "!", sep="")
print("\n")

fav_car = input("Enter your favorite car here: ")
print("\n")

ans = input("Are you ready to begin Level 1? (yes/no): ")
print("\n")
score = 0
totalQuestions = 4


# Level 1
    
    # Question 1
if ans.lower() == "yes":
    ans = input("Question 1. What is the car manufacturer that has a bull as its logo? ")
    if ans.lower() == "lamborghini":
        score += 1
        print("Correct!")
        print("\n")
    else:
        print("Try again.")
        print("\n")
      
    # Question 2
    ans = input("What country does BMW originate from? ")
    if ans.lower() == "germany":
        score += 1
        print("Nice job!")
        print("\n")
    else:
        print("Not quite.")
        print("\n")

    #Question 3
    ans = input("Fill in the blank. The 5.0 liter mustang engine has _ cylinders. ")
    if ans == "8":
        score += 1
        print("Correct!")
        print("\n")
    else:
        print("Wrong!")
        print("\n")

    # Question 4
    ans = input("What car manufacturer produces the Supra model? ")
    if ans.lower() == "toyota":
        score += 1
        print("Excellent Job!")
        print("\n")
    else:
        print("Incorrect!")
        print("\n")

    # Question 5
    ans = input("What make and model is named after an emergency phone number? ")
    if ans.lower() == "porsche 911":
        score += 1
        print("You raced past level 1!")
        print("\n")
    else:
        print("Wrong, but you're almost at the finsh line for level 1.")
        print("\n")

print("You got", score, "question(s) correct on Level 1.")
print("\n")


# Level 2
ans = input("Are you ready to begin Level 2? (yes/no): ")
score = 0
totalQuestions = 4
print("\n")

# Question 1
mc_answer1 = input("What engine does the Mark 4 Toyota Supra have? \na. 2JZ \nb. SR20 \nc. 1JZ \nd. RB26 \nAnswer: ")
if mc_answer1.lower() == "a":
    score += 1
    print("Correct!")
    print("\n")
else:
    print("Wrong engine.")
    print("\n")

# Question 2
mc_answer2 = input("What model of Nissan has the nickname Godzilla? \na. Maxima \nb. Frontier \nc. 240SX \nd. GTR \nAnswer: ")
if mc_answer2.lower() == "d":
    score += 1
    print("Correct!")
    print("\n")
else:
    print("Wrong Nissan!")
    print("\n")

# Question 3
mc_answer3 = input("How much horsepower does the Dodge Hellcat Charger have? \na. 600 HP \nb. 685 HP \nc. 707 HP \nd. 900 HP \nAnswer: ")
if mc_answer3.lower() == "c":
    score += 1
    print("707 is the lucky number! Great job!")
    print("\n")
else:
    print("Not quite.")
    print("\n")

# Question 4
mc_answer3 = input("How many Lexus LFAs were produced in the entire world? \na. 500 \nb. 470 \nc. 200 \nd. 100 \nAnswer: ")
if mc_answer3.lower() == "a":
    score += 1
    print("Awesome job!")
    print("\n")
else:
    print("Not quite.")
    print("\n")

# Question 5
tf_question1 = input("The R34 Nissan Skyline is currently legal in the United States. True or false: ")
if tf_question1.lower() == "false":
    score += 1
    print("Nice job!")
    print("\n")
else:
    print("Incorrect.")
    print("\n")

print("You got", score, "question(s) correct on Level 2.")

print("\n")


#Level 3: True or False

import random

input("Awesome job! You are about to begin level 3! Click the enter key to proceed.")

print("\n")

def level_3():
    statements = []
    statements.append(["The Tesla Model S P100D has a 0-60 mph time of 2.5 seconds.", "True"])
    statements.append(["The Lamborghini Aventador has a 6 cylinder engine.", "False"])
    statements.append(["The BMW M4 is a 4 door sedan.", "False"])
    statements.append(["Newer cars are using turbochargers which allows the use of a smaller engine while maintaining the same amount of horsepower.", "True"])
    statements.append(["The 10th generation Civic Type-R was introduced in the year of 2017", "True"])

    return statements

def begin_level_3():

    tof_questions = level_3()
    random.shuffle(tof_questions)
    score = 0

    for q in tof_questions:
        print("True or False: " + q[0])

        guess = input("Enter True or False: ")
        if guess == q[1]:
            print("Great Job!")
            score = score + 1
        else:
            print("Wrong!")

begin_level_3()

print("You got", score, "correct on Level 3.")

print("\n")

print("You have completed the final level!")
print("\n")

# Bonus Round
ans = input("Would you like to enter into the 5 point bonus round?(yes/no): ")
if ans.lower() == "yes":
    prius_mpg = "58"
    guess = " "
    guess_count = 0
    guess_limit = 3
    out_of_guesses = False

    while guess != prius_mpg and not(out_of_guesses):
        if guess_count < guess_limit:
            guess = input("You have 3 attempts! Guess how many miles per gallon the 2020 Toyota Prius gets: ")
            guess_count += 1
        else:
            out_of_guesses = True

    if out_of_guesses:
        print("You ran out of guesses. Sorry!")
    else:
        print("You earned 5 bonus points! Congratulations!")

# Score Feedback
numCorrect = int(input("Enter how many questions you got correct: "))

if numCorrect < 5:
    print("Better luck next time!")
elif numCorrect > 5 and numCorrect < 10:
    print("You did a decent job!")
elif numCorrect > 10:
    print("You must be a car guru! Excellent work!")
else:
    print("Re-enter your score.")
    
print("Thank you for playing Car Enthusiast Trivia! Hope you had fun! Stay tuned for version 2!")






