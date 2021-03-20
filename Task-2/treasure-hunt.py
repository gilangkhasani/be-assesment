# This is a treasure hunt game.
#
# The world is a grid (defined by GRID_SIZE).  The player starts in position (1,1).
# A monster is randomly positioned within the world, along with a number of
# treasures.  The player must find all treasures without getting eaten by the
# monster.
#
# The player is warned when they are near the monster, which should help them evade it.
#
# The player can use the commands L, R, U, and D to move.  They can quit the game with the
# Q command.


import random

#
# This class defines a location within the game grid.  It has both an X- and Y- coordinate.
class Point:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def to_string(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"

    def is_equal_to(self, pt):
        if (pt == None):
            return False

        if (self.x == pt.x and self.y == pt.y):
            return True

        return False

GRID_SIZE = 6

treasures = ['$']
treasure_locations = []
obstacle_locations = []
obstacles = [
    Point(2, 2),
    Point(2, 3),
    Point(2, 4),
    Point(3, 4),
    Point(3, 6),
    Point(4, 2),
]
player_location = Point(4, 1)

# Initialize a new game
def init_game():
    global player_location
    global treasure_locations
    global obstacle_locations

    # Position the player in the top left corner of the grid (1,1)
    player_location = Point(4, 1)
    occupied_locations = [player_location]

    # Choose a random location for the monster, excluding the player's location
    for i in range(0, len(obstacles)):
        obstacle_locations.append(obstacles[i])
        occupied_locations.append(obstacles[i])

    # Randomly locate each of the treasures in unoccupied spaces
    for i in range(0, len(treasures)):
        treasure_locations.append(choose_unoccupied_location(occupied_locations))

# Find a point within a list and return its position, or -1 if not found
def find_point(list, pt):
    for i in range(0, len(list)):
        if (list[i].is_equal_to(pt)):
            return i

    return -1

# Choose a random unoccupied position within a list of used locations.  The new location is added to the
# list, and the new location is returned.
def choose_unoccupied_location(used_locations):
    while True:
        location = Point(random.randint(1, GRID_SIZE), random.randint(1, GRID_SIZE))

        if (find_point(used_locations, location) < 0):
            used_locations.append(location)
            return location

# Handle the player entering a new location in the game
def enter_location(location):
    global player_location

    player_location = location

    print("You are now in location " + player_location.to_string())

    # Determine if any treasure is in the location
    treasure = find_point(treasure_locations, player_location)

    if (treasure >= 0):
        print("You found the " + treasures[treasure])
        return False
    
    return True

# Process a command from the player
def process_command(command):
    command = command.lower()

    if (command == ""):
        print("What??")
        return True

    if (command == "q"):
        return False

    new_location = None

    # Handle a possible movement command
    if (command == "a"): #Up/North
        if (player_location.x > 1):
            new_location = Point(player_location.x - 1, player_location.y)
    elif (command == "c"): #Down/South
        if (player_location.x < GRID_SIZE):
            new_location = Point(player_location.x + 1, player_location.y)
    elif (command == "d"): #West/Left
        if (player_location.y > 1):
            new_location = Point(player_location.x, player_location.y - 1)
    elif (command == "b"): #East/Right
        if (player_location.y < GRID_SIZE):
            new_location = Point(player_location.x, player_location.y + 1)
    else:
        print("No Command")
        return True

    obstacle = find_point(obstacle_locations, new_location)
    if (obstacle >= 0):
        new_location = None

    if (new_location == None):
        print("You can't move in that direction")
        return True

    return enter_location(new_location)

# Implement the game loop, which repeats until the game is over.
def game_loop():
    game_active = enter_location(player_location)

    while game_active == True:
        print("\nWhat do you want to do? ")
        option = input()

        game_active = process_command(option)

# Initialize the gamer
init_game()
game_loop()