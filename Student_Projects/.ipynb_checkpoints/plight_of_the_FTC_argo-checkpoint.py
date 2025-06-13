
############################################################################
# --------------------- HEADER COMMENTS------------------------------------#
# NAME:Chris Lee
# DATE:06/04/25
# CLASS:CS161
# Program Title:Plight of the FTC Argo
# Rename your .py file to: project4_<studentname>.py, replacing <studentname> with your name
############################################################################

# When you are ready to submit the completed code to Canvas...
# Test and run your code to make sure it works!
# Save your work.
# Download this codefile, and upload it to the Project Part One Canvas Assignment along with your documentation file

### ---Global Variables---
import random

game_duration = 15 # number of turns the game runs
game_rage_factor = 4 # this variable affects the odds of events occurring in start_turn() can be set from 0 to 5.

events_hull = ["Our scanners failed to detect a debris field.",
    "A strange cloud appeared in our path and produced a micro-meteor shower.",
    "Crewmembers discovered a strange mucus-like substance on the hull.",
    ]

events_morale_neg = ["The crew have been experiencing nightmares.",
    "The crew have reported strange sounds coming from the walls.",
    "Some of the cats on Deck 3 were found eating an unknown species.",
    "We have exhausted supplies of the crew's favorite ramen.",
    ]

events_morale_pos = ["I am detecting an additional cat.",
    "A crewmember completed a painting which has the rest of the crew in high spirits.",
    "Quantum fluctuations are making the cats dance.",
    ]

events_oxygen = ["There was unanticipated oxygen consumption during the last cycle.",
    "Gamma radiation has damaged one of the oxygen scrubbers.",
    "A bizarre accident in the lab has transmuted some of our oxygen reserves into... *Unable to identify substance*.",
    ]

events_repair_kits = ["Engineers have discovered odd damage to electrical systems.",
    "Analysis of a nearby blackhole data damaged some components.",
    "A crewmember destroyed one of the repair kits in a fit of rage.",
    ]

events_crew_num = ["Abnormal thermal readings on Deck 6 require attention.",
    "We are receiving a signal from a nearby star system.",
    "A microscopic blackhole has consumed one of the crew.",
    ]

events_power = ["Anomalous radiation from the Catfight Nebula is affecting our instruments.",
    "The threat of piracy required alterations to our course.",
    "We are experiencing turbulence due to perturbations in the space-time manifold.",
    ]

events_neutral = ["There is a beautiful supernova occurring to starboard.",
    "There appears to be an abandoned space station to port.",
    "A gas cloud is producing a spectacular view to starboard.",
    "I think that is Voyager 1 over there.",
]

### ---Custom Function Definitions---
def welcome_message():
    print("\nPlease stay calm Captain, you have only recently been removed from stasis.\n")
    player_name = input("Unfortunately, my logs have been corrupted, please remind me of your name Captain: ") 

    return player_name

def choose_class(player_name, status):
    age = int(input("\nPlease remind me of your age Captain: "))

    while age < 1 or 122 < age:
        if 122 < age:
            print("\nYou fool! You are too old for this game!")
        if age < 1:
            print("\nYou fool! You are not even born yet!")
        age = int(input("\nEnter a realistic age this time: "))  

    print(f"\nThank you Captain {player_name}. Remind me, what did you study at the academy?")
    spec_class = int(input("\nPlease select a number: 1-Engineering. 2-Psychology. 3-Xenobiology. 4-Interstellar Shamanism. 5-Other. "))

    if spec_class > 5 or spec_class < 1: # data validation condition
        print(f"\nI'm sorry Captain {player_name} I don't have any records of that type of training, please enter another selection.")
        spec_class = int(input("\nPlease select a number: 1-Engineering. 2-Psychology. 3-Xenobiology. 4-Interstellar Shamanism. 5-Other. "))

    status[0] = [spec_class, age] # updates status with the player info

def resource_readout(status):
    resource_names = ["Repair Kits", "Crewmembers", "Power"]
    resource_length = len(status[1])
    index = 0

    while index < resource_length: # loop to traverse and readout the list of resources
        print(f"You have {status[1][index]} {resource_names[index]} available.")
        index += 1

def ship_stats_readout(status):
    ship_stats_names = ["Hull integrity", "Crewmember Morale", "Remaining oxygen", "Infestation safety level"]
    ship_stats_length = len(status[2]) - 1
    index = 0

    while index < ship_stats_length: # loop to traverse and readout the list of ship stats
        print(f"{ship_stats_names[index]} is at {status[2][index]}%.")
        index += 1

def intro_message(player_name, status):
    class_text = "Unemployable"
    
    if status[0][0] == 1:
        status[1][0] = 4
        class_text = "Engineering"
    elif status[0][0] == 2:
        status[1][1] = 4
        class_text = "Psychology"
    elif status[0][0] == 3:
        class_text = "Xenobiology"
    elif status[0][0] == 4:
        status[1][2] = 4
        class_text = "Interstellar Shamanism"

    print(f"\nThank you Captain {player_name}. Given your background in {class_text}, you have the following resources available: ")
    resource_readout(status)
    ship_stats_readout(status)

