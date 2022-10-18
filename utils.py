from collections import deque

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
