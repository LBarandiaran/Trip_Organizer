# Day Trip Generator Project Luis Barandiaran devCodeCamp

# (5 points): As a developer, I want to make at least three commits with descriptive messages.
# (5 points): As a developer, I want to store my destinations, restaurants, mode of transportations, and entertainments in their own separate lists.
# (5 points): As a user, I want a destination to be randomly selected for my day trip.
# (5 points): As a user, I want a restaurant to be randomly selected for my day trip.
# (5 points): As a user, I want a mode of transportation to be randomly selected for my day trip.
# (5 points): As a user, I want a form of entertainment to be randomly selected for my day trip.
# (15 points): As a user, I want to be able to randomly re-select a destination, restaurant, mode of transportation, and/or form of entertainment if I don’t like one or more of those things.
# (10 points): As a user, I want to be able to confirm that my day trip is “complete” once I like all of the random selections.
# (10 points): As a user, I want to display my completed trip in the console.
# (5 points): As a developer, I want all of my functions to have a Single Responsibility. Remember, each function should do just one thing!


city_list = ["Lima, Peru", "Boulder, Colorado", "Chicago, Illinois", "London, England", "Corpus Christi, Texas", "Seoul, South Korea"]

transportation_list = ["plane", "train", "boat", "stagecoach", "teleporter", "Slip 'n Slide"]

lima_entertainment_list = ["visiting the central Plaza downtown", "going to the beach", "working on survival skills at a soccer game", "shopping 'till you drop at an artisanal market"]
boulder_entertainment_list = ["going hiking along the Flatirons", "taking in a CU Buffs football game at Folsom Field", "climbing The Bastile in Eldorado Canyon", "strolling around the Pearl Street Mall"]
chicago_entertainment_list = ["going to the Field Museum", "visiting the Navy Pier and Aquarium", "checking out the beach and swim in Lake Michigan", "visiting the observation deck at the top of the Hancock Building"]
london_entertainment_list = ["taking in a concert at St. Martin in the Fields", "visiting the British Museum", "driving around and around Picadilly Circus for a couple hours", "walking along the River Thames"]
corpus_entertainment_list = ["going out to Padre Island and enjoying the beach", "visiting the USS Lexington", "playing a round of golf", "going to check out the boats at the Marina downtown"]
seoul_entertainment_list = ["taking a tour of the DMZ north of the city", "walking the networks of parks along the Han River", "enjoying the shopping and coffee houses in Apgujeong", "spending some time at a PC bang"]

lima_restaurant_list = ["Central", "La Mar", "Astrid & Gaston", "Punto Azul"]
boulder_restaurant_list = ["Frasca", "La Corrida", "The Kitchen", "Zoe Ma Ma"]
chicago_restaurant_list = ["Gino's", "Charlie Trotter's", "Alinea", "Lula Cafe"]
london_restaurant_list = ["Chishuru", "Planque", "Le Gavroche", "Singburi"]
corpus_restaurant_list = ["Executive Surf Club", "Taqueria Jalisco", "Las Milpas", "Whataburger"]
seoul_restaurant_list = ["Jungsik", "La Yeon", "Gaon", "Cleo"]

import random
from tkinter import N, Y       # built-in module for random generation

print("Welcome to the Day Trip Generator!  Let me apologize in advance, but you did put your vacation in my hands!  Let's see what we can come up with...")

# # Create a random item generator

def random_item_picker(list):
    random_item = random.choice(list)
    return random_item



# #  Create a City Corfirmation function

def city_confirmation():
    random_city = random_item_picker(city_list)
    destination_choice = input(f"We have selected {random_city} for your destination! Would you like to go to this city? Enter y/n: ")
    if destination_choice == "y":
        print("That's great! You will have a wonderful visit there! Now let's talk about transportation...")
        return random_city
    elif destination_choice == "n":
        print("No problem.... it's the off-season there anyway, let's make another choice")
        return city_confirmation()
    elif destination_choice != "y" or "n":
        print("Please use y/n only")
        return city_confirmation()
    
confirmed_city = city_confirmation()

# #  Create a Transporation Confirmation function

