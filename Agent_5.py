import random
from pprint import pprint

import config
import utils
from prey import Prey
from predator import Predator


class Agent_5:
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

        self.predator_belief_state = dict.fromkeys([i for i in range(50)], 0)
        self.predator_belief_state[predator_loc] = 1



    def move(self, arena, prey_loc, predator_loc):
        """
        Moves Agent 5 according to the given Agent 1 priority

        Parameters:
        self
        arena (dictionary): Adjacency list representing the graph
        prey_loc (int): Location of prey
        predator_loc (int): Location of Predator
        """

        pos = utils.best_node(arena, self.curr_pos, prey_loc, predator_loc)

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

        while game_count < number_of_games:
            # Creating objects
            prey = Prey()
            predator = Predator()
            agent5 = Agent_5(prey.curr_pos, predator.curr_pos)

            step_count = 0
            found_predator = True
            believed_predator_curr_pos = predator.curr_pos
            while 1:
                print("In game Agent_5 at game_count: ", game_count, " step_count: ", step_count)
                print(agent5.curr_pos, prey.curr_pos, predator.curr_pos)

                # Survey a node initially without ever knowing where the prey is for a fact
                found_predator, node_surveyed = utils.survey_predator(agent5, predator)

                # prey belief state will be updated here
                agent5.predator_belief_state = utils.update_predator_belief_state(agent5.predator_belief_state, \
                                                                            agent5.curr_pos, \
                                                                            agent5.prev_pos, \
                                                                            arena, \
                                                                            found_predator, \
                                                                            node_surveyed, \
                                                                            'after_survey')


                believed_predator_curr_pos = utils.return_max_predator_belief(agent5.predator_belief_state, arena)

                print(f'believed_predator_curr_pos: {believed_predator_curr_pos}')
                # using the max belief node for prey
                agent5.move(arena, prey.curr_pos, believed_predator_curr_pos)

                # Checking termination states
                if agent5.curr_pos == prey.curr_pos:
                    win_count += 1
                    break
                elif agent5.curr_pos == predator.curr_pos:
                    loss_count += 1
                    break

                # update belief state
                agent5.predator_belief_state = utils.update_predator_belief_state(agent5.predator_belief_state, \
                                                                            agent5.curr_pos, \
                                                                            agent5.prev_pos, \
                                                                            arena, \
                                                                            found_predator, \
                                                                            node_surveyed, \
                                                                            'after_agent_moves')

                prey.move(arena)


                # Checking termination states
                if agent5.curr_pos == prey.curr_pos:
                    win_count += 1
                    break

                predator.distracted_move(agent5.curr_pos, arena)

                agent5.predator_belief_state = utils.update_predator_belief_state(agent5.predator_belief_state, \
                                                                            agent5.curr_pos, \
                                                                            agent5.prev_pos, \
                                                                            arena, \
                                                                            found_predator, \
                                                                            node_surveyed, \
                                                                            'after_predator_moves')

                # Checking termination states
                if agent5.curr_pos == predator.curr_pos:
                    loss_count += 1
                    break

                step_count += 1

                # Forcing termination
                if step_count >= forced_termination_threshold:
                    forced_termination += 1
                    break

            game_count += 1

        data_row = ["Agent_5", win_count * 100 / number_of_games, loss_count * 100 / number_of_games,
                    forced_termination * 100 / number_of_games]
        # data.append(data_row)
        return data_row