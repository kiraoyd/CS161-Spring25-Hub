############################################################################
# --------------------- HEADER COMMENTS------------------------------------#
# NAME: Morgan Steeneck
# DATE: 6/6/2025
# CLASS: CS161
# Program Title: Junkworld
# Rename your .py file to: part1_<studentname>.py, replacing <studentname> with your name

############################################################################

# When you are ready to submit the completed code to Canvas...
# Test and run your code to make sure it works!
# Save your work.
# Download this codefile, and upload it to the Project Part One Canvas Assignment along with your documentation file


'''see below'''
#NOTE!!!!!!!!!!!!!!!!!!!!
#YOU WILL HAVE TO INSTALL THE PYFIGLET MODULE USING pip install pyfiglet

import time
import random
import pyfiglet
import textwrap


STARTINGHEALTH = 100
STARTINGPOWER = 3
STARTINGLUCK = 2
STARTINGSCRAP = 0

def welcome():
    print("Welcome to Junkworld, citizen.")
    input("Hit enter to continue...")

def gameinstructions():
    introtext = ("In this game, you're a lowly, young scavenger living on a junk strewn planet who has uncovered a forgotten and discarded drone. You must train your new friend through various methods so it can help you earn enough scrap to leave the planet.")
    wrapped_intro = textwrap.fill(introtext)
    print(wrapped_intro)
    print(end="\n")

    print("You have 10 days to reach 150 scrap in order to purchase passage and leave the planet. During each day, you are presented with 4 options:") 
    print("\n1. Search: \n  Scavenge safely (You will gain a low amount of scrap, but face no consequences.) \n2. Fight: \n  Search a dangerous area and fight for scrap. \n3. Tinker: \n   Train your drone, either increasing power or luck. Power affects your fighting chances, and luck affects gambling success... as well as possibly something else. \n4. Gamble: \n  Be careful with this, because you can easily lose it all. \n\nIf you do not reach the desired level of scrap, or your drone's health reaches zero, you lose the game. If you reach the desired scrap level before 10 days are up, you will win. Good luck!")
    print(end="\n")

def gamelore():
    print(end="\n")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    loretext = ("You are a citizen of Neo Flores, a remote dystopian planet, and a garbage dump for the rest of the planetary system. You work as a salvager, painstakingly roaming the dumps to hopefully find anything even slightly valuable. There’s a small but proud population in the solitary settlement, in the only valley with what sparse forest is left, completely surrounded by heaps of discarded junk hundreds of miles in every direction. You’re still young, with ideas of leaving and exploring, but unfortunately outside of the garbage ships staying in mid orbit to dump, there is only a supply shuttle that comes and goes once every year. Tickets don't exist, and the only way to leave is getting smuggled on by Ratz, the slightly shady owner of Static, a seedy bar across town. Securing passage takes a sizable bribe in the one currency people give a shit about, Scrap, able to be melted down and repurposed. One day, on the job, while walking the maze of metal that you call a home, you notice a peculiar faint red glow coming from underneath a rusty sheet of thin, ancient plexsteel. Lifting up the sheet, you uncover a relic of the past. Someone from a distant planet has discarded an early model of the sentient companion drones popular on the affluent inner planets. Normally recycled immediately upon their contract ending, it’s a mystery how this one slipped through, but you immediately grab it and put it in your frame pack. You’ve learned a little engineering from tinkering with the assorted devices you've found and stashed away, so you’re able to figure out what bits need adjusting and re-soldering, getting the little robot working. After getting it up and running, you realize it’s actually a fully fledged early prototype military drone with an ancient but effective search and location module. Suddenly, leaving seems very possible...")
    wrapped_lore = textwrap.fill(loretext)
    print(wrapped_lore)
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print(end="\n")



def playername():
    playername = input("What is your name? ")
    return playername

def petname():
    petname = input("What would you like to name your drone? ")
    print(end="\n")
    return petname


#this is a welcome message when the first day starts
def startingstatus(playername, petname):
    print(end="\n")
    print(f"Nice to see you again, {playername}.")
    print(f"Drone status: Online. Callsign: {petname}.")
    print("You have 10 days to complete the game. Good luck.")

#this will be sent at the start of each new day
def daystart(petname, currenthealth, currentpower, currentluck, currentscrap, days, scrap_log):
    print(f"A new day begins! You venture forth with {petname}.")
    print(f"{petname}'s current stats:")
    print(f"Health: {currenthealth}")
    print(f"PWR: {currentpower}")
    print(f"LUCK: {currentluck}")
    print(f"Current scrap level: {currentscrap}")
    if days > 1:
        print(f"You have {days} days left...")
    elif days == 1:
        print(f"You have {days} day left...")
    print(f"This is the current scrap log: {scrap_log}")

