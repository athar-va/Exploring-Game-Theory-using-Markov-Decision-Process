import random
from collections import deque
from copy import deepcopy

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

    
    def move(self, agent_pos, arena):
        """
        Randomly chooses between the neighbours having the shortest path to the agent

        Parameters:
        self
        arena (dict): The arena used currently
        agent_pos (int): Position of the agent
        """

        predator_neighbour_path_length = {}

        # Finds the length for the shortest path for each of predators neighbours
        for i in arena[self.curr_pos]:
            path, path_length = utils.get_shortest_path(i, agent_pos, arena)
            predator_neighbour_path_length[i] = path_length

        # Finds all the neighbours that have minimum path length
        min_length = min(predator_neighbour_path_length.values())
        neighbours_with_min_path_length = [key for key, value in predator_neighbour_path_length.items() if
                                           value == min_length]

        # Chooses randomly between the neighbours
        self.curr_pos = random.choice(neighbours_with_min_path_length)

    def distracted_move(self, agent_pos, arena):
        """
        Randomly chooses between the neighbours having the shortest path to the agent

        Parameters:
        self
        arena (dict): The arena used currently
        agent_pos (int): Position of the agent
        """

        if random.random() <= 0.6:
            predator_distracted = False
        else:
            predator_distracted = True
        if predator_distracted:
            list_to_choose_from = deepcopy(arena[self.curr_pos])
            self.curr_pos = random.choice(list_to_choose_from)
        else:        
            predator_neighbour_path_length = {}

            # Finds the length for the shortest path for each of predators neighbours
            for i in arena[self.curr_pos]:
                path, path_length = utils.get_shortest_path(i, agent_pos, arena)
                predator_neighbour_path_length[i] = path_length

            # Finds all the neighbours that have minimum path length
            min_length = min(predator_neighbour_path_length.values())
            neighbours_with_min_path_length = [key for key, value in predator_neighbour_path_length.items() if
                                            value == min_length]

            # Chooses randomly between the neighbours
            self.curr_pos = random.choice(neighbours_with_min_path_length)

    def move_with_rand_selection(self, agent_pos, arena):
        """
                Finds the shortest path to the agent and then takes a step towards it

                Parameters:
                self
                arena (dict): The arena used currently
                agent_pos (int): Position of the agent
        """
        predator_neighbour_path_length = {}

        # Finds the length for the shortest path for each of predators neighbours
        for i in arena[self.curr_pos]:
            path, path_length = utils.get_shortest_path(i, agent_pos, arena)
            predator_neighbour_path_length[i] = path_length

        # Finds all the neighbours that have minimum path length
        min_length = min(predator_neighbour_path_length.values())
        neighbours_with_min_path_length = [key for key, value in predator_neighbour_path_length.items() if value == min_length ]

        # Chooses randomly between the neighbours
        self.curr_pos = random.choice(neighbours_with_min_path_length)

