print("Welcome to the Trivia Game!")

playing = input("Do you want to play? ")

# If player types "no" - program will quit
if playing.lower() != "yes":
    quit()

print("Ok! Let's play!")
score = 0

# Questions

# Question 1
answer = input("Who was the first President of the United States? ")
if answer.lower() == "george washington":
    print("Correct!")
    # if correct - add 1 to the score
    score += 1
else: 
    print("Wrong!")


# Question 2
answer = input("What ocean is the largest? ")
if answer.lower() == "pacific":
    print("Correct!")
    score += 1
else: 
    print("Wrong!")


# Question 3
answer = input("What continent is China located in? ")
if answer.lower() == "asia":
    print("Correct!")
    score +=1
else: 
    print("Wrong!")


# Question 4
answer = input("How many moons does Earth have? ")
if answer.lower() == "one":
    print("Correct!")
    score += 1
else: 
    print("Wrong!")


# Question 5
answer = input("Are turtles reptiles or mammals? ")
if answer.lower() == "reptiles":
    print("Correct!")
    score +=1
else: 
    print("Wrong!")


print("You got " + str(score) + " questions correct!")

