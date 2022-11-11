import random
from pprint import pprint

import config
import utils
from prey import Prey
from predator import Predator


class Agent_8:

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

        # Initialize prey belief state
        self.prey_belief_state = dict.fromkeys([i for i in range(50)], 1 / 49)
        self.prey_belief_state[self.curr_pos] = 0
        # print(f'Initial prey belief state: {self.prey_belief_state}')

        # Initialize peadator belief state
        self.predator_belief_state = dict.fromkeys([i for i in range(50)], 0)
        self.predator_belief_state[predator_loc] = 1
        # print(f'Initial predator belief state: {self.predator_belief_state}')

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
        predator_certainty = 0.0
        while game_count < number_of_games:
            # Creating objects
            prey = Prey()
            predator = Predator()
            agent8 = Agent_8(prey.curr_pos, predator.curr_pos)

            step_count = 0
            found_prey = False
            found_predator = True
            prey_certainty_counter = 0
            predator_certainty_counter = 0
            while 1:
                print("In game Agent_8 at game_count: ", game_count, " step_count: ", step_count)
                print(agent8.curr_pos, prey.curr_pos, predator.curr_pos)

                # Check if it knows where the predator is
                if max(agent8.predator_belief_state.values()) == 1.0:
                    found_prey, node_surveyed = utils.survey_prey(agent8, prey)
                else:
                    found_predator, node_surveyed = utils.survey_predator(agent8, predator)

                # updating both belief states
                agent8.prey_belief_state = utils.update_prey_belief_state(agent8.prey_belief_state, \
                                                                          agent8.curr_pos, \
                                                                          agent8.prev_pos, \
                                                                          arena, \
                                                                          found_prey, \
                                                                          node_surveyed, \
                                                                          'after_survey')
                if max(agent8.prey_belief_state.values()) == 1:
                    prey_certainty_counter += 1
                agent8.predator_belief_state = utils.update_predator_belief_state(agent8.predator_belief_state, \
                                                                                  agent8.curr_pos, \
                                                                                  agent8.prev_pos, \
                                                                                  arena, \
                                                                                  found_predator, \
                                                                                  node_surveyed, \
                                                                                  'after_survey')
                if max(agent8.predator_belief_state.values()) == 1:
                    predator_certainty_counter += 1

                believed_prey_curr_pos = utils.return_max_prey_belief(agent8.prey_belief_state, arena)
                believed_predator_curr_pos = utils.return_max_predator_belief(agent8.predator_belief_state, arena)

                # print(f'believed_prey_curr_pos: {believed_prey_curr_pos}')
                # print(f'believed_predator_curr_pos: {believed_predator_curr_pos}')
                # using the max belief node for prey
                agent8.move(arena, believed_prey_curr_pos, believed_predator_curr_pos)

                # Checking termination states
                if agent8.curr_pos == prey.curr_pos:
                    win_count += 1
                    break
                elif agent8.curr_pos == predator.curr_pos:
                    loss_count += 1
                    break

                # update belief state
                agent8.prey_belief_state = utils.update_prey_belief_state(agent8.prey_belief_state, \
                                                                          agent8.curr_pos, \
                                                                          agent8.prev_pos, \
                                                                          arena, \
                                                                          found_prey, \
                                                                          node_surveyed, \
                                                                          'after_agent_moves')

                agent8.predator_belief_state = utils.update_predator_belief_state(agent8.predator_belief_state, \
                                                                                  agent8.curr_pos, \
                                                                                  agent8.prev_pos, \
                                                                                  arena, \
                                                                                  found_predator, \
                                                                                  node_surveyed, \
                                                                                  'after_agent_moves')

                prey.move(arena)

                agent8.prey_belief_state = utils.update_prey_belief_state(agent8.prey_belief_state, \
                                                                          agent8.curr_pos, \
                                                                          agent8.prev_pos, \
                                                                          arena, \
                                                                          found_prey, \
                                                                          node_surveyed, \
                                                                          'after_prey_moves')

                # Checking termination states
                if agent8.curr_pos == prey.curr_pos:
                    win_count += 1
                    break

                predator.distracted_move(agent8.curr_pos, arena)

                agent8.predator_belief_state = utils.update_predator_belief_state(agent8.predator_belief_state, \
                                                                                  agent8.curr_pos, \
                                                                                  agent8.prev_pos, \
                                                                                  arena, \
                                                                                  found_predator, \
                                                                                  node_surveyed, \
                                                                                  'after_predator_moves')
                # Checking termination states
                if agent8.curr_pos == predator.curr_pos:
                    loss_count += 1
                    break

                step_count += 1

                # Forcing termination
                if step_count >= forced_termination_threshold:
                    forced_termination += 1
                    break

            prey_certainty += prey_certainty_counter / step_count
            predator_certainty += predator_certainty_counter / step_count

            game_count += 1

        data_row = ["Agent_8", win_count * 100 / number_of_games, loss_count * 100 / number_of_games,
                    forced_termination * 100 / number_of_games, prey_certainty * 100 / number_of_games, predator_certainty * 100 / number_of_games]
        # data.append(data_row)
        return data_row