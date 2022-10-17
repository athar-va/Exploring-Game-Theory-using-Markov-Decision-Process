from pprint import pprint

import environment as env
from prey import Prey
from predator import Predator
import utils

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

if __name__ == '__main__':
    run()
