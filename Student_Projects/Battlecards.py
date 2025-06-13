#Author: Vince Budak
#CS161 - Spring 2025

import time
import random
import sys

#-----initialize variables for player, kingdom, and NPC names-----
player_name = ""
npc_name = ["Adonis", "Kieran", "Kiernan", "Evan", "Evin", "Evander", "Callan", "Elyan",  
            "Percival", "Elijah", "Wesley", "Wren", "Ren", "Evren", "Taran", "Avis",
            "Gwyneth", "Guinevere", "Elyse", "Evaine", "Aveline", "Vivaine", "Nettie"]
continue_playing = True

#-----title card-----
def title_card():
    print(r"     ______   _______ __________________ _        _______    _______  _______  _______  ______   _______    ")
    print(r"    (  ___ \ (  ___  )\__   __/\__   __/( \      (  ____ \  (  ____ \(  ___  )(  ____ )(  __  \ (  ____ \   ")
    print(r"    | (   ) )| (   ) |   ) (      ) (   | (      | (    \/  | (    \/| (   ) || (    )|| (  \  )| (    \/   ")
    print(r"    | (__/ / | (___) |   | |      | |   | |      | (__      | |      | (___) || (____)|| |   ) || (_____    ")
    print(r"    |  __ (  |  ___  |   | |      | |   | |      |  __)     | |      |  ___  ||     __)| |   | |(_____  )   ")
    print(r"    | (  \ \ | (   ) |   | |      | |   | |      | (        | |      | (   ) || (\ (   | |   ) |      ) |   ")
    print(r"    | )___) )| )   ( |   | |      | |   | (____/\| (____/\  | (____/\| )   ( || ) \ \__| (__/  )/\____) |   ")
    print(r"    |/ \___/ |/     \|   )_(      )_(   (_______/(_______/  (_______/|/     \||/   \__/(______/ \_______)   ")
    time.sleep(1)

#-----get player name-----
def get_player_name():
    global player_name
    player_name = input("What is your name? " )

#-----choose random NPC name from list-----
def get_npc_name():
    global npc_name
    npc_name = random.choice(npc_name)

#-----greet the player, state their kingdom and opponent by name-----
def intro_greeting():
    global player_name
    global npc_name
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(f"Greetings {player_name}! Prepare yourself for battle!")
    time.sleep(1)
    print(f"You will be battling against the great and terrible {npc_name}!")
    time.sleep(1)

#-----package all pregame stuff-----
def pregame():
    get_player_name()
    get_npc_name()
    intro_greeting()

#-----set a difficulty level for the npc-----
def difficulty_level(npc_hp):
    choice = int(input(f"What difficulty level would you like {npc_name} to be? 1 = Easy, 2 = Medium, 3 = Hard "))
    while choice < 1 or choice > 3:
        choice = int(input("Please enter either 1, 2, or 3..."))
    if choice == 1:
        npc_hp = 5
    elif choice == 2:
        npc_hp = 10
    elif choice == 3:
        npc_hp = 15
    return npc_hp

