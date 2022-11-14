import random
import config
import utils
from prey import Prey
from predator import Predator



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
                    forced_termination * 100 / number_of_games, 100.0, 100.0]

        return data_row