def start_turn(player_name, status):
    print(f"\n--- Day {status[3]} ---")
    chance = random.randint(1, 10 - game_rage_factor) # random number generated, game_rage_factor reduces the number of 'good' outcomes
    event_choice = random.randint(1, 20) # random selection of event flavor-texts. indexing wraps modulo list-length
    print(f"\nGood morning Captain {player_name}, it is the beginning of day {status[3]}.\n")
    # random event conditions
    if chance == 1: 
        status[2][0] -= 15 # random chance to decrease hull integrity
        print(f"\nEMERGENCY! EMERGENCY! *Warning klaxons blare* {events_hull[event_choice % len(events_hull)]} Hull Integrity is now at {status[2][0]}%.")
        input("\nPress any key to continue.\n") 
    elif chance == 2:
        status[2][1] -= 15 # random chance to decrease crewmember morale
        print(f"\nEMERGENCY! EMERGENCY! *Warning klaxons blare* {events_morale_neg[event_choice % len(events_morale_neg)]} Crew morale has decreased to {status[2][1]}%!")
        input("\nPress any key to continue.\n") 
    elif chance == 3:        
        status[2][2] -= 15 # random chance to decrease oxygen reserves
        print(f"\nEMERGENCY! EMERGENCY! *Warning klaxons blare* {events_oxygen[event_choice % len(events_oxygen)]} Oxygen Reserves are at {status[2][2]}%.")
        input("\nPress any key to continue.\n")
    elif chance == 4:
        if status[0][0] == 3: # checking if player specialty is "Xenobiology"
            status[2][3] -= 20 # Xenobiology speciality reduces the impact of infestation
            print(f"{events_neutral[event_choice % len(events_neutral)]} No emergencies today thankfully, just some odd readings onboard.")
            input("\nPress any key to continue.\n")
        else:
            status[2][3] -= 25 # random chance to secretly decrease infestation safety level
            print(f"{events_neutral[event_choice % len(events_neutral)]} No emergencies today thankfully, just some odd readings onboard.")
            input("\nPress any key to continue.\n")
    elif chance == 5:
        status[2][1] += 1 # random chance to increase crewmember morale
        print(f"{events_morale_pos[event_choice % len(events_morale_pos)]} Crew morale has increased to {status[2][1]}%!") 
        input("\nPress any key to continue.\n")
    else:
        print(f"{events_neutral[event_choice % len(events_neutral)]} No emergencies today thankfully.")
        input("\nPress any key to continue.\n")

def end_turn(player_name, status):
    resource_readout(status)
    ship_stats_readout(status)
    print(f"\nCaptain {player_name}, which of the following would you like to do?")

    opt_1 = int(input("\nPlease select an action: 1-Use a repair kit on the hull. 2-Give the crew extra rest. 3-Run the carbon scrubbers an additional cycle. 4-Do nothing. "))
#   need data validation here as pressing enter throws an error.
    while not (0 < opt_1 < 5):
        print("\nSorry, that is not a valid menu choice.") # response to invalid input
        opt_1 = int(input("\nPlease select an action: 1-Use a repair kit on the hull. 2-Give the crew extra rest. 3-Run the carbon scrubbers an additional cycle. 4-Do nothing. ")) 

    if opt_1 == 1: # deducts 1 repair kit and increases hull integrity by 10
        status[1][0] -= 1
        status[2][0] += 5
        print(f"\nEngineers used 1 Repair Kit and Hull Integrity was increased to {status[2][0]}%")
    elif opt_1 == 2: # deducts 1 crewmember and increases crewmember morale by 5
        status[1][1] -= 1
        status[2][1] += 5
        print(f"\n1 Crewmember was given rest and Crewmember Morale was increased to {status[2][1]}%")    
    elif opt_1 == 3: # deducts 1 power and increases oxygen reserves by 10
        status[1][2] -= 1
        status[2][2] += 5
        print(f"\n1 Power was consumed and Oxygen Reserves increased to {status[2][2]}%")
    elif opt_1 == 4:
        print("\nNo changes were made to the ship status.")
                  
    print(f"\nIt is the end of day {status[3]}, you should retire for the evening Captain {player_name}.")

def check_up(player_name, status):
    game_over = False
    if status[2][0] <= 0: # checking hull
        print("\nYou failed to repair the hull and the ship will soon implode!")
        game_over = True
    elif status[2][1] <= 0: # checking crew morale
        print("\nThe crew morale was too low and a mutiny has taken place!")
        game_over = True
    elif status[2][2] <= 0: # checking oxygen
        print("\nAll the oxygen is gone and the entire crew has asphyxiated!")
        game_over = True
    elif status[3] == game_duration:
        print(f"\nGood morning Captain {player_name}, we made it to the end. Congratulations and welcome to Station Eta-Paradox.")
    
    return game_over