#-----startup menu-----
def opening_menu():
    print("---------------------PLAYER-MENU-----------------")
    print("1.              🔥 Start a new game 🔥           ")
    print("2.                🧾 How to play 🧾             ")
    print("3.                 🚪 Quit game 🚪               ")
    print("-------------------------------------------------")
    choice = int(input("(Enter 1, 2, or 3): "))
    if choice == 1:
        print("Starting game...")
        time.sleep(1)
        pregame()
    elif choice == 2:
        print("-------------------------HOW TO PLAY THE GAME------------------------")
        print("You and your opponent will have 3 rounds to draw cards into your hand")
        print("and place them onto 1 of 5 battlefield arenas. You will not be able to")
        print("see what your enemy plays and in what place until the Battle Phase")
        print("which takes place every 3 rounds, pitting each players cards against")
        print("each other. If a card does not have an opposing card to battle in their")
        print("arena during the Battle Phase, they will attack the player directly.")
        print("Also if a card defeats an opponent card, they will also attack the player.")
        print("The game is won or lost when one player's HP reaches 0.")
        print("")
        time.sleep(1)
        print("..::Drawing Phase::.. (every round)")
        print("You and your opponent can only hold three cards in your hand at a time.")
        print("If you have fewer than 3 cards, you will draw from a random deck during this phase.")
        print("")
        time.sleep(1)
        print("..::Playing Phase::.. (every round)")
        print("You and your opponent can play a card from their hand onto one of the battlefield")
        print("arenas. If you already have a card occupying an arena, you may not play one there.")
        print("The cards your opponent plays will be hidden until the Battle Phase, so place wisely!") 
        print("")
        time.sleep(1)
        print("..::Battle Phase::.. (every 3 rounds)")
        print("Now the fight really begins as you and your opponent's cards duke it out on")
        print("different battlefields to defeat each other, and eventually commander themselves!")
        print("Cards attack each other, and if one player has no cards to fight in a certain arena")
        print("where the other player does, the player lacking a card will take a hit to their HP.")
        print("If a card wins a battle in its arena, it will then surge forward and attack the commander.")
        print("After each Battle Phase, cards that won battles or attacked a commander remain for")
        print("the next Battle Phase, licking their wounds, ready to fight again! Two cards of the")
        print("same type will fight to the death in battle, resulting in the loss of both.")
        print("")
        time.sleep(1)
        print("-----------------")
        print("..::The Cards::..")
        print("-----------------")
        print("KNIGHT -- beats Ranger, loses to Wizard")
        print("The Knight is a strong and capable fighter, equipped with a sword, shield, and full plate armor.")
        print("In head-to-head brawls, the knight is not to be trifled with. They will easily defeat Rangers in")
        print("combat, as well as fight other knights to the death. They find their shortcomings when battling")
        print("a Wizard, due to their slower movement and metal armor. Magic + metal dont mix - ouch!")
        print("")
        time.sleep(1)
        print("RANGER -- beats Wizard, loses to Knight")
        print("The Ranger prides themself on swift and deadly blows from afar. A longbow and minimal leather")
        print("armor does the trick for them. Battling other rangers is surely a fight to the death, and a")
        print("fight with a Wizard likely goes the Ranger's way, as their superior dexterity and ability to")
        print("attack from 2afar make this a one-sided fight. However, a Knight is a Ranger's worst enemy,")
        print("as their arrows rarely penetrate the Knight's sturdy plate armor.")
        print("")
        time.sleep(1)
        print("WIZARD -- beats Knight, loses to Ranger")
        print("The Wizard has deep knowledge of the strange and deadly arcane arts. Using spells and incantations,")
        print("they scorch, freeze, and shock their enemies with elemental bursts and curses. A battle between")
        print("two Wizards is a spectacle to behold with few survirors, and Knights across the realm fear")
        print("a magical burst frying them in their armor. Rangers, however, continue to exploit the weaknesses")
        print("of Wizards by striking with arrows from afar while avoiding dangerous magical spells.")
        print("---------------------------------------------------------------------")        
        time.sleep(1)
        quit_return = 0
        while quit_return != 1 or quit_return != 2:
            quit_return = int(input("Enter 1 to return to menu or 2 to quit."))
            if quit_return == 1:
                print("Returning to main menu...")
                time.sleep(1)
                opening_menu()
                break
            elif quit_return == 2:
                print("See you next time!")
                time.sleep(2)
                sys.exit()     
    elif choice == 3:
        print("See you next time!")
        time.sleep(2)
        sys.exit()
    else:
        print("Please enter a valid choice.")
        opening_menu()

#----------------------------------- I N G A M E ---- F U N C T I O N S ----------------------------#    

#-------------------------- PLAYER FUNCTIONS --------------------------#
#-----draw a card into the player's hand-----
def player_draw(player_num_cards_hand):
    player_num_cards_hand += 1
    return player_num_cards_hand