def maingame():
    days = 10
    currenthealth = STARTINGHEALTH
    currentpower = STARTINGPOWER
    currentluck = STARTINGLUCK
    currentscrap = STARTINGSCRAP
    
    scrap_log = []
        
    gamelore()
    yourname = playername()
    dronename = petname()
    startingstatus(yourname, dronename)
            
    print(end="\n")
    while days >= 1:
        if currenthealth <= 0:
            days = 0
                    
        elif currentscrap < 150:
            print(end="\n")
                    
            daystart(dronename, currenthealth, currentpower, currentluck, currentscrap, days, scrap_log)
            print(end="\n")
            currentscrap, currentpower, currentluck, currenthealth, scrap_log = chooseaction(dronename, currentscrap, currenthealth, currentpower, currentluck, scrap_log)
            
            days = days - 1
            print(end="\n")
                    
        elif currentscrap >= 150:
            days = 0
                

                
    if currenthealth <= 0:
        you_died = pyfiglet.figlet_format("DEATH...")
        print(you_died)
        print("Your drone died! Try again.")
        print(end="\n")
                    
    elif currentscrap < 150:
        game_over = pyfiglet.figlet_format("GAME OVER")
        print(game_over)
        print("You tried your best, but scrap isn't as abundant as it once was. You'll have to wait another year...")
        print(end="\n")
                
                    
    elif currentscrap >= 150:
        you_win = pyfiglet.figlet_format("YOU WIN!")
        print(you_win)
        win_text = ("The scrap is heavy in your pack, clinking softly with every step toward the bar. Static, the unlikely source of hope in this mess. Ratz eyes you, then the scrap, then nods. No words. Hours later, you crouch in the guts of a shuttle, your new friend hovering close with a soft whirr. You hear engines whining above. Your whole life shrinks through a grime-streaked port. Neo Flores disappears beneath clouds of orbital waste as you hurtle towards a new chapter...")
        wrapped_win = textwrap.fill(win_text)
        print(wrapped_win)
        print(end="\n")

def mainmenu():
    menuchoice = (input("MAIN MENU: \nPress 1 for game instructions \nPress 2 to start a new game. \nPress 0 to quit the game and end the program. \nPlease make a selection: "))
    print(end="\n")
    return menuchoice

#this is the main loop to increase drone power or gather scrap, day will increase by 1 at the end
def chooseaction(petname, currentscrap, currenthealth, currentpower, currentluck, scrap_log):
    print("What would you like to do today?")
    print(end="\n")
    print(f"1. Send {petname} off to search a relatively safe area outside of the city, known for reliable low quality scrap deposits.")
    print("2. Ratz told you about a spot down south where an old mil-spec research vessel that got caught by raiders and trashed got put down. The bugs down there are fierce, drawn by the faint currents still running through the ship's electrical. It's probably worth the risk though...")
    print(f"3. You’ve learned a little engineering from tinkering with the little devices you find stashed away, so with a little effort you can increase {petname}'s stats.")
    print("4. Back in the day, Ratz' bar used to be a haven for the old crowd which had a penchant for gambling. There's been a rumor that it's still active... maybe you could give it a shot?")
    print(end="\n")
    
    choice = input("Which action would you like to take? Please input a number: ")
    print(end="\n")
    
   
    
    if choice == "1":
        print(f"{petname} ventures forth, working dilligently and discovers a few piles of unremarkable scrap...")
        scrap_earned = 10
        currentscrap = currentscrap + scrap_earned
        scrap_log.append(scrap_earned)
        print("...")
        time.sleep(1)
        print(f"You find 10 scrap, increasing your scrap level to {currentscrap}!")
        print(end="\n")
        
    elif choice == "2":
        print(f"You make sure {petname} is in good shape and send it off to fight...")
        pwrcheck = random.randint(1, 9)
        pwrroll = random.randint(1, 9)
        #I decided to make the player check twice, if you fail your first check you can still try for a tiny scrap gain.
        ###print(f"This is the first power check: {pwrcheck}") ###########
        if currentpower < pwrcheck:
            if pwrroll >= 3:
                ###print(f"This is the roll to determine failure or success: {pwrroll}") ###############
                scrap_earned = 20
                currentscrap = currentscrap + scrap_earned
                scrap_log.append(scrap_earned)
                currenthealth = currenthealth - 15
            elif pwrroll < 3:
                ###print(f"This is the roll to determine failure or success: {pwrroll}") ##############
                print(f"{petname} tries to search for scrap but is driven off by a few lesser bugs and takes a small amount of damage")
                currenthealth = currenthealth - 15
        if currentpower >= pwrcheck:
            print(f"{petname} encounters a menacing group of bugs, but your training has paid off and beats them handily. A huge scrap cache is discovered, but {petname} takes a moderate amount of damage...")
            scrap_earned = 40
            currentscrap = currentscrap + scrap_earned
            scrap_log.append(scrap_earned)
            currenthealth = currenthealth - 30
        time.sleep(1)
        print("It comes back after a few hours, moving a little bit slower...")
        print(f"You now have {currentscrap} scrap, but {petname} took some damage and its health is decreased to {currenthealth}.")
        print(end="\n")
    
    elif choice == "3":
        print(f"You tinker with {petname} and figure out a way to increase it's capabilities... ")
        print("Would you like to increase:")
        print("a) PWR")
        print("b) LUCK")
        stat_choice = input("Enter a or b: ")
        print(end="\n")
    
        if stat_choice == "a":
            currentpower = currentpower + 1
            print(f"PWR increased by 1! Your PWR is now: {currentpower}.")
            print(end="\n")
        elif stat_choice == "b":
            currentluck = currentluck + 1
            print(f"LUCK increased by 1! Your LUCK is now: {currentluck}.")
            print(end="\n")
        else:
            print("Invalid input! You wasted an entire day fiddling with circuitry and accomplished absolutely nothing.")
            print(end="\n")
    
    elif choice == "4":
        print(f"Ratz doesn't advertise it, but he's willing to let anyone (or any drone...) gamble if they've got the right amount of scrap. Ratz motions back behind him, and {petname} follows you behind the bar.")
        print(end="\n")
        print("You look around and see a hooded figure beckoning to you. Walking up to it, you hear a slightly mechanical voice rasp, \"20 scrap if you lose. Put it down on the table.\"") 
        print(end="\n")
        print(f"You put the scrap down and the ancient attendant springs into action, hooking a couple diodes up to {petname} in the appropriate ports and pulling a lever. After a brief delay you hear the sound of a pre-war processor groaning, accompanied by some protesting beeps. A word flashes on the terminal screen, and you lean over to look...")
        print(end="\n")
        
        
        time.sleep(1)
        print("...")
        time.sleep(1)
        roll = random.randint(1, 10)
        
        if currentluck < roll:
            scrap_earned = -20
            currentscrap = currentscrap + scrap_earned
            scrap_log.append(scrap_earned)
            print(f"It reads LOSE. You shake your head and walk back upstairs, your scrap now sitting at {currentscrap}.  Well, there's always tomorrow...")
            print(end="\n")
        elif currentluck > roll and currentluck != roll:
            scrap_earned = 30
            currentscrap = currentscrap + scrap_earned
            scrap_log.append(scrap_earned)
            print(f"You catch a glimpse of WIN on the little LED screen and grin. The biodrone shakes it's head and adds the scrap to your total, which now sits at {currentscrap}")
            print(end="\n")
        elif currentluck == roll:
            scrap_earned = 50
            currentscrap = currentscrap + scrap_earned
            scrap_log.append(scrap_earned)
            currentluck = currentluck + 1
            print(f"JCKPT lights up and the machine starts whirring loudly. A barely functional speaker starts emitting a buzz that maybe once could have been some congratulatory sounds. A huge scrap cache hits your inventory, now sitting at {currentscrap}. You hear the ancient gambling attendant grumble, \"Keep those diodes on... looks like you won a little upgrade to your luck too.\"")
            print("Your LUCK increases by 1!")
            print(end="\n")
            
    currentscrap = lucky_bonus(scrap_log, currentluck)
    
    input("Hit enter to continue...")
    print(end="\n")
    return currentscrap, currentpower, currentluck, currenthealth, scrap_log

