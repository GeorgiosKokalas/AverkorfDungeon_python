import os,sys

# Before Importing, we set the workign directory to be that of the script
# Then append the Code folder into our path
os.chdir(os.path.dirname(os.path.realpath(__file__)))
sys.path.append("./Code/")

# Import what we need from the Code section
from Code.global_vars import *
import Code.Class_Room as Room
from Code.interface import run_interface
import Code.Class_Option as Option


def print_txt(fileName):
    fileName = "./txt_folder/" + fileName + ".txt"
    file = open(fileName, "r")
    print(file.read())
    file.close()

def screen_clear():
    # for windows
    if os.name == 'nt':
        os.system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        os.system('clear')
      
        
def print_locations():
    global LOCATIONS

    message = 'You wip out your catalogous to see these locations: \n'
    counter = 0
    for i in LOCATIONS.val.keys():
        message += f"Room {LOCATIONS.val[i].roomNum} is at {i} \t"
        counter += 1
        if counter == 7:
            counter = 0
            message += '\n'
    print(message)


def GAME_change_room(DoorChoice):
    global LOCATIONS, CURRENT_LOCATION
    CURRENT_LOCATION.val = LOCATIONS.val[CURRENT_LOCATION.val].go_to(DoorChoice)


def GAME_explore_room() -> Option.Option:
    global OPENINGS, LOCATIONS, ABSOLUTE_ROOM_NUM, CURRENT_LOCATION, DIRECTIONS
    if CURRENT_LOCATION.val not in LOCATIONS.val:
        ABSOLUTE_ROOM_NUM.val += 1
        LOCATIONS.val[CURRENT_LOCATION.val] = Room.Room(-1, ABSOLUTE_ROOM_NUM.val, CURRENT_LOCATION.val)
    room = LOCATIONS.val[CURRENT_LOCATION.val]
    room.update()

    optionsList = [ Option.Option("Check the room", -1, "check_room") ]
    for doorIdx in range(len(DIRECTIONS)):
        if room.doors[doorIdx] > 0:
            optionsList.append(Option.Option("Move " + DIRECTIONS[doorIdx], doorIdx, "change_room"))
    
    return run_interface(optionsList, AsciiArt=0, StatusText=str(room),TxtPointer=False)

        

def GAME_event_manager(CurrentEvent = "explore_room") -> Option.Option:
    match str(CurrentEvent):
        case "explore_room":
            return GAME_explore_room()


### GAME INTRO FUNCTION
# ---------------------
# FUNCTION used to display the intro bit by bit
def INTRO_game_intro(Stage = 1) -> Option.Option:
    asciiArt = "INTRO_Pic" + str(Stage)
    statusText = "INTRO_Part" + str(Stage)
    optionsList = []
    if Stage < 4:
        optionsList = [ Option.Option("Continue", Stage+1, "intro_continue"), \
                        Option.Option("Skip", -1, "intro_skip")]
    else:
        optionsList = [ Option.Option("Continue", -1, "intro_skip") ]
    return run_interface(optionsList,AsciiArt=asciiArt,StatusText=statusText)


### MAIN MENU FUNCTIONS
# ----------------------
# FUNCTION used to set up information pages for the user
def MM_info_generic(Variant = "game_info") -> Option.Option:
    # These should differ per information page
    optionNames, optionCommand, statusText = [], [], ""
    
    # match the variables for each game 
    match Variant.lower():
        case "game_info":
            optionNames = ["See build history"]
            optionCommand = ["build_info"]
            statusText = "MM_GameInfo"
        case "build_info":
            optionNames = ["See game information"]
            optionCommand = ["game_info"]
            statusText = "MM_BuildInfo"
        case _:
            print("Variant of information site is unknown, assuming game_info")
            return MM_info_generic("game_info")

    # If for some reason we do not have equal list lengths, options cannot be created
    if len(optionCommand) != len(optionNames):
        raise IndexError("optionCommand and optionNames are supposed to have equal lengths for button creation")
    
    # Create options lists
    optionsList = [Option.Option(optionNames[idx], -1, optionCommand[idx]) for idx in range(len(optionCommand))]
    optionsList.append(Option.Option("Back to Main Menu", -1, "main_menu"))
    optionsList.append(Option.Option("Quit", -1, "quit"))

    return run_interface(optionsList,AsciiArt="MM_Title",StatusText=statusText)


# FUNCTION MAIN MENU
def main_menu() -> Option.Option:
    playOption = Option.Option("New Game", 1, "new_game")
    loadOption = Option.Option("Load Game", -1, "load_game")
    infoOption = Option.Option("Info", -1, "game_info")
    quitOption = Option.Option("Quit", -1, "quit")
    optionsList = [playOption, loadOption, infoOption, quitOption]
    
    return run_interface(optionsList, "MM_Title")


# MAIN
# ----
# The main command serves as the main hub for all button clicks
def main():
    takenOption = main_menu()
    while True:
        match takenOption.command.lower():
            # MAIN MENU ITEMS
            case "main_menu":
                takenOption = main_menu()
            case "new_game":
                reset_global_vars()
                takenOption = INTRO_game_intro()
            case "load_game":
                break
            case "game_info":
                takenOption = MM_info_generic("game_info")
            case "build_info":
                takenOption = MM_info_generic("build_info")
            case "quit":
                quit()
            
            # INTRO ITEMS
            case "intro_continue":
                takenOption = INTRO_game_intro(takenOption.id)
            case "intro_skip":
                takenOption = GAME_event_manager("explore_room")

            ## GAMEPLAY
            case "change_room":
                GAME_change_room(takenOption.id)
                takenOption = GAME_event_manager("explore_room")

            # FALLBACK
            case _:
                raise ValueError("Command not understood. Deciding to crash...")
            
            

if __name__ == "__main__":
    main()