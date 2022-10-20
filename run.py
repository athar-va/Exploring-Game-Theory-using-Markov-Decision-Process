from pprint import pprint

import environment as env
from prey import Prey
from predator import Predator
from Agent_1 import Agent_1
import utils

def begin_agent_1(agent1, prey, predator, arena):
    pass

def run():
    # Generating the environment
    arena = env.generate_environement()
    pprint(arena)

    print('-'*100)
    prey = Prey()
    print(prey.curr_pos)

    # testing prey
    prey.move(arena)
    print(prey.curr_pos)

    #testing predator
    predator = Predator()
    print('Predator:')
    print(f'predator is at {predator.curr_pos}')
    predator.move(20, arena)
    print(f'predator moved to {predator.curr_pos}')

    #testing Agent 1
    agent1= Agent_1(prey.curr_pos, predator.curr_pos)
    print("Agent 1:")

    results_agent_1 = begin_agent_1(agent1, prey, predator, arena)
    agent1.move(arena, prey.curr_pos, predator.curr_pos)


if __name__ == '__main__':
    run()