#-----remove card from player hand and play it onto the field-----
def player_play(player_num_cards_hand, player_num_cards_field):
    player_num_cards_hand -= 1
    player_num_cards_field += 1
    return (player_num_cards_hand, player_num_cards_field)

#-----determine what card player wants to play-----
def player_play_choice(player_hand):
    return player_hand.pop(0)
    
#-----determine what arena player wants to play card to-----
def player_arena_choice(player_field1, player_field2, player_field3, player_field4, player_field5, chosen_card):
    choice = int(input(f"Which battlefield arena would you like to deploy your card to? 1/2/3/4/5 "))
    if choice == 1:
        if len(player_field1) > 0:
            print(f"Sorry, {player_name}, you already have a {player_field1} on that field, choose another.")
            time.sleep(1)
            player_arena_choice(player_field1, player_field2, player_field3, player_field4, player_field5, chosen_card)
        else:
            player_field1.append(chosen_card)
            print("------------------------------------------------------------")
            print(f"{player_name} plays a {chosen_card} in Battlefield Arena 1!")
            print("------------------------------------------------------------")
    elif choice == 2:
        if len(player_field2) > 0:
            print(f"Sorry, {player_name}, you already have a {player_field2} on that field, choose another.")
            time.sleep(1)
            player_arena_choice(player_field1, player_field2, player_field3, player_field4, player_field5, chosen_card)
        else:    
            player_field2.append(chosen_card)
            print("------------------------------------------------------------")
            print(f"{player_name} plays a {chosen_card} in Battlefield Arena 2!")
            print("------------------------------------------------------------")
    elif choice == 3:
        if len(player_field3) > 0:
            print(f"Sorry, {player_name}, you already have a {player_field3} on that field, choose another.")
            time.sleep(1)
            player_arena_choice(player_field1, player_field2, player_field3, player_field4, player_field5, chosen_card)
        else:    
            player_field3.append(chosen_card)
            print("------------------------------------------------------------")
            print(f"{player_name} plays a {chosen_card} in Battlefield Arena 3!")
            print("------------------------------------------------------------")
    elif choice == 4:
        if len(player_field4) > 0:
            print(f"Sorry, {player_name}, you already have a {player_field4} on that field, choose another.")
            time.sleep(1)
            player_arena_choice(player_field1, player_field2, player_field3, player_field4, player_field5, chosen_card)
        else:    
            player_field4.append(chosen_card)
            print("------------------------------------------------------------")
            print(f"{player_name} plays a {chosen_card} in Battlefield Arena 4!")
            print("------------------------------------------------------------")
    elif choice == 5:
        if len(player_field5) > 0:
            print(f"Sorry, {player_name}, you already have a {player_field5} on that field, choose another.")
            time.sleep(1)
            player_arena_choice(player_field1, player_field2, player_field3, player_field4, player_field5, chosen_card)
        else:    
            player_field5.append(chosen_card)
            print("------------------------------------------------------------")
            print(f"{player_name} plays a {chosen_card} in Battlefield Arena 5!")
            print("------------------------------------------------------------")
    else:
        print("Please choose battlefield 1-5...")
        player_arena_choice(player_field1, player_field2, player_field3, player_field4, player_field5, chosen_card)

#-------------------------- NPC FUNCTIONS --------------------------#
#-----draw a card into the npc's hand-----
def npc_draw(npc_num_cards_hand):
    npc_num_cards_hand += 1
    return npc_num_cards_hand

#-----remove card from npc's hand and play it onto the field-----
def npc_play(npc_num_cards_hand, npc_num_cards_field):
    npc_num_cards_hand -= 1
    npc_num_cards_field += 1
    return (npc_num_cards_hand, npc_num_cards_field)

#-----pop card out of hand to be appended-----
def npc_play_choice(npc_hand):
    return npc_hand.pop(0)