def travel_confirmation():
    random_trans = random_item_picker(transportation_list)
    trans_choice = input(f"We have selected {random_trans} for your mode of transportation!  Is this your preferred method of travel? Enter y/n: ")
    if trans_choice == "y":
        print("OK wonderful!  Now let's talk about entertainment...")
        return random_trans
    elif trans_choice == "n":
        print("Not to worry, there are other transporation options...")
        return travel_confirmation()
    elif trans_choice != "y" or "n":
        print("Please use y/n only")
        return travel_confirmation()

confirmed_trans = travel_confirmation()


# #  Create an Entertainment Confirmation function

def entertain_confirmation():
    if confirmed_city == "Lima, Peru":   #I'm sure there's a more elegant way of calling the list item: I was thinking "if city_confirmation = city_list[0]:" or something like that
        random_entertain = random_item_picker(lima_entertainment_list)
        entertain_choice = input(f"We have selected {random_entertain} for your entertainment option!  Does this sound like fun?  Enter y/n: ")
        if entertain_choice == "y":
            print("Great choice! Now let's talk about dining options...")
            return random_entertain
        elif entertain_choice == "n":
            print("Not a problem, there are other activities, let's make another choice...")
            return entertain_confirmation()
        elif entertain_choice != "y" or "n":
            print("Please use y/n only")
            return entertain_confirmation()
    if confirmed_city == "Boulder, Colorado":   
        random_entertain = random_item_picker(boulder_entertainment_list)
        entertain_choice = input(f"We have selected {random_entertain} for your entertainment option!  Does this sound like fun?  Enter y/n: ")
        if entertain_choice == "y":
            print("Great choice! Now let's talk about dining options...")
            return random_entertain
        elif entertain_choice == "n":
            print("Not a problem, there are other activities, let's make another choice...")
            return entertain_confirmation()
        elif entertain_choice != "y" or "n":
            print("Please use y/n only")
            return entertain_confirmation()
    if confirmed_city == "Chicago, Illinois":   
        random_entertain = random_item_picker(chicago_entertainment_list)
        entertain_choice = input(f"We have selected {random_entertain} for your entertainment option!  Does this sound like fun?  Enter y/n: ")
        if entertain_choice == "y":
            print("Great choice! Now let's talk about dining options...")
            return random_entertain
        elif entertain_choice == "n":
            print("Not a problem, there are other activities, let's make another choice...")
            return entertain_confirmation()
        elif entertain_choice != "y" or "n":
            print("Please use y/n only")
            return entertain_confirmation()
    if confirmed_city == "London, England":   
        random_entertain = random_item_picker(london_entertainment_list)
        entertain_choice = input(f"We have selected {random_entertain} for your entertainment option!  Does this sound like fun?  Enter y/n: ")
        if entertain_choice == "y":
            print("Great choice! Now let's talk about dining options...")
            return random_entertain
        elif entertain_choice == "n":
            print("Not a problem, there are other activities, let's make another choice...")
            return entertain_confirmation()
        elif entertain_choice != "y" or "n":
            print("Please use y/n only")
            return entertain_confirmation()
    if confirmed_city == "Corpus Christi, Texas": 
        random_entertain = random_item_picker(corpus_entertainment_list)
        entertain_choice = input(f"We have selected {random_entertain} for your entertainment option!  Does this sound like fun?  Enter y/n: ")
        if entertain_choice == "y":
            print("Great choice! Now let's talk about dining options...")
            return random_entertain
        elif entertain_choice == "n":
            print("Not a problem, there are other activities, let's make another choice...")
            return entertain_confirmation()
        elif entertain_choice != "y" or "n":
            print("Please use y/n only")
            return entertain_confirmation()
    if confirmed_city == "Seoul, South Korea":
        random_entertain = random_item_picker(seoul_entertainment_list)
        entertain_choice = input(f"We have selected {random_entertain} for your entertainment option!  Does this sound like fun?  Enter y/n: ")
        if entertain_choice == "y":
            print("Great choice! Now let's talk about dining options...")
            return random_entertain
        elif entertain_choice == "n":
            print("Not a problem, there are other activities, let's make another choice...")
            return entertain_confirmation()
        elif entertain_choice != "y" or "n":
            print("Please use y/n only")
            return entertain_confirmation()

confirmed_entertain = entertain_confirmation()

# # Create a Dining Confirmation function

