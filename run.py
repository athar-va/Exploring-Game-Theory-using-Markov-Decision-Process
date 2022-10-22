from pprint import pprint

import environment as env
from prey import Prey
from predator import Predator
from Agent_1 import Agent_1
import utils
import config

def run():
    """
    Runs all the agents and calls the data collection function

    """
    no_of_arenas = 0

    results=[]
    header = ["agent_no", "perc_win", "perc_loss", "perc_forced_termination"]
    results.append(header)

    while no_of_arenas < config.NUMBER_OF_ARENAS:
        arena = env.generate_environement()
        results.append(Agent_1.begin(arena))
        #  results.append(begin_agent_2(arena))
        #  results.append(begin_agent_3(arena))
        #  results.append(begin_agent_4(arena))
        #  results.append(begin_agent_5(arena))
        #  results.append(begin_agent_6(arena))
        #  results.append(begin_agent_7(arena))
        #  results.append(begin_agent_8(arena))

        no_of_arenas += 1

    utils.store_data(results)
    print("Final Data Collected !")

if __name__ == '__main__':
    run()
