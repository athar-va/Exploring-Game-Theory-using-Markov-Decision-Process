from collections import deque
import csv
import random
from pprint import pprint

from matplotlib.artist import get

import config

def update_prey_belief_state(prey_belief_state, agent_curr_pos, agent_prev_pos, arena, found_prey, surveyed_node, checkpoint):
    """
    Handles kind of updates based on found_prey

    Parameters:


    Returns:
    new_prey_belief_state (dict): The updated belief state
    """

    # Initializing the new prey belief states
    new_prey_belief_state = dict.fromkeys([i for i in range(50)], 999.0)
    new_prey_belief_state[agent_curr_pos] = 0.0

    # After surveying the node
    if checkpoint == 'after_survey':
        if found_prey:
            for i in range(50):
                new_prey_belief_state[i] = 0.0
            new_prey_belief_state[surveyed_node] = 1.0
            return new_prey_belief_state
        else:
            new_prey_belief_state[surveyed_node] = 0.0
            for i in range(50):
                if i not in (agent_curr_pos, surveyed_node):
                    new_prey_belief_state[i] = prey_belief_state[i] / ( sum(prey_belief_state.values()) - prey_belief_state[surveyed_node] - prey_belief_state[agent_curr_pos])
            # print('in update func')
            # pprint(new_prey_belief_state)
            # print('sum of prob: ', sum(new_prey_belief_state.values()))
            # exit(0)
            return new_prey_belief_state
    
    elif checkpoint == 'after_agent_moves':
        if found_prey:
            return prey_belief_state
        else:
            print(f'agent_curr_pos in func: {agent_curr_pos}')
            new_prey_belief_state[agent_prev_pos] = 0.0
            new_prey_belief_state[agent_curr_pos] = 0.0
            new_prey_belief_state[surveyed_node] = 0.0
            
            for i in range(50):
                if i not in (agent_curr_pos, agent_prev_pos, surveyed_node):
                    new_prey_belief_state[i] = prey_belief_state[i] / ( sum(prey_belief_state.values()) - prey_belief_state[agent_curr_pos] - prey_belief_state[surveyed_node])
            # print('in update func')
            # pprint(new_prey_belief_state)
            # print('sum of prob: ', sum(new_prey_belief_state.values()))
            # exit(0)
            return new_prey_belief_state

    elif checkpoint == 'after_prey_moves':
        new_prey_belief_state[agent_curr_pos] = 0.0

        temp_prey_belief_state = dict.fromkeys([i for i in range(50)], 999.0)
        temp_prey_belief_state[agent_curr_pos] = 0.0

        # for i in range(50):
        #     if i != agent_curr_pos:
        #         temp_prey_belief_state[i] = prey_belief_state[i] / ( sum(prey_belief_state.values()) - prey_belief_state[surveyed_node] - prey_belief_state[agent_curr_pos])
        # print('in update func temp')
        # pprint(temp_prey_belief_state)
        # print('sum of prob: ', sum(temp_prey_belief_state.values()))
        # print('arena')
        
        # Test for degree
        # for i in range(50):
        #     temp_sum = 0.0
        #     if i != agent_curr_pos:
        #         if i not in arena[agent_curr_pos]:
        #             for j in arena[i]:
        #                 temp_sum += prey_belief_state[j] / ( get_degree(arena, j) + 1 )
        #             temp_sum += prey_belief_state[i] / ( get_degree(arena, i) + 1 )
        #         elif i in arena[agent_curr_pos]:
        #             for j in arena[i]:
        #                 temp_sum += prey_belief_state[j] / ( get_degree(arena, j))
        #             temp_sum += prey_belief_state[i] / ( get_degree(arena, i))
        #     new_prey_belief_state[i] = temp_sum
        
        # prey has moved
        for i in range(50):
            temp_sum = 0.0
            for j in arena[i]:
                temp_sum += prey_belief_state[j] / ( get_degree(arena, j) + 1 )
            temp_sum += prey_belief_state[i] / ( get_degree(arena, i) + 1 )
            temp_prey_belief_state[i] = temp_sum

        # pretend to survey node for agent curr pos
        new_prey_belief_state[agent_curr_pos] = 0.0
        for i in range(50):
            if i != agent_curr_pos:
                new_prey_belief_state[i] = temp_prey_belief_state[i] / ( sum(temp_prey_belief_state.values()) - temp_prey_belief_state[agent_curr_pos])


        # print('in update func')
        # pprint(new_prey_belief_state)
        # print('sum of prob: ', sum(new_prey_belief_state.values()))
        # print('arena')
        # pprint(arena)
        # exit(0)
        return new_prey_belief_state

