from pprint import pprint

import environment as env
from prey import Prey
from predator import Predator
from Agent_1 import Agent_1
from Agent_2 import Agent_2
from Agent_3 import Agent_3
from Agent_4 import Agent_4
from Agent_5 import Agent_5
from Agent_6 import Agent_6
from Agent_7 import Agent_7
from Agent_8 import Agent_8
from Agent_7_with_defective_drone import Agent_7_wdd
from Agent_7_wdd_handled import Agent_7_wdd_handled
# from Agent_9 import Agent_9
# from test_agent import Agent_7
import utils
import config

def run():
    """
    Runs all the agents and calls the data collection function

    """
    no_of_arenas = 0

    results=[]
    # header = ["agent_no", "perc_win", "perc_loss", "perc_forced_termination"]
    header = ["agent_no", "perc_win", "perc_loss", "perc_forced_termination", "perc_prey_known", "perc_predator_known"]
    results.append(header)

    while no_of_arenas < config.NUMBER_OF_ARENAS:
        arena = env.generate_environement()
        # results.append(Agent_1.begin(arena))
        # results.append(Agent_2.begin(arena))
        # results.append(Agent_3.begin(arena))
        # results.append(Agent_4.begin(arena))
        # results.append(Agent_5.begin(arena))
        # results.append(Agent_6.begin(arena))
        results.append(Agent_7.begin(arena))
        # results.append(Agent_8.begin(arena))
        # results.append(Agent_7_wdd.begin(arena))
        # results.append(Agent_7_wdd_handled.begin(arena))
        # results.append(Agent_9.begin(arena))
        # results.append(Agent_test.begin(arena))

        print('-'*100)
        print(f'arena number: {no_of_arenas}')
        no_of_arenas += 1
    
    #wrote something for summarizing metrics across all arenas, should convert to a function later
    # a1_survival = 0
    # a1_dead = 0
    # a1_terminated = 0

    # print('r')
    # print(results)
    # print('r')
    # print(results[0][0])
    # print('r')
    # print(results[1][0])

    # for row in results:
    #     if row[0] == 'Agent_1':
    #         a1_survival += row[1]
    #         a1_dead += row[2]
    #         a1_terminated += row[3]
    # results.append(['Agent_1_Summary', a1_survival / config.NUMBER_OF_ARENAS, a1_dead / config.NUMBER_OF_ARENAS\
    #                 , a1_terminated / config.NUMBER_OF_ARENAS])

    # print(results)

    utils.store_data(results)
    print("Final Data Collected !")

if __name__ == '__main__':
    run()