#-----choose random arena to play card-----
def npc_arena_choice(npc_field1, npc_field2, npc_field3, npc_field4, npc_field5, chosen_card):
    choice = random.choice([1,2,3,4,5])
    if len(npc_field1) > 0 and len(npc_field2) > 0 and len(npc_field3) > 0 and len(npc_field4) > 0 and len(npc_field5) > 0:
        return
    if choice == 1:
        if len(npc_field1) > 0:
            npc_arena_choice(npc_field1, npc_field2, npc_field3, npc_field4, npc_field5, chosen_card)
        else:
            npc_field1.append(chosen_card)
            print("-------------------------")
            print(f"{npc_name} plays a card.")
            print("-------------------------")
            time.sleep(1)
    elif choice == 2:
        if len(npc_field2) > 0:
            npc_arena_choice(npc_field1, npc_field2, npc_field3, npc_field4, npc_field5, chosen_card)
        else:
            npc_field2.append(chosen_card)
            print("-------------------------")
            print(f"{npc_name} plays a card.")
            print("-------------------------")
            time.sleep(1)
    elif choice == 3:
        if len(npc_field3) > 0:
            npc_arena_choice(npc_field1, npc_field2, npc_field3, npc_field4, npc_field5, chosen_card)
        else:
            npc_field3.append(chosen_card)
            print("-------------------------")
            print(f"{npc_name} plays a card.")
            print("-------------------------")
            time.sleep(1)
    elif choice == 4:
        if len(npc_field4) > 0:
            npc_arena_choice(npc_field1, npc_field2, npc_field3, npc_field4, npc_field5, chosen_card)
        else:
            npc_field4.append(chosen_card)
            print("-------------------------")
            print(f"{npc_name} plays a card.")
            print("-------------------------")
            time.sleep(1)
    elif choice == 5:
        if len(npc_field5) > 0:
            npc_arena_choice(npc_field1, npc_field2, npc_field3, npc_field4, npc_field5, chosen_card)
        else:
            npc_field5.append(chosen_card)
            print("-------------------------")
            print(f"{npc_name} plays a card.")
            print("-------------------------")
            time.sleep(1)

#-------------------------- DUAL FUNCTIONS --------------------------#
#-----shuffle the deck-----
def make_deck():
    deck = ["Knight", "Ranger", "Wizard", "Knight", "Ranger", "Wizard", "Knight", "Ranger", "Wizard", "Knight", "Ranger", "Wizard", "Knight", "Ranger", "Wizard", "Knight", "Ranger", "Wizard", "Knight", "Ranger", "Wizard", "Knight", "Ranger", "Wizard", "Knight", "Ranger", "Wizard", "Knight", "Ranger", "Wizard", "Knight", "Ranger", "Wizard", "Knight", "Ranger", "Wizard", "Knight", "Ranger", "Wizard", "Knight", "Ranger", "Wizard", "Knight", "Ranger", "Wizard", "Knight", "Ranger", "Wizard", "Knight", "Ranger", "Wizard", "Knight", "Ranger", "Wizard", "Knight", "Ranger", "Wizard", "Knight", "Ranger", "Wizard", "Knight", "Ranger", "Wizard", "Knight", "Ranger", "Wizard", "Knight", "Ranger", "Wizard", "Knight", "Ranger", "Wizard", "Knight", "Ranger", "Wizard", "Knight", "Ranger", "Wizard", "Knight", "Ranger", "Wizard", "Knight", "Ranger", "Wizard", "Knight", "Ranger", "Wizard", "Knight", "Ranger", "Wizard", "Knight", "Ranger", "Wizard", "Knight", "Ranger", "Wizard", "Knight", "Ranger", "Wizard", "Knight", "Ranger", "Wizard", "Knight", "Ranger", "Wizard", "Knight", "Ranger", "Wizard", "Knight", "Ranger", "Wizard", "Knight", "Ranger", "Wizard"]
    random.shuffle(deck)
    return deck

