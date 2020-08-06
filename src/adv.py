from room import Room
from player import Player
from gameplay import Gameplay

# Declare all the rooms

room = {
    "outside":  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    "foyer":    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    "northeast stairwell":    Room("NE Stairwell", """To the right, four photographs hang along the wall.
The first photo reads "VI", second reads "II", the third reads "CC", and the fourth photo reads "Backwards from whence thee came." """),

    "overlook": Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    "narrow":   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    "treasure": Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}
gameplay = Gameplay()


# Link rooms together

room["outside"].n_to = room["foyer"]
room["foyer"].s_to = room["outside"]
room["foyer"].n_to = room["overlook"]
room["foyer"].ne_to = room["northeast stairwell"]
room["foyer"].e_to = room["narrow"]
room["overlook"].s_to = room["foyer"]
room["narrow"].w_to = room["foyer"]
room["narrow"].n_to = room["treasure"]
room["treasure"].s_to = room["narrow"]

#
# Main
#
def info():
    print("******************** INSTRUCTIONS📄********************")
    print("""N = Move North ↑,\nNW = Move Northwest ↖,\nW = Move West ←,\nSW = Move Southwest ↙,\nS = Move South ↓,\nSE = Move Southeast ↘,\nE = Move East →,\nNE = Move Northeast ↗,\nQ = Quit Game 🛑""")
    print("******************* ⬆️INSTRUCTIONS⬆️ *******************")

# Make a new player object that is currently in the 'outside' room.
player = Player("joshua", 'm',room["outside"],100)
# Write a loop that:

while True:

    print(player.location)
    gameplay.msg(player)
    res = input(">").lower()
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
