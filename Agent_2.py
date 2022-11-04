import random
from pprint import pprint
import matplotlib.pyplot as plt
import config
import utils
from prey import Prey
from predator import Predator
import networkx as nx
"""
# Test Imports
from pprint import pprint
import environment as env

"""


class Agent_2:

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
        Moves according to the modified priority

        Parameters:
        self
        arena (dictionary): Adjacency list representing the graph
        prey_loc (int): Location of prey
        predator_loc (int): Location of Predator
        """

        pos = utils.best_node_v2(arena, self.curr_pos, prey_loc, predator_loc)

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

        number_of_games = config.NUMBER_OF_GAMES
        forced_termination_threshold = config.FORCED_TERMINATION_THRESHOLD

        while game_count < number_of_games:
            # Creating objects
            prey = Prey()
            predator = Predator()
            agent2 = Agent_2(prey.curr_pos, predator.curr_pos)

            step_count = 0

            # chocolate pan
            test_prey_pos= prey.curr_pos
            test_predator_pos = predator.curr_pos
            test_agent_pos = agent2.curr_pos

            while 1:
                print("In game Agent_2 at game_count: ", game_count, " step_count: ", step_count)
                print(agent2.curr_pos, prey.curr_pos, predator.curr_pos)
                agent2.move(arena, prey.curr_pos, predator.curr_pos)

                # Checking termination states
                if agent2.curr_pos == prey.curr_pos:
                    win_count += 1
                    break
                elif agent2.curr_pos == predator.curr_pos:
                    loss_count += 1
                    break

                prey.move(arena)

                # Checking termination states
                if agent2.curr_pos == prey.curr_pos:
                    win_count += 1
                    break

                predator.move(agent2.curr_pos, arena)

                # Checking termination states
                if agent2.curr_pos == predator.curr_pos:
                    loss_count += 1
                    break

                step_count += 1

                # Forcing termination
                if step_count >= forced_termination_threshold:
                    forced_termination += 1
                    break

            game_count += 1

        data_row = ["Agent_2", win_count * 100 / number_of_games, loss_count * 100 / number_of_games,
                    forced_termination * 100 / number_of_games]
        # data.append(data_row)


        # chocolate pan
        # if loss_count * 100 / number_of_games > 30:
        #     pprint(arena)
        #     print("Agent:",test_agent_pos," Prey :",test_prey_pos, " Predator :",test_predator_pos)
        #
        #     edges = []
        #     for key in arena:
        #         for i in arena[key]:
        #             edges.append([key,i])
        #         #print(edges)
        #     graph=nx.Graph()
        #     graph.add_edges_from(edges)
        #     nx.draw_networkx(graph)
        #     plt.show()
        #
        #     exit(0)
        return data_row


"""
# Class Test code
#arena=env.generate_environement()
arena = {0: [1, 49, 48],
         1: [2, 0, 46],
         2: [3, 1, 5],
         3: [4, 2, 7],
         4: [5, 3, 6],
         5: [6, 4, 2],
         6: [7, 5, 4],
         7: [8, 6, 3],
         8: [9, 7, 10],
         9: [10, 8, 11],
         10: [11, 9, 8],
         11: [12, 10, 9],
         12: [13, 11, 14],
         13: [14, 12, 15],
         14: [15, 13, 12],
         15: [16, 14, 13],
         16: [17, 15, 19],
         17: [18, 16, 20],
         18: [19, 17, 21],
         19: [20, 18, 16],
         20: [21, 19, 17],
         21: [22, 20, 18],
         22: [23, 21, 26],
         23: [24, 22, 25],
         24: [25, 23, 28],
         25: [26, 24, 23],
         26: [27, 25, 22],
         27: [28, 26, 30],
         28: [29, 27, 24],
         29: [30, 28, 31],
         30: [31, 29, 27],
         31: [32, 30, 29],
         32: [33, 31, 35],
         33: [34, 32],
         34: [35, 33, 39],
         35: [36, 34, 32],
         36: [37, 35, 38],
         37: [38, 36, 41],
         38: [39, 37, 36],
         39: [40, 38, 34],
         40: [41, 39, 44],
         41: [42, 40, 37],
         42: [43, 41],
         43: [44, 42, 47],
         44: [45, 43, 40],
         45: [46, 44, 49],
         46: [47, 45, 1],
         47: [48, 46, 43],
         48: [49, 47, 0],
         49: [0, 48, 45]}
# print(a1.curr_pos)
a1.move(arena, 5, 6)
# pprint(arena)
"""