#-----update player on hp-----
def hp_update(player_hp, npc_hp):
    print("--------------------------------------")
    print(f"{player_name} HP: {player_hp} ❤️ ")
    print(f"{npc_name} HP: {npc_hp} ❤️ ")
    print("--------------------------------------")        

#-----determine if fields have cards in them-----
def fields_can_fight(player_field, npc_field):
    if len(player_field) > 0 and len(npc_field) > 0:
        return True
    else:
        return False

#-----compare cards and remove loser card, remove both if tie-----
def compare_cards(player_field, npc_field, player_num_cards_field, npc_num_cards_field):
    player_card = player_field[0]
    npc_card = npc_field[0]
    
    # Handle ties
    if player_card == npc_card:
        print(f"Two {player_card}s battle to the death!")
        time.sleep(1)
        player_field.pop(0)
        npc_field.pop(0)
        player_num_cards_field -= 1
        npc_num_cards_field -= 1

    # Handle player win conditions
    elif player_card == "Knight" and npc_card == "Ranger":
        print(f"{player_name}'s {player_card} defeats {npc_name}'s {npc_card}!")
        time.sleep(1)
        npc_field.pop(0)
        npc_num_cards_field -= 1
    elif player_card == "Ranger" and npc_card == "Wizard":
        print(f"{player_name}'s {player_card} defeats {npc_name}'s {npc_card}!")
        time.sleep(1)
        npc_field.pop(0)
        npc_num_cards_field -= 1
    elif player_card == "Wizard" and npc_card == "Knight":
        print(f"{player_name}'s {player_card} defeats {npc_name}'s {npc_card}!")
        time.sleep(1)
        npc_field.pop(0)
        npc_num_cards_field -= 1

    # Handle player lose conditions
    elif npc_card == "Knight" and player_card == "Ranger":
        print(f"{npc_name}'s {npc_card} defeats {player_name}'s {player_card}!")
        time.sleep(1)
        player_field.pop(0)
        player_num_cards_field -= 1
    elif npc_card == "Ranger" and player_card == "Wizard":
        print(f"{npc_name}'s {npc_card} defeats {player_name}'s {player_card}!")
        time.sleep(1)
        player_field.pop(0)
        player_num_cards_field -= 1
    elif npc_card == "Wizard" and player_card == "Knight":
        print(f"{npc_name}'s {npc_card} defeats {player_name}'s {player_card}!")
        time.sleep(1)
        player_field.pop(0)
        player_num_cards_field -= 1
    return player_num_cards_field, npc_num_cards_field

#-----determine who attacks commander-----
def no_fight(player_field, npc_field):
    if len(player_field) > 0 and len(npc_field) == 0:
        return 1
    elif len(npc_field) > 0 and len(player_field) == 0:
        return 2
    
#----------------------------------- M A I N ---- R O U T I N E ----------------------------#

