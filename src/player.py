# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self,name,gender,location,healthpts):
        self.name = name
        self.gender = gender
        self.location = location
        self.healthpts = healthpts
        self.keys = set()