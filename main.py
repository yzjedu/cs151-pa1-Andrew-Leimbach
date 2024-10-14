# Programmer: Andrew Leimbach
# Course:  CS151, Dr. Zee
# Due Date: 10/09/24
# PA Assignment: 1
# Problem Statement: Creating a text adventure game, using inputs from the user that affect the path of the story.
# Data In: Name, age, animal preference, cruise duration, and personal choices
# Data Out:  Different statements are outputted based on users input.


#Input user's name and display welcome statement
user_name = input("Enter your name: ")
print(f"Welcome to the jungle cruise, {user_name}! Are you ready for an adventure?")

#Input user's age
age = int(input("Enter your age: "))

#Age-based responses
if age < 12:
    print("You are young! Let's make sure the adventure is safe.")
elif 12 <= age <= 60:
    print("That's a great age! Exciting times ahead.")
else:
    print("Experience is on your side! Let's embark on a nice journey.")

#Input user's animal preference
animal = input("What's your favorite animal? (tiger, elephant, monkey): ")

#Animal-based responses
if animal == "tiger":
    print("Oh! A tiger is a fierce choice. Let’s head toward the deep jungle.")
elif animal == "elephant":
    print("An elephant! We will go towards the riverbank where they gather.")
else:
    print("Monkeys are playful! We’ll venture into the trees where they swing.")

# Input user's estimated cruise duration in hours
duration = float(input("How long do you plan to cruise? (in hours): "))

#Duration-based responses
if duration < 1.0:
    print("A quick cruise, eh? We'll have to skip all the fun.")
elif 1.0 <= duration < 3.0:
    print("A moderate adventure! We can explore some hidden spots.")
else:
    print("A long cruise! We can explore the depths of the jungle.")

# Input users approach preference
print("As you continue, you hear noise up ahead. Suddenly, you spot a mysterious animal! What do you want to do?")
choice = input("Enter your choice (approach, observe from a distance, back away): ").lower()

#Responding to user's choice about approaching an animal
if choice == "approach":
    print("You bravely approach the animal. Do you want to offer it food? (yes/no)")
    offer_food = input("Your decision: ")

    print("Before you decide, you notice its behavior. Is it growling or calm? (growling/calm)")
    behavior = input("Observation: ")

    if offer_food == "yes" and behavior == "calm":
        print("The animal accepts your food and leads you to a hidden grove!")
    elif offer_food == "yes" and behavior == "growling":
        print("The animal growls and retreats! You back away cautiously.")
    else:
        print("The animal seems suspicious but stays calm. You take a cautious step back.")

elif choice == "observe from a distance":
    print("You choose to watch the animal carefully. Do you want to capture a picture? (yes/no)")
    capture_decision = input("Your decision: ")

    if capture_decision == "yes":
        print("Say Cheese!")
    else:
        print("The animal wanders off, and you miss a great opportunity.")

else:
    print("You decide it's best to keep your distance and enjoy the rest of the ride!")