def main():
    
    #defining variables
    global continue_playing
    player_num_cards_hand, player_num_cards_field = (0,0)
    npc_num_cards_hand, npc_num_cards_field = (0,0)
    player_hp = 10
    npc_hp = 1
    player_hand = []
    player_field1 = []
    player_field2 = []
    player_field3 = []
    player_field4 = []
    player_field5 = []
    npc_hand = []
    npc_field1 = []
    npc_field2 = []
    npc_field3 = []
    npc_field4 = []
    npc_field5 = []
    round_counter = 1
    deck = make_deck()
    
    #introduction
    title_card()
    opening_menu()
    npc_hp = difficulty_level(npc_hp)
    
    #game loop begins
    while continue_playing == True:

        print(f"----------DRAW PHASE---------- <<<Round: {round_counter}>>> -------------------")
        print(f"Your hand: {player_hand}")
        print(f"Your battlefields: 1:{player_field1} // 2: {player_field2} // 3: {player_field3} // 4: {player_field4} // 5: {player_field5}")
        print("-----------------------------------------------------------------")
        time.sleep(2)
        
        #check if too many cards in player hand
        if player_num_cards_hand >= 3:
            print(f"Sorry, {player_name}, your hand is full.")
        
        #give player top card from deck
        else:
            card = deck.pop(0)
            player_hand.append(card)
            player_num_cards_hand = player_draw(player_num_cards_hand)
            print("------------------------------")
            print(f"{player_name} draws a {card}.")
            print("------------------------------")
        time.sleep(1)

        #give npc top card from deck
        if npc_num_cards_hand < 3:
            card = deck.pop(0)
            npc_hand.append(card)
            npc_num_cards_hand = npc_draw(npc_num_cards_hand)
            print("------------------------------")
            print(f"{npc_name} draws a card.")
            print("------------------------------")
            time.sleep(1)

        print(f"----------PLAY PHASE---------- <<<Round: {round_counter}>>> -------------------")
        print(f"Your hand: {player_hand}")
        print(f"Your battlefields: 1:{player_field1} // 2: {player_field2} // 3: {player_field3} // 4: {player_field4} // 5: {player_field5}")
        print("---------------------------------------------------------------")
        time.sleep(2)        
        
        #decide if player wants to play 
        choice = input("Would you like to play your card this round? y/n: ")
        while choice != "y" and choice != "n":
            print("Please enter y or n...")
            time.sleep(1)
            choice = input("Would you like to play your card this round? y/n: ")            
        
        if choice == "y":        
            
            #check if too many cards on player fields
            if player_num_cards_field >= 5:
                print(f"Sorry, {player_name}, you have the maximum number of cards on the field already.")
            
            #check if no cards in player hand 
            elif player_num_cards_hand == 0:
                print(f"Sorry, {player_name}, you have no cards in your hand to play.")
            else:
                #pop top card from player hand
                #get player arena choice
                #append popped card to arena
                player_choice = player_play_choice(player_hand)
                player_arena_choice(player_field1, player_field2, player_field3, player_field4, player_field5, player_choice)  
                player_num_cards_hand, player_num_cards_field = player_play(player_num_cards_hand, player_num_cards_field)  
        elif choice == "n":
            print("You choose not to play this round.")   
        time.sleep(1)
        
        #npc automatically plays card if allowed
        if npc_num_cards_hand > 0 and npc_num_cards_field <= 5:
            #pop top card from npc hand
            #randomize arena choice
            #append popped card to arena
            npc_choice = npc_play_choice(npc_hand)
            npc_arena_choice(npc_field1, npc_field2, npc_field3, npc_field4, npc_field5, npc_choice)
            npc_num_cards_hand, npc_num_cards_field = npc_play(npc_num_cards_hand, npc_num_cards_field)

        #commence battle phase every 3 rounds
        if round_counter % 3 == 0:
            print("⚔️ ⚔️ ⚔️ A BATTLE IS ABOUT TO COMMENCE!!! ⚔️ ⚔️ ⚔️")
            time.sleep(2)
            print(f"----------BATTLE PHASE---------- <<<Round: {round_counter}>>> -------------------")
            print(f"Your hand: {player_hand}")
            print(f"Your battlefields: 1:{player_field1} // 2: {player_field2} // 3: {player_field3} // 4: {player_field4} // 5: {player_field5}")
            print("---------------------------------------------------------------")
            print(f"{npc_name}'s troops:")
            print(f"Battlefields: 1:{npc_field1} // 2: {npc_field2} // 3: {npc_field3} // 4: {npc_field4} // 5: {npc_field5}")
            print("---------------------------------------------------------------")
            time.sleep(1)
            input("Press enter to commence the battle!")
                
        #check if fields can fight
        #kill loser cards
            if fields_can_fight(player_field1, npc_field1):
                player_num_cards_field, npc_num_cards_field = compare_cards(player_field1, npc_field1, player_num_cards_field, npc_num_cards_field)
            if fields_can_fight(player_field2, npc_field2):
                player_num_cards_field, npc_num_cards_field = compare_cards(player_field2, npc_field2, player_num_cards_field, npc_num_cards_field)
            if fields_can_fight(player_field3, npc_field3):
                player_num_cards_field, npc_num_cards_field = compare_cards(player_field3, npc_field3, player_num_cards_field, npc_num_cards_field)
            if fields_can_fight(player_field4, npc_field4):
                player_num_cards_field, npc_num_cards_field = compare_cards(player_field4, npc_field4, player_num_cards_field, npc_num_cards_field)
            if fields_can_fight(player_field5, npc_field5):
                player_num_cards_field, npc_num_cards_field = compare_cards(player_field5, npc_field5, player_num_cards_field, npc_num_cards_field)
        
        #affect hp if card didn't fight
        #1 = player does damage, 2 = npc does damage    
            if no_fight(player_field1, npc_field1) == 1:
                npc_hp -= 1
                print(f"{npc_name} takes damage from Battlefield 1!")
                time.sleep(1)
            elif no_fight(player_field1, npc_field1) == 2:
                player_hp -= 1
                print(f"{player_name} takes damage from Battlefield 1!")
                time.sleep(1)
            if no_fight(player_field2, npc_field2) == 1:
                npc_hp -= 1
                print(f"{npc_name} takes damage from Battlefield 2!")
                time.sleep(1)
            elif no_fight(player_field2, npc_field2) == 2:
                player_hp -= 1
                print(f"{player_name} takes damage from Battlefield 2!")
                time.sleep(1)
            if no_fight(player_field3, npc_field3) == 1:
                npc_hp -= 1
                print(f"{npc_name} takes damage from Battlefield 3!")
                time.sleep(1)
            elif no_fight(player_field3, npc_field3) == 2:
                player_hp -= 1
                print(f"{player_name} takes damage from Battlefield 3!")
                time.sleep(1)
            if no_fight(player_field4, npc_field4) == 1:
                npc_hp -= 1
                print(f"{npc_name} takes damage from Battlefield 4!")
                time.sleep(1)
            elif no_fight(player_field4, npc_field4) == 2:
                player_hp -= 1
                print(f"{player_name} takes damage from Battlefield 4!")
                time.sleep(1)
            if no_fight(player_field5, npc_field5) == 1:
                npc_hp -= 1
                print(f"{npc_name} takes damage from Battlefield 5!")
                time.sleep(1)
            elif no_fight(player_field5, npc_field5) == 2:
                player_hp -= 1
                print(f"{player_name} takes damage from Battlefield 5!")
                time.sleep(1)

        #give post battle report
            print("⚔️ ⚔️ ⚔️ Post Battle Report ⚔️ ⚔️ ⚔️")
            print(f"----------BATTLE PHASE---------- <<<Round: {round_counter}>>> -------------------")
            print(f"Your hand: {player_hand}")
            print(f"Your battlefields: 1:{player_field1} // 2: {player_field2} // 3: {player_field3} // 4: {player_field4} // 5: {player_field5}")
            print("---------------------------------------------------------------")
            print(f"{npc_name}'s troops:")
            print(f"Battlefields: 1:{npc_field1} // 2: {npc_field2} // 3: {npc_field3} // 4: {npc_field4} // 5: {npc_field5}")
            print("---------------------------------------------------------------")
            time.sleep(1)
            hp_update(player_hp, npc_hp)
            time.sleep(1)
            input("Press enter to proceed.")

        #quit if player dies
        if player_hp == 0:
            print("-------------------------------------------")
            print(f"Oh no! {player_name} has died! You lose...")
            print("-------------------------------------------")
            time.sleep(2)
            print("The game will now quit, better luck next time!")
            time.sleep(2)
            continue_playing = False
        
        #quit if npc dies
        if npc_hp == 0:
            print("--------------------------------------------------------------")
            print(f"{player_name} has defeated {npc_name} in a thrilling victory!")
            print("--------------------------------------------------------------")
            time.sleep(2)
            print("The game will now quit, thanks for playing!")
            time.sleep(2)
            continue_playing = False
        
        round_counter += 1

main()