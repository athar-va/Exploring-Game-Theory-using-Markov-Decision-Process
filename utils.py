from collections import deque
import csv

import config

def store_data(data):
    """
    Stores the collected data toa a CSV file

    data: Data collected from all the agents
    """
    file_path_to_write = config.FILE_PATH + config.FILE_NAME
    print(file_path_to_write)
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


