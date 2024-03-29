from enum import IntEnum

class color_wheel():
    def __init__(self):
        self.val = {}
        self.val["RESET"]           = "\033[0m"
        self.val["BLACK"]           = "\033[0;30m"
        self.val["RED"]             = "\033[0;31m"
        self.val["GREEN"]           = "\033[0;32m"
        self.val["YELLOW"]          = "\033[0;33m"
        self.val["BLUE"]            = "\033[0;34m"
        self.val["PURPLE"]          = "\033[0;35m"
        self.val["CYAN"]            = "\033[0;36m"
        self.val["WHITE"]           = "\033[0;37m"
        self.val["GRAY"]            = "\033[0;38m"
        self.val["DARK_GRAY"]       = "\033[1;30m"
        self.val["BOLD_RED"]        = "\033[1;31m"
        self.val["BOLD_GREEN"]      = "\033[1;32m"
        self.val["BOLD_YELLOW"]     = "\033[1;33m"
        self.val["BOLD_BLUE"]       = "\033[1;34m"
        self.val["BOLD_PURPLE"]     = "\033[1;35m"
        self.val["BOLD_CYAN"]       = "\033[1;36m"
        self.val["BOLD_WHITE"]      = "\033[1;37m"
        self.val["BOLD_GRAY"]       = "\033[1;38m"

# ENUMS
class DOOR_STATUS(IntEnum):
    # Wall
    NonExistent = 0
    # Passable doors
    P_NewDoor = 1
    P_KnownDoor = 2 
    # Unopenable doors
    U_NoDoorHandle = -1
    U_CollapsedDoor = -2
    # Barricaded doors
    B_LockedDoor = -100
    B_BreakableDoor = -200
    
class RNG(IntEnum):
    Random_Room_Spawn = 40      # The chances of a new door to spawn
    Entrance_Lock = 20          # The chances that you cannot head back the way you came from
    Suddenly_Secret_Door = 50   # The chances that a door that should lead to another room is locked from this side


# Create all global variables, should be called only once
def create_globals():
    global CH_ABS_ROOM_NUM, CH_LOCATIONS, CH_OPENINGS, CH_CUR_LOCATION
    global DIRECTIONS
    CH_ABS_ROOM_NUM = 0
    CH_LOCATIONS = {}
    CH_OPENINGS = 0
    CH_CUR_LOCATION = (0,0,0)

    DIRECTIONS = ["North", "East", "South", "West", "Up", "Down"]

# Reset all global variables (used for a New Game)
def reset_globals():
    global CH_ABS_ROOM_NUM, CH_LOCATIONS, CH_OPENINGS, CH_CUR_LOCATION
    CH_ABS_ROOM_NUM= 0
    CH_LOCATIONS = {}  
    CH_OPENINGS = 0
    CH_CUR_LOCATION = (0,0,0)


# PROGRAM INFO
TITLE = "Averkorf Dungeon"
CREATOR = "George"
PLATFORM = "Python 3"
