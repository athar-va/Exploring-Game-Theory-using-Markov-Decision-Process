import random
from collections import deque

import utils

class Predator:
    def __init__(self, start = random.randint(0,49)):
        """
        Initializing the position of the predator

        Parameters:
        self
        start (int): A random integer denoting a node in the arena
        """
        self.curr_pos = start
        print(f'predator initialized with {self.curr_pos}')
    
    def move(self, agent_pos, arena):
        """
        Finds the shortest path to the agent and then takes a step towards it

        Parameters:
        self
        arena (dict): The arena used currently
        agent_pos (int): Position of the agent
        """
        print('moving predator')
        path, path_length = utils.get_shortest_path(self.curr_pos, agent_pos, arena)
        print(path)
        self.curr_pos = path.popleft()