def dining_confirmation():
    if confirmed_city == "Lima, Peru":
        random_dining = random_item_picker(lima_restaurant_list)
        dining_choice = input(f"We have selected {random_dining} for your dining option!  Does this sound like fun?  Enter y/n: ")
        if dining_choice == "y":
            print("Great choice! They have some of the best food in the city!")
            return random_dining
        elif dining_choice == "n":
            print("Not a problem, there are other establishments, let's make another choice...")
            return dining_confirmation()
        elif dining_choice != "y" or "n":
            print("Please use y/n only")
            return dining_confirmation()
    if confirmed_city == "Boulder, Colorado":
        random_dining = random_item_picker(boulder_restaurant_list)
        dining_choice = input(f"We have selected {random_dining} for your dining option!  Does this sound like fun?  Enter y/n: ")
        if dining_choice == "y":
            print("Great choice! They have some of the best food in the city!")
            return random_dining
        elif dining_choice == "n":
            print("Not a problem, there are other establishments, let's make another choice...")
            return dining_confirmation()
        elif dining_choice != "y" or "n":
            print("Please use y/n only")
            return dining_confirmation()
    if confirmed_city == "Chicago, Illinois":
        random_dining = random_item_picker(chicago_restaurant_list)
        dining_choice = input(f"We have selected {random_dining} for your dining option!  Does this sound like fun?  Enter y/n: ")
        if dining_choice == "y":
            print("Great choice! They have some of the best food in the city!")
            return random_dining
        elif dining_choice == "n":
            print("Not a problem, there are other establishments, let's make another choice...")
            return dining_confirmation()
        elif dining_choice != "y" or "n":
            print("Please use y/n only")
            return dining_confirmation()
    if confirmed_city == "London, England":
        random_dining = random_item_picker(london_restaurant_list)
        dining_choice = input(f"We have selected {random_dining} for your dining option!  Does this sound like fun?  Enter y/n: ")
        if dining_choice == "y":
            print("Great choice! They have some of the best food in the city!")
            return random_dining
        elif dining_choice == "n":
            print("Not a problem, there are other establishments, let's make another choice...")
            return dining_confirmation()
        elif dining_choice != "y" or "n":
            print("Please use y/n only")
            return dining_confirmation()
    if confirmed_city == "Corpus Christi, Texas":
        random_dining = random_item_picker(corpus_restaurant_list)
        dining_choice = input(f"We have selected {random_dining} for your dining option!  Does this sound like fun?  Enter y/n: ")
        if dining_choice == "y":
            print("Great choice! They have some of the best food in the city!")
            return random_dining
        elif dining_choice == "n":
            print("Not a problem, there are other establishments, let's make another choice...")
            return dining_confirmation()
        elif dining_choice != "y" or "n":
            print("Please use y/n only")
            return dining_confirmation()
    if confirmed_city == "Seoul, South Korea":
        random_dining = random_item_picker(seoul_restaurant_list)
        dining_choice = input(f"We have selected {random_dining} for your dining option!  Does this sound like fun?  Enter y/n: ")
        if dining_choice == "y":
            print("Great choice! They have some of the best food in the city!")
            return random_dining
        elif dining_choice == "n":
            print("Not a problem, there are other establishments, let's make another choice...")
            return dining_confirmation()
        elif dining_choice != "y" or "n":
            print("Please use y/n only")
            return dining_confirmation()

confirmed_dining = dining_confirmation()

print("Congratulations! You have completed generating your trip of a lifetime!  Now let's confirm the details!")

print("Here is your itinerary:")
print(f"Destination: {confirmed_city}")
print(f"Transporatation: {confirmed_trans}")
print(f"Entertainment: {confirmed_entertain}")
print(f"Restaurant: {confirmed_dining}")

# #  Create a Final Confirmation function

def final_confirmation():
    trip_finalize = input("Would you like to confirm this trip? Enter y/n: ")
    if trip_finalize == "y":
        print(f"OK.... You are all set!  Prepare yourself for an unforgettable getaway!  You will be arriving in {confirmed_city} by {confirmed_trans}, where you will spend the day {confirmed_entertain}. You will end the evening dining in style at {confirmed_dining}, a famous local restaurant. ")
        return trip_finalize
    elif trip_finalize == "n":
        print("*sigh* All of that work for nothing, let's start all over again")
        return city_confirmation()

finalized_trip = final_confirmation()