def update_predator_belief_state(predator_belief_state, agent_curr_pos, agent_prev_pos, arena, found_predator, surveyed_node, checkpoint):
    """Placeholder
    Handles kind of updates based on found_prey
    """
    
    # Initializing the new prey belief states
    new_predator_belief_state = dict.fromkeys([i for i in range(50)], 999.0)
    """
    if checkpoint == 'after_survey':
        
    elif checkpoint == 'after_agent_moves':
    
    elif checkpoint == 'after_prey_moves':
    """

def get_degree(arena, node):
    """
    Gets the degree of the node

    Parameters:
    arena (dict): Arena for the game
    node (int): Node to get the degree for

    Returns:
    len(arena[node]) (int): Gets the degree of the node
    """
    return len(arena[node])

def survey_prey(agent, prey):
    """
    Surveys the node with the highest probability of the prey being there and updates the belief state accordingly

    Parameters:
    agent (object): Agent object
    prey (object): Prey object

    Returns:
    found_prey (Bool): Returns True if found prey else False
    node_to_survey (int): Returns the node surveyed
    """

    belief_state = agent.prey_belief_state

    # Selects all positions where the probability is max
    max_prob_of_prey = [pos for pos, prob in belief_state.items() if prob ==  max(belief_state.values())]

    print(max_prob_of_prey)

    node_to_survey = random.choice(max_prob_of_prey)

    print(node_to_survey)

    if node_to_survey == prey.curr_pos:
        return True, node_to_survey
    else:
        return False, node_to_survey

def survey_predator(agent, predator):
    """
    Surveys the node with the highest probability of the predator being there and updates the belief state accordingly

    Parameters:
    agent (object): Agent object
    prey (object): Predator object

    Returns:
    found_predator (Bool): Returns True if found predator else False
    node_to_survey (int): Returns the node surveyed
    """

    belief_state = agent.predator_belief_state

    # Selects all positions where the probability is max
    max_prob_of_predator = [pos for pos, prob in belief_state.items() if prob == max(belief_state.values())]

    print(max_prob_of_predator)

    node_to_survey = random.choice(max_prob_of_predator)

    print(node_to_survey)

    if node_to_survey == predator.curr_pos:
        return True, node_to_survey
    else:
        return False, node_to_survey


def store_data(data):
    """
    Stores the collected data toa a CSV file

    data: Data collected from all the agents
    """
    file_path_to_write = config.FILE_PATH + config.FILE_NAME
    # print(file_path_to_write)
    f = open(file_path_to_write, 'w')
    writer = csv.writer(f)
    writer.writerows(data)
    print("Data Collection Complete")
    f.close()


def FindPath(parent, start_pos, end_pos):
    """
    Backtracks and finds the path in the arena to the end position from the start position

    Parameters:
    parent (dict): Parent dictionary of each node
    start_pos (int): Start position of the path
    end_pos (int): End position of the path

    Returns:
    path (deque): Path from start to end position
    """
    path = deque()
    path.append(end_pos)
    while path[-1] != start_pos:
         path.append(parent[path[-1]])
    path.reverse()
    path.popleft()
    return path

def get_shortest_path(start_pos, end_pos, arena):
    """
    Uses Breath First Search to find the shortest path between the start and end position
    'neighbours' is used as the fringe (queue) to add surrounding nodes in the arena

    Parameters:
    start_pos (int): Start position of the path
    end_pos (int): End position of the path
    arena (dict): The arena used currently

    Returns:
    path (deque): Shortest path evaluated
    (len(path) - 1) (int): Length of the path
    """
    
    parent = {}
    visited = [False] * 50
    
    #print(f'start_pos = {start_pos}')
    visited[start_pos] = True
    # print(visited)
    neighbours = deque()

    curr_pos = start_pos
    while curr_pos != end_pos:
        for surrounding_node in arena[curr_pos]:
            # print(f'curr_pos: {curr_pos}')
            # print(f'surrounding_node: {surrounding_node}')
            if not visited[surrounding_node] and surrounding_node not in neighbours:
                neighbours.append(surrounding_node)
                parent.update({surrounding_node: curr_pos})
                visited[surrounding_node] = True
                # print(f'added {surrounding_node}')
        curr_pos = neighbours.popleft()

    path = FindPath(parent, start_pos, end_pos)
    # print(f'a {type(path)}')
    return path, (len(path) - 1)