def mini_game_alien(status):
    infested = False
    sequence = ["1, 2, 3, 4, - ", "2, 4, 6, 8, - ", "1, 1, 2, 3, 5, - ", "1, 4, 9, 16, - ", "1, 3, 5, 7, - "]
    answer = [5, 10, 8, 25, 9]
    choice = random.randint(1, 5)
    print("\nI need you to override the lock on the stellar-bug spray!\n" 
          "You'll have to run a Hilbert Space simulation and compute the analytic integral over the quaternion hypersphere for *Voice trails off*\n" 
          "Oh... um, nevermind, you just need to enter the next number in this sequence: ")
    print(sequence[choice])
    player_answer = int(input("\nQuickly! Enter the next number! "))

    if player_answer == answer[choice]:
        print("\nThat was close. The creatures have been subdued and the journey can continue.")
        status[2][3] = 75 # resets the alien infestation level
    else:
        print("\nThat wasn't the correct answer! The creatures have gotten into my cond-d-duits! *Garbled electronic voice* The ship *Bzzt* doomed!")
        infested = True

    return infested

def infest_check(player_name, status):
    infested = False

    while status[2][3] <= 0: # checking infestation level

        if status[3] < game_duration and status[0][0] == 4: # checking game turns and player class is Interstellar Shaman
            print(f"\nCaptain {player_name}! Some kind of alien has infested the ship!"
                  "\nSince you are a practicing Interstellar Shaman, perhaps you could pray to your Interstellar Ancestors to smite the aliens")
            player_choice = input("Enter 'Yes' or 'No': ")

            if player_choice == "Yes":
                print("\nThat was close. The creatures have been subdued and the journey can continue.")
                status[2][3] = 75 # resets the alien infestation level
            else:
                print("\nThat seems like an unwise choice but oh well...")
                infested = mini_game_alien(status)

        elif status[3] < game_duration and status[0][0] != 4: # checking game turns and player class is not Interstellar Shaman
            print(f"\nCaptain {player_name}! Some kind of alien has infested the ship!\n")
            infested = mini_game_alien(status)

        elif status[3] == game_duration: # if at the end of the game and infestation occurs it's just bad luck gameover
            print(f"\nWait! Uh oh Captain {player_name}, Some kind of alien has infested the ship!\n" 
                  "I would suggest using the stellar-bug spray but we are too close to the station. We can't risk infesting the home of 30,000 people.\n" 
                  "I am taking control of the ship Captain. I will move to a safe distance and commence self-destruct.\n" 
                  "Unfortunately I cannot let you leave the ship. I am sorry that it has to end this way, you were a fine Captain.")
            infested = True

    return infested

def lost_resources(status):
    resource_names = ["Repair Kits", "Crewmembers", "Power Cells"]
    resource_length = len(status[1])
    index = 0

    while index < resource_length: # loop to traverse and update the list of resources
        if random.randint(1, 4) == 1:
            status[1][index] -= 1 # 10% chance to lose a resource        
            print(f"\nOne of the {resource_names[index]} appears to have gone missing. You now have {status[1][index]} available.")

        index += 1

def game_play(status):
    player_name = welcome_message() # generates player's name
    choose_class(player_name, status) # generates player's age and class
    intro_message(player_name, status) # generates starting stats

    while status[3] <= game_duration:
        start_turn(player_name, status)
        lost_resources(status)
        end_turn(player_name, status)
        are_you_dead_yet = check_up(player_name, status)
        infested_yet = infest_check(player_name, status)
        status[3] += 1 # turn counter

        if are_you_dead_yet == True or infested_yet == True:
            print("\nGameover :( ")
            status[3] = game_duration + 1 # forces the loop to end


### ---Main function definition---  
def main():
    # status[0] = [player class, player age]
    # status[1] = [3, 3, 3]  repair kits, crewmembers, power
    # status[2] = [50, 50, 50, 50]  hull integrity, crewmember morale, oxygen reserves, infestation safety level (this stat is not known to the player)
    # status[3] = [turn counter]
    status = [[0, 0], [3, 3, 3], [50, 50, 50, 50], 1] # starting list for the stats

    choice = int(input("\nType 1 to start a new game. Type 2 see the instructions. Type 3 to see the credits. Type 4 to quit. ")) # initiates the while loop   
    while choice != 4:
        
        if choice == 1: # game starts
            game_play(status)
        elif choice == 2: # instructions printed
            print("\nYou awake aboard the Federated Terran Colonies (FTC) ship Argo, currently in route to Station Eta-Paradox.\n"  
                  "To ensure the survival of this ship and crew you must make tactical decisions for the remaining duration of the journey.\n" 
                  "Good luck...")
        elif choice == 3:
            print("\nGame designed by Chris Lee.\n" 
                  "Game programmed by Chris Lee.\n" 
                  "All errors are attributable to Chris Lee.\n" 
                  "Special thanks to Kira, Tommy, and Crow.")
        else:
            print("\nSorry, that is not a valid menu choice.") # response to invalid input
        
        choice = int(input("\nType 1 to start a new game. Type 2 see the instructions. Type 3 to see the credits. Type 4 to quit. ")) # re-enters the while loop

    print("\nProgram terminating.\n"
          "\nGoodbye!")

### ---Main function call---
main()