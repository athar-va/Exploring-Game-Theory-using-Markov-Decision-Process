import networkx as nx
import matplotlib.pyplot as plt
import random

def generate_environement():
    available_nodes=[]

    # Adjacency Hashmap to build a crircular arena
    arena = {0:[1,49],1:[2,0],2:[3,1],3:[4,2],4:[5,3],5:[6,4],6:[7,5],7:[8,6],8:[9,7],9:[10,8],10:[11,9],11:[12,10],12:[13,11],13:[14,12],14:[15,13],15:[16,14],16:[17,15],17:[18,16],18:[19,17],19:[20,18],20:[21,19],21:[22,20],22:[23,21],23:[24,22],24:[25,23],25:[26,24],26:[27,25],27:[28,26],28:[29,27],29:[30,28],30:[31,29],31:[32,30],32:[33,31],33:[34,32],34:[35,33],35:[36,34],36:[37,35],37:[38,36],38:[39,37],39:[40,38],40:[41,39],41:[42,40],42:[43,41],43:[44,42],44:[45,43],45:[46,44],46:[47,45],47:[48,46],48:[49,47],49:[0,48]}

    # Map to store degree of each node
    degree = {}

    # initiating degrees
    for keys in arena.keys():
        degree[keys]=len(arena[keys])
        available_nodes.append(keys)

    #print(degree)
    #print(available_nodes)

    while len(available_nodes) > 0:
        #print(available_nodes)
        node1 = random.choice(available_nodes)

        # Checking if random node has degree 3
        if degree[node1] < 3:

            #generating node1 neighbours with degree < 2
            legal_node2_neighbours=[]
            i = -5
            while i < 6:
                node2 = node1 + i
                i = i + 1

                # Handling  node2 < 0 and node2 > 49
                if node2 < 0:
                    node2 = 50 - abs(node2)
                if node2 > 49:
                    node2 = node2 - 50

                #discard if the edge already exists
                if node2 == node1 or degree[node2] >= 3 or node2 in arena[node1] :
                    continue
                elif degree[node2] > 3:
                    continue
                else:
                    legal_node2_neighbours.append(node2)

            #print("legal nodes for ",node1,":", legal_node2_neighbours)

            # legal_node2_neighbours contains all the legal neighbours of node2
            if len(legal_node2_neighbours)==0:
                available_nodes.remove(node1)
                continue

            # Selecting a random node 2
            node2 = random.choice(legal_node2_neighbours)

            # Checking degree of Node 2
            if degree[node2] < 3:
                # Adding edge to the dictionary
                arena[node1].append(node2)
                arena[node2].append(node1)

                # Removing nodes from available nodes
                #print(node1,node2)
                available_nodes.remove(node1)
                available_nodes.remove(node2)
                degree[node1] += 1
                degree[node2] += 1

        """if len(available_nodes) == 2:
            node1=available_nodes[0]
            node2=available_nodes[1]
            if degree[node2] <3 and degree[node1] < 3 :
                # Adding edge to the dictionary
                arena[node1].append(node2)
                arena[node2].append(node1)

                # Removing nodes from available nodes
                print(node1, node2)
                available_nodes.remove(node1)
                available_nodes.remove(node2)
                degree[node1] += 1
                degree[node2] += 1"""

        #print(available_nodes)
        #print(sum(degree.values()))

    print(sum(degree.values()))
    #print(degree)
    #print(arena)

    # Maze visualization code

    """edges = []
    for key in arena:
        for i in arena[key]:
            edges.append([key,i])
    #print(edges)
    graph=nx.Graph()
    graph.add_edges_from(edges)
    nx.draw_networkx(graph)
    plt.show()"""

    return arena

# arena=generate_environement()
# print(arena)
