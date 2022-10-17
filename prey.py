import random

class Prey:
    def __init__(self, start = random.randint(0,49)):
        self.curr_pos = start

    def move(self, arena):
        list_to_choose_from = arena[self.curr_pos]
        list_to_choose_from.append(self.curr_pos)
        self.curr_pos = random.choice(list_to_choose_from)

class Predator:
    pass