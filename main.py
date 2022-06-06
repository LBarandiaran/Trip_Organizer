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

import random       # built-in module for random generation

# # Create a random city destination

def random_item_picker(list):
    random_item = random.choice(list)
    return random_item

def city_confirmation():
    random_city = random_item_picker(city_list)
    destination_choice = input(f"We have selected {random_city} for your destination! Would you like to go to this city? Enter y/n: ")
    if destination_choice == "y":
        print("That's great! You will have a wonderful visit there! Now let's talk about transporatation...")
        return random_city
    elif destination_choice == "n":
        print("No problem.... it's the off-season there anyway, let's make another choice")
        return city_confirmation()
    
confirmed_city = city_confirmation()





