import random
from copy import deepcopy

class Prey:
    def __init__(self, start = random.randint(0,49)):
        """
        Initializing the position of the prey

        Parameters:
        self
        start: A random integer denoting a node in the arena
        """
        
        self.curr_pos = start

    def move(self, arena):
        """
        Method to move the prey

        Parameters:
        self
        arena: The arena used currently
        """


        list_to_choose_from = deepcopy(arena[self.curr_pos])
        list_to_choose_from.append(self.curr_pos)
        self.curr_pos = random.choice(list_to_choose_from)
