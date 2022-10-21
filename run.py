from pprint import pprint
import csv
import environment as env
from prey import Prey
from predator import Predator
from Agent_1 import Agent_1
import utils


def begin_agent_1(arena):
    """
    Creates all the maze objects and plays number of games and collects data

    Parameters:
    agent1 (agent): Agent object

    """

    # Initiating game variables
    game_count = 0
    step_count = 0

    # Initiating variables for analysis
    win_count = 0
    loss_count = 0
    forced_termination = 0
    data = []
    data_row = []


    # Config variable (To be transferred to a parameter file)
    number_of_games = 1
    forced_termination_threshold = 1000

    while game_count < number_of_games:
        # Creating objects
        prey = Prey()
        predator = Predator()
        agent1 = Agent_1(prey.curr_pos, predator.curr_pos)

        step_count = 0

        while 1:
            print("In game Agent_1 at game_count: ", game_count, " step_count: ", step_count)
            print(agent1.curr_pos,prey.curr_pos,predator.curr_pos)
            agent1.move(arena, prey.curr_pos, predator.curr_pos)

            # Checking termination states
            if agent1.curr_pos == prey.curr_pos:
                win_count += 1
                break
            elif agent1.curr_pos == predator.curr_pos:
                loss_count += 1
                break

            prey.move(arena)

            # Checking termination states
            if agent1.curr_pos == prey.curr_pos:
                win_count += 1
                break
            elif agent1.curr_pos == predator.curr_pos:
                loss_count += 1
                break

            predator.move(agent1.curr_pos, arena)

            # Checking termination states
            if agent1.curr_pos == predator.curr_pos:
                loss_count += 1
                break

            step_count += 1

            # Forcing termination
            if step_count >= forced_termination_threshold:
                forced_termination += 1
                loss_count += 1
                break

        game_count += 1
        data_row = ["Agent_1", win_count*100/number_of_games,loss_count*100/number_of_games,forced_termination*100/number_of_games]
        print(data_row)
        data.append(data_row)
        pprint(arena)
    print(data)
    return data

def store_data(data):
    """
    Stores the collected data toa a CSV file

    data: Data collected from all the agents
    """
    f = open('D:/Desktop/Fall_22_Academics/520_Intro to AI/Project_2/Data/Agent1_data.csv', 'w')
    writer = csv.writer(f)
    writer.writerows(data)
    print("Data Collection Complete")
    f.close()

def run():
    """
    Runs all the agents and calls the data collection function

    """
    no_of_mazes=0

    results=[]
    header = ["agent_no", "perc_win", "perc_loss", "perc_forced_termination"]
    results.append(header)

    while no_of_mazes < no_of_mazes:
        arena = env.generate_environement()
        results.append(begin_agent_1(arena))
        #  results.append(begin_agent_2(arena))
        #  results.append(begin_agent_3(arena))
        #  results.append(begin_agent_4(arena))
        #  results.append(begin_agent_5(arena))
        #  results.append(begin_agent_6(arena))
        #  results.append(begin_agent_7(arena))
        #  results.append(begin_agent_8(arena))

        no_of_mazes += 1

    store_data(results)
    print("Final Data Collected !")



if __name__ == '__main__':
    run()