def return_max_prey_belief(belief_state, arena):
    """
    Placeholder for now
    """
    # return max(belief_state, key = belief_state.get)
    return random.randint(0,49)

def return_max_predator_belief(belief_state, arena):
    """
    Placeholder for now
    """
    # return max(belief_state, key = belief_state.get)
    return random.randint(0,49)

#needs to be worked upon
def best_node_v2(arena, curr_pos, prey_loc, predator_loc):
    """
    Returns the node that the agent should move to according to the following rules:
    1. Neighbors that are closer to the Prey and farther from the Predator.
    2. Neighbors that are closer to the Prey and not closer to the Predator.
    3. Neighbors that are not farther from the Prey and farther from the Predator.
    4. Neighbors that are not farther from the Prey and not closer to the Predator.
    5. Neighbors that are farther from the Predator.
    6. Neighbors that are not closer to the Predator.
    7. Sit still and pray.

    Parameters:
    arena (dictionary): Adjacency list representing the graph
    prey_loc (int): Location of prey
    predator_loc (int): Location of Predator

    Returns:
    curr_pos (int): Position to move to
    """

    # Do not remove the following test cases
    # curr_pos = 17
    # curr_pos = 42

    #print("Initial pos", curr_pos)
    # Neighbours of the current node are extracted here
    neighbours = arena[curr_pos].copy()

    # Distances from prey and predator will be stored in the following dicts
    predator_dist = {}
    prey_dist = {}

    # Storing the distances of the agent location to the prey and predator
    path, curr_pos_prey_dist = get_shortest_path(curr_pos, prey_loc, arena)
    path, curr_pos_predator_dist = get_shortest_path(curr_pos, predator_loc, arena)

    # Find distance from all neighbours to the prey and the predator
    for i in neighbours:
        path, prey_dist[i] = get_shortest_path(i, prey_loc, arena)
        path, predator_dist[i] = get_shortest_path(i, predator_loc, arena)

    # Defining subsets of nodes
    closer_to_prey = {}
    not_farther_from_prey = {}
    farther_from_predator = {}
    not_closer_to_predator = {}

    # Adding nodes to the subsets
    for k in prey_dist.keys():
        if prey_dist[k] < curr_pos_prey_dist:
            closer_to_prey[k] = prey_dist[k]

    for k in prey_dist.keys():
        if prey_dist[k] == curr_pos_prey_dist:
            not_farther_from_prey[k] = prey_dist[k]

    for k in predator_dist.keys():
        if predator_dist[k] >= curr_pos_predator_dist:
            farther_from_predator[k] = predator_dist[k]

    for k in predator_dist.keys():
        if predator_dist[k] == curr_pos_predator_dist:
            farther_from_predator[k] = predator_dist[k]

    # Flag helps to avoid going through multiple ifs if one if condition is satisfied
    flag = 0

    # Assigning the position accorinding to the given priorrity
    if len(set(closer_to_prey).intersection(set(farther_from_predator))) != 0 and flag == 0:
        curr_pos = min(closer_to_prey, key=closer_to_prey.get)
        #print("priority 1")
        flag = 1

    elif len(set(closer_to_prey).intersection(set(not_closer_to_predator))) != 0 and flag == 0:
        curr_pos = min(closer_to_prey, key=closer_to_prey.get)
        #print("priority 2")
        flag = 1

    elif len(set(not_farther_from_prey).intersection(set(farther_from_predator))) != 0 and flag == 0:
        curr_pos = min(not_farther_from_prey, key=not_farther_from_prey.get)
        #print("priority 3")
        flag = 1

    elif len(set(closer_to_prey).intersection(set(not_closer_to_predator))) != 0 and flag == 0:
        curr_pos = min(closer_to_prey, key=closer_to_prey.get)
        #print("priority 4")
        flag = 1

    elif len(farther_from_predator) != 0 and flag == 0:
        curr_pos = max(farther_from_predator, key=farther_from_predator.get)
        #print("priority 5")
        flag = 1

    elif len(not_closer_to_predator) != 0 and flag == 0:
        curr_pos = min(not_closer_to_predator, key=not_closer_to_predator.get)
        #print("priority 6")

    else:
        pass
        #print("Sitting and Praying")
        return 999

    """print(curr_pos_prey_dist,curr_pos_predator_dist)
    print(prey_dist,predator_dist)
    print("pos after movement", curr_pos)"""

    return curr_pos

