from room import Room
from player import Player
from gameplay import Gameplay
from key import Key


# Declare all the rooms

room = {
    "outside":  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    "foyer":    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    "northeast stairwell":    Room("Golden NE Stairwell", """To the right, four photographs hang along the wall.
The first photo reads "VI", second reads "II", the third reads "CC", and the fourth photo reads "Backwards from whence thee came." """),

    "northwest stairwell":    Room("Black NW Stairwell", """" Animals hang mounted on the wall to the left of the stairwell.
I must be careful in this old building, the Third step is missing. """),

    "overlook": Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    "narrow":   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    "treasure": Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers 😫. The only exit is to the south."""),
}

keys=[Key("Car"),
Key("Window"),
Key("Shed"),
Key("Treasure"),
Key("Laundry"),
Key("Closet"),
Key("Chimney")]




gameplay = Gameplay(4)
player = Player("joshua", 'm',room["outside"],100)


# Link rooms together

room["outside"].n_to = room["foyer"]
room["foyer"].s_to = room["outside"]
room["foyer"].n_to = room["overlook"]
room["foyer"].ne_to = room["northeast stairwell"]
room["foyer"].nw_to = room["northwest stairwell"]
room["foyer"].e_to = room["narrow"]
room["foyer"].se_to = room["foyer"]
room["overlook"].s_to = room["foyer"]
room["northeast stairwell"].sw_to = room["foyer"]
room["narrow"].w_to = room["foyer"]
room["narrow"].n_to = room["treasure"]
room["treasure"].s_to = room["narrow"]

#
# Main
#


# Make a new player object that is currently in the 'outside' room.
# Write a loop that:
gameplay.info()
while True:
    gameplay.msg(player)
    print(player.location)
    res = input(">")
    player.location = gameplay.respond(player, player.location.name, res)

    # player.location = player.location.n_to
    # global res
    # if player.location == room["outside"] and res == 'n':
    #     player.location = player.location.n_to
    #     print(f"its pretty cold out {player.name}, why dont you come inside and make yourself at home.")
    # elif player.location == room["outside"] and res != 'q' and res !='n':
    #     input("invalid response. Try again.")

    # if player.location == room["foyer"]:
    #     info()
    #     print(player.location)
    #     res = input(f"Welcome!\nFeel free we take a look around. ")
    # elif player.location == room["foyer"] and res != 'q' and res !='n' and res !='ne':
    #     input("invalid response. Try again.")
    # # elif player.location == room["outside"] and res == 'q':
    # #     print("Thanks for stopping by, hope to see you soon")
    # #     break
    # elif player.location == room["outside"] and res != 'q' and res !='n':
    #     input("invalid response. Try again.")

    # if res == 'q':
    #     print("Thanks for stopping by, hope to see you soon.")
    #     break
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
