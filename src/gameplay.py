from datetime import datetime

class Gameplay():
    def __init__(self):
        self.name = "Adventure Cave"

    def msg(self, player):
        mnth = datetime.now().month

        if player.location.name == "Outside Cave Entrance":
            if mnth >= 3 and mnth < 6:
                # spring
                print(f"{player.name}, why dont you come inside and make yourself at home. We've just began a bit of spring cleaning")

            if mnth >= 6 and mnth < 9:
                # summer
                print(f"its pretty hot out today {player.name}, why dont you come inside and make yourself at home.")

            if mnth >= 9 and mnth < 12:
                # Autumn
                print(f"{player.name}, why dont you come inside and make yourself at home. I've got a fresh pot of pumpkin spice coffee brewing just for you")

            if mnth == 12 and mnth < 3:
                # winter
                print(f"its pretty cold out {player.name}, why dont you come inside and make yourself at home.")


    def respond(self, player, location, res):
        if location == "Outside Cave Entrance" and res == 'n':
            return player.location.n_to
        elif location == "Foyer" and res == 'n':
            return player.location.n_to
        elif location == "Foyer" and res == 'ne':
            return player.location.ne_to
        elif location == "Foyer" and res == 'e':
            return player.location.e_to
        elif location == "Foyer" and res == 's':
            return player.location.s_to


