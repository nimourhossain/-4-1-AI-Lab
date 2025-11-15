import random

class Environment:
    def __init__(self):
        self.rooms = {'A': random.choice(['clean','dirty']),
                      'B': random.choice(['clean','dirty'])}
        self.agent_location = random.choice(['A','B'])

    def is_dirty(self,location):
        return self.rooms[location]=='dirty' 


    def clean(self,location):
        self.rooms[location]=='clean'

    def move(self,new_location):
        self.agent_location=new_location

    def randomly_dirty_rooms(self, probability = 0.3):
        for room in self.rooms:
            if self.rooms[room]=='clean' and random.random()<probability:
               self.rooms[room]='dirty'
               print(f"Environment: Room {room} got dirty again")

    def display(self):
        print()           


