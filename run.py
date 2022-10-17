from pprint import pprint

import environment as env
from prey import Prey

def run():
    # Generating the environment
    arena = env.generate_environement()
    pprint(arena)

    print('-'*100)
    prey = Prey()
    print(prey.curr_pos)

    prey.move(arena)
    print(prey.curr_pos)

if __name__ == '__main__':
    run()