def best_node(arena, curr_pos, prey_loc, predator_loc):
    """
    Returns the node that the agent should move to according to the following rules:
    1. Neighbors that are closer to the Prey and farther from the Predator.
    2. Neighbors that are closer to the Prey and not closer to the Predator.
    3. Neighbors that are not farther from the Prey and farther from the Predator.
    4. Neighbors that are not farther from the Prey and not closer to the Predator.
    5. Neighbors that are farther from the Predator.
    6. Neighbors that are not closer to the Predator.
    7. Sit still and pray.

    Parameters:
    arena (dictionary): Adjacency list representing the graph
    prey_loc (int): Location of prey
    predator_loc (int): Location of Predator

    Returns:
    curr_pos (int): Position to move to
    """

    # Do not remove the following test cases
    # curr_pos = 17
    # curr_pos = 42

    #print("Initial pos", curr_pos)
    # Neighbours of the current node are extracted here
    neighbours = arena[curr_pos].copy()

    # Distances from prey and predator will be stored in the following dicts
    predator_dist = {}
    prey_dist = {}

    # Storing the distances of the agent location to the prey and predator
    path, curr_pos_prey_dist = get_shortest_path(curr_pos, prey_loc, arena)
    path, curr_pos_predator_dist = get_shortest_path(curr_pos, predator_loc, arena)

    # Find distance from all neighbours to the prey and the predator
    for i in neighbours:
        path, prey_dist[i] = get_shortest_path(i, prey_loc, arena)
        path, predator_dist[i] = get_shortest_path(i, predator_loc, arena)

    # Defining subsets of nodes
    closer_to_prey = {}
    not_farther_from_prey = {}
    farther_from_predator = {}
    not_closer_to_predator = {}

    # Adding nodes to the subsets
    for k in prey_dist.keys():
        if prey_dist[k] < curr_pos_prey_dist:
            closer_to_prey[k] = prey_dist[k]

    for k in prey_dist.keys():
        if prey_dist[k] == curr_pos_prey_dist:
            not_farther_from_prey[k] = prey_dist[k]

    for k in predator_dist.keys():
        if predator_dist[k] >= curr_pos_predator_dist:
            farther_from_predator[k] = predator_dist[k]

    for k in predator_dist.keys():
        if predator_dist[k] == curr_pos_predator_dist:
            farther_from_predator[k] = predator_dist[k]

    # Flag helps to avoid going through multiple ifs if one if condition is satisfied
    flag = 0

    # Assigning the position accorinding to the given priorrity
    if len(set(closer_to_prey).intersection(set(farther_from_predator))) != 0 and flag == 0:
        curr_pos = min(closer_to_prey, key=closer_to_prey.get)
        #print("priority 1")
        flag = 1

    elif len(set(closer_to_prey).intersection(set(not_closer_to_predator))) != 0 and flag == 0:
        curr_pos = min(closer_to_prey, key=closer_to_prey.get)
        #print("priority 2")
        flag = 1

    elif len(set(not_farther_from_prey).intersection(set(farther_from_predator))) != 0 and flag == 0:
        curr_pos = min(not_farther_from_prey, key=not_farther_from_prey.get)
        #print("priority 3")
        flag = 1

    elif len(set(closer_to_prey).intersection(set(not_closer_to_predator))) != 0 and flag == 0:
        curr_pos = min(closer_to_prey, key=closer_to_prey.get)
        #print("priority 4")
        flag = 1

    elif len(farther_from_predator) != 0 and flag == 0:
        curr_pos = max(farther_from_predator, key=farther_from_predator.get)
        #print("priority 5")
        flag = 1

    elif len(not_closer_to_predator) != 0 and flag == 0:
        curr_pos = min(not_closer_to_predator, key=not_closer_to_predator.get)
        #print("priority 6")

    else:
        pass
        #print("Sitting and Praying")
        return 999

    """print(curr_pos_prey_dist,curr_pos_predator_dist)
    print(prey_dist,predator_dist)
    print("pos after movement", curr_pos)"""

    return curr_pos


