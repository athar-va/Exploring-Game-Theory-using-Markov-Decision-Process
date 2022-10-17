from pprint import pprint
import environment as env

def run():
    # Generating the environment
    arena = env.generate_environement()
    pprint(arena)

if __name__ == '__main__':
    run()
