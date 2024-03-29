import random
from pprint import pprint
import config
import utils
from prey import Prey
from predator import Predator


class Agent_1:

    def __init__(self, prey_loc, predator_loc):
        """
        Initializing the position of the Agent at locations where prey and predator are not present

        Parameters:
        self
        prey_loc (int): Location of the prey
        predator_loc (int): Location of the predator
        """

        # Handling condition where prey and predator are spawned on the same location
        list_to_choose_from = list(range(50))
        if prey_loc == predator_loc:
            list_to_choose_from.remove(prey_loc)
        else:
             list_to_choose_from.remove(prey_loc)
             list_to_choose_from.remove(predator_loc)

        self.curr_pos = random.choice(list_to_choose_from)

    def move(self, arena, prey_loc, predator_loc):
        """
        Moves Agent 1 according to the given priority

        Parameters:
        self
        arena (dictionary): Adjacency list representing the graph
        prey_loc (int): Location of prey
        predator_loc (int): Location of Predator
        """
        """
        print("Initial pos",self.curr_pos)
        # Neighbours of the current node are extracted here
        self.neighbours = arena[self.curr_pos].copy()

        # Distances from prey and predator will be stored in the following dicts
        predator_dist = {}
        prey_dist = {}

        # Storing the distances of the agent location to the prey and predator
        path, curr_pos_prey_dist = utils.get_shortest_path(self.curr_pos, prey_loc, arena)
        path, curr_pos_predator_dist = utils.get_shortest_path(self.curr_pos, predator_loc, arena)

        # Find distance from all neighbours to the prey and the predator
        for i in self.neighbours:
            path, prey_dist[i] = utils.get_shortest_path(i, prey_loc, arena)
            path, predator_dist[i] = utils.get_shortest_path(i, predator_loc, arena)

       # Defining subsets of nodes
        closer_to_prey = {}
        not_farther_from_prey = {}
        farther_from_predator = {}
        not_closer_to_predator = {}


        # Adding nodes to the subsets
        for k in prey_dist.keys():
            if prey_dist[k] < curr_pos_prey_dist:
                closer_to_prey[k]=prey_dist[k]

        for k in prey_dist.keys():
            if prey_dist[k] == curr_pos_prey_dist:
                not_farther_from_prey[k]=prey_dist[k]

        for k in predator_dist.keys():
            if predator_dist[k] >= curr_pos_predator_dist:
                farther_from_predator[k]=predator_dist[k]

        for k in predator_dist.keys():
            if predator_dist[k] == curr_pos_predator_dist:
                farther_from_predator[k]=predator_dist[k]


        # Assigning the position accorinding to the given priorrity
        if len(set(closer_to_prey).intersection(set(farther_from_predator))) != 0:
            self.curr_pos=min(closer_to_prey, key=closer_to_prey.get)
            #print("priority 1")

        elif len(set(closer_to_prey).intersection(set(not_closer_to_predator))) !=0:
            self.curr_pos=min(closer_to_prey, key=closer_to_prey.get)
            #print("priority 2")

        elif len(set(not_farther_from_prey).intersection(set(farther_from_predator))) !=0:
            self.curr_pos=min(not_farther_from_prey, key=not_farther_from_prey.get)
            #print("priority 3")

        elif len(set(closer_to_prey).intersection(set(not_closer_to_predator))) !=0:
            self.curr_pos=min(closer_to_prey, key=closer_to_prey.get)
            #print("priority 4")

        elif len(farther_from_predator) !=0:
            self.curr_pos=max(farther_from_predator, key=farther_from_predator.get)
            #print("priority 5")

        elif len(not_closer_to_predator) != 0:
            self.curr_pos=min(not_closer_to_predator, key=not_closer_to_predator.get)
            #print("priority 6")

        else:
            pass
            #print("Sitting and Praying")

        #print(curr_pos_prey_dist,curr_pos_predator_dist)

        print("Current pos" , self.curr_pos)
        """

        pos = utils.best_node(arena, self.curr_pos, prey_loc, predator_loc)

        # Handling Sitting and praying case
        if pos == 999:
            pass
        else:
            self.curr_pos = pos

    def begin(arena):
        """
        Creates all the maze objects and plays number of games and collects data

        Parameters:
        arena (dict): Arena to use

        Returns:
        data_row (list): Results evaluated for the agent
        """

        # Initiating game variables
        game_count = 0
        step_count = 0

        # Initiating variables for analysis
        win_count = 0
        loss_count = 0
        forced_termination = 0
        # data = []
        data_row = []


        # Config variable (To be transferred to a parameter file)
        number_of_games = config.NUMBER_OF_GAMES
        forced_termination_threshold = config.FORCED_TERMINATION_THRESHOLD

        while game_count < number_of_games:
            # Creating objects
            prey = Prey()
            predator = Predator()
            agent1 = Agent_1(prey.curr_pos, predator.curr_pos)

            step_count = 0

            while 1:
                print("In game Agent_1 at game_count: ", game_count, " step_count: ", step_count)
                print(agent1.curr_pos, prey.curr_pos, predator.curr_pos)
                agent1.move(arena, prey.curr_pos, predator.curr_pos)

                # Checking termination states
                if agent1.curr_pos == prey.curr_pos:
                    win_count += 1
                    break
                elif agent1.curr_pos == predator.curr_pos:
                    loss_count += 1
                    break

                prey.move(arena)

                # Checking termination states
                if agent1.curr_pos == prey.curr_pos:
                    win_count += 1
                    break

                predator.move(agent1.curr_pos, arena)

                # Checking termination states
                if agent1.curr_pos == predator.curr_pos:
                    loss_count += 1
                    break

                step_count += 1

                # Forcing termination
                if step_count >= forced_termination_threshold:
                    forced_termination += 1
                    break

            game_count += 1

        data_row = ["Agent_1", win_count * 100 / number_of_games, loss_count * 100 / number_of_games,
                    forced_termination * 100 / number_of_games, 100.0, 100.0]
        # data.append(data_row)
        return data_row
