#1-import the random module
import random
# Subject list
subjects = [
    "Shahrukh Khan",
    "Virat Kohli",
    "Nirmala Sitaraman",
    "A Mumbai Cat",
    "A Groups Of Monekeys",
    "Prime Minister Modi",
    "Auto Rickshaw Driver From Delhi"
]

# Actions
actions=[
    "launches",
    "cancles",
    "dances with",
    "eats",
    "declares war on",
    "orders",
    "celebrates"

]

# Places or things
places_or_things =[
    "at Red Fort", 
    "in Mumbai local Train",
    "a plate of samosa",
    "inside parliament",
    "at Ganga ghat",
    "during IPL Match ",
    "at India Gate"
]

# Loop
while True: 
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(places_or_things)

    headline = f"BREAKING NEWS: {subject} {action} {place_or_thing}!"
    print("\n"+ headline)

    user_input =input("\nDo you want another headline?(yes/no)").strip().lower()
    if user_input=="no":
       break

    print("\nThanks for the Fake News headline Generator. Have a fun!")