def lucky_bonus(scrap_log, currentluck):
    
    bonus_amount = 30
    
    if len(scrap_log) > 0:
        roll = random.randint(1, 10)

        if currentluck > roll:
            lowest_index = 0
            index = 1
            while index < len(scrap_log):
                if scrap_log[index] < scrap_log[lowest_index]:
                    lowest_index = index
                index = index + 1
                
            old_value = scrap_log[lowest_index]
            
            if old_value < bonus_amount:
                scrap_log[lowest_index] = bonus_amount
                print(f"Walking home, a tiny glint catches your eye and you bend down to inspect it. Dusting it off, it appears to be an incredibly valuable relic that a traveling merchant must have dropped... \nI bet you could pay off some debt with this. \n[Lucky! Your lowest scrap value ({old_value}) was replaced with {bonus_amount}!]")
                print(f"Updated scrap log: {scrap_log}")
                print(end="\n")
            else:
                print("You had a lucky feeling, but I guess it wasn't lucky enough...")
        else:
            print("You feel the hint of an auspicious wind start blowing, but nothing seems to happen... Odd...")
            print(end="\n")

    total_scrap = 0
    index = 0
    while index < len(scrap_log):
        total_scrap = total_scrap + scrap_log[index]
        index = index + 1

    return total_scrap
    

def main():

    gametitle = pyfiglet.figlet_format("JUNKWORLD")
    print(gametitle)
    
    welcome()
    print(end="\n")
   
    menuchoice = mainmenu()

    while menuchoice != "0":
        if menuchoice == "1":
            instructions = pyfiglet.figlet_format("INSTRUCTIONS")
            print(instructions)
            gameinstructions()
            menuchoice = mainmenu()
    
        elif menuchoice == "2":
            print(end="\n")
            maingame()
            menuchoice = mainmenu()
                       
        else:
            print("Sorry that wasn't a valid selection!")
            menuchoice = mainmenu()

    if menuchoice == "0":
        print ("Thank you for playing! The program will terminate now. Goodbye.")
main()