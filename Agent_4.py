import random
import config
import utils
from prey import Prey
from predator import Predator


class Agent_4:

    def __init__(self, prey_loc, predator_loc):
        """
        Initializing the position of the Agent at locations where prey and predator are not present
        Also initializes the belief state of the agent

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

        self.prev_pos = 999

        self.prey_belief_state = dict.fromkeys([i for i in range(50)], 1 / 49)
        self.prey_belief_state[self.curr_pos] = 0
        # print(f'Initial belief state: {self.prey_belief_state}')

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
            self.prev_pos = self.curr_pos
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
        data_row = []

        number_of_games = config.NUMBER_OF_GAMES
        forced_termination_threshold = config.FORCED_TERMINATION_THRESHOLD

        prey_certainty = 0.0
        while game_count < number_of_games:
            # Creating objects
            prey = Prey()
            predator = Predator()
            agent4 = Agent_4(prey.curr_pos, predator.curr_pos)

            step_count = 0
            found_prey = False
            prey_certainty_counter = 0
            while 1:
                print("In game Agent_4 at game_count: ", game_count, " step_count: ", step_count)
                print(agent4.curr_pos, prey.curr_pos, predator.curr_pos)

                # Survey a node initially without ever knowing where the prey is for a fact
                found_prey, node_surveyed = utils.survey_prey(agent4, prey)

                # prey belief state will be updated here
                agent4.prey_belief_state = utils.update_prey_belief_state(agent4.prey_belief_state, \
                                                                          agent4.curr_pos, \
                                                                          agent4.prev_pos, \
                                                                          arena, \
                                                                          found_prey, \
                                                                          node_surveyed, \
                                                                          'after_survey')
                if max(agent4.prey_belief_state.values()) == 1:
                    prey_certainty_counter += 1

                believed_prey_curr_pos = utils.return_max_prey_belief(agent4.prey_belief_state, arena)

                # using the max belief node for prey
                agent4.move(arena, believed_prey_curr_pos, predator.curr_pos)

                # Checking termination states
                if agent4.curr_pos == prey.curr_pos:
                    win_count += 1
                    break
                elif agent4.curr_pos == predator.curr_pos:
                    loss_count += 1
                    break

                # update belief state
                agent4.prey_belief_state = utils.update_prey_belief_state(agent4.prey_belief_state, \
                                                                          agent4.curr_pos, \
                                                                          agent4.prev_pos, \
                                                                          arena, \
                                                                          found_prey, \
                                                                          node_surveyed, \
                                                                          'after_agent_moves')


                prey.move(arena)

                # Checking termination states
                if agent4.curr_pos == prey.curr_pos:
                    win_count += 1
                    break

                agent4.prey_belief_state = utils.update_prey_belief_state(agent4.prey_belief_state, \
                                                                          agent4.curr_pos, \
                                                                          agent4.prev_pos, \
                                                                          arena, \
                                                                          found_prey, \
                                                                          node_surveyed, \
                                                                          'after_prey_moves')


                predator.move(agent4.curr_pos, arena)

                # Checking termination states
                if agent4.curr_pos == predator.curr_pos:
                    loss_count += 1
                    break

                step_count += 1

                # Forcing termination
                if step_count >= forced_termination_threshold:
                    forced_termination += 1
                    break
            if step_count != 0:
                prey_certainty += prey_certainty_counter / step_count
            else:
                prey_certainty = 0.0

            game_count += 1

        data_row = ["Agent_4", win_count * 100 / number_of_games, loss_count * 100 / number_of_games,
                    forced_termination * 100 / number_of_games, prey_certainty * 100 / number_of_games, 100.0]

        return data_row
