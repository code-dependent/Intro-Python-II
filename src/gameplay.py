from datetime import datetime
import calendar
import sys

class Gameplay():
    def __init__(self, tkey):
        self.name = "Adventure Cave"
        self.date = datetime.now()
        self.tkey = []

    def info(self):
        print("******************** INSTRUCTIONS📄********************\n")
        print("""N = Move North ↑,\nNW = Move Northwest ↖\nW = Move West ←\nSW = Move Southwest ↙\nS = Move South ↓\nSE = Move Southeast ↘\nE = Move East →\nNE = Move Northeast ↗\nQ = Quit Game 🛑\n""")
        print("******************* ⬆️INSTRUCTIONS⬆️ *******************\n")

    def msg(self, player):

        if player.location.name == "Outside Cave Entrance":
            if self.date.month >= 3 and self.date.month < 6:
                # spring
                print(f"{player.name}, why dont you come inside and make yourself at home. We've just began a bit of spring cleaning\n")

            if self.date.month >= 6 and self.date.month < 9:
                # summer
                print(f"its pretty hot out today {player.name}, why dont you come inside and make yourself at home.\n")

            if self.date.month >= 9 and self.date.month < 12:
                # Autumn
                print(f"{player.name}, why dont you come inside and make yourself at home. I've got a fresh pot of pumpkin spice coffee brewing just for you\n")

            if self.date.month == 12 and self.date.month < 3:
                # winter
                print(f"its pretty cold out {player.name}, why dont you come inside and make yourself at home.\n")
        # if msgcode != "null":
        #     if msgcode == "fsec":
        #         if self.date.day < 7:
        #             print(self.date.day)

        #         if self.date.day > 7:
        #             print(self.date.day)
        #         if self.date.day == 7:
        #             print(self.date.day)


    def respond(self, player, location, res):
        if location == "Outside Cave Entrance" and res == 'n':
            return player.location.n_to
        elif location == "Foyer" and res == 'n':
            return player.location.n_to
        elif location == "Foyer" and res == 'ne':
            return player.location.ne_to
        elif location == "Foyer" and res == 'nw':
            return player.location.nw_to
        elif location == "Foyer" and res == 'e':
            return player.location.e_to
        elif location == "Foyer" and res == 'se':
            if self.date.day < 7:
                dif = 7 - self.date.day
                print(f"{player.name}, looks at the calender:\n{calendar.TextCalendar().prmonth(self.date.year,self.date.month)}\n'Looks like the shepard is hosting a party in the ballroom in {dif} day(s).\nMaybe I will stop by.'\n")
            elif self.date.day > 7:
                dif = self.date.day - 7
                print(f"{player.name}, looks at the calender:\n{calendar.TextCalendar().prmonth(self.date.year,self.date.month)}\n'Looks like I just missed the shepard's monthly ballroom event {dif} day(s) ago..\nI suppose I will have to try for next month on the 7th.'\n")
            elif self.date.day == 7 and self.date.month != 3:
                print(f"{player.name}, looks at the calender:\n{calendar.TextCalendar().prmonth(self.date.year,self.date.month)}\n'Looks like the shepard is hosting a party tonight in the ballroom.\nPerhaps I'll drop by.'\n")
            elif self.date.day == 7 and self.date.month == 3:
                print(f"{player.name}, looks at the calender:\n{calendar.TextCalendar().prmonth(self.date.year,self.date.month)}\n'Looks like I made it just in time for the shepard's Grand Festival in the Overlook room.\nPerhaps I will invite a guest to join me.'\n")
        elif location == "Foyer" and res == 's':
            return player.location.s_to
        elif location == "Foyer" and res == 'sw':
            print("""+-------------------------------------+
|                                     |
|  🗝    🔑    🗝    🗝    🔑    🔑    🔑|
|                                     |
+-------------------------------------+\nLooks like a key holder with 7 keys attatched.\n""")
        elif location == "Golden NE Stairwell" and res == 'sw':
            return player.location.sw_to
        elif location == "Black NW Stairwell" and res == 's':
            return player.location.s_to
        elif location == "Narrow Passage" and res == 'w':
            return player.location.w_to
        elif location == "Narrow Passage" and res == 'n':
            print("The door is locked. I wonder if I can find a way in.")
            res2 = input("Enter a space seperated code: ")
            res2 = res2.split()
            if res2 == tpword and tkey in player.keys:
                print("I DID IT!🎊🎉💎🌹💍")
                return player.location.n_to
            else:
                print("🚫ACCESS DENIED🚫")
        else:
            print("Invalid Response")
        if res == 'q':
            res2 = input("End the game\nare you sure?(y/n)")
            if res2 == 'y' or res2 == "yes":
                print(f"fairwell {player.name},\nHope we meet again soon.🚪")
                sys.exit(1)
        return player.location


