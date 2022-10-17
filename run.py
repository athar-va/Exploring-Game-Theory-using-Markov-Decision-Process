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

    # testing shortest path utility
    # path, path_length = utils.get_shortest_path(arena, 0, 48)
    # print(path, path_length)

    predator = Predator()
    print('Predator:')
    print(f'predator is at {predator.curr_pos}')
    predator.move(20, arena)
    print(f'predator moved to {predator.curr_pos}')

if __name__ == '__main__':
    run()
