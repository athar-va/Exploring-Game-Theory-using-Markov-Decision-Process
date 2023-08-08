# Purpose of the Project

Here, we help an agent catch a prey in the presence of an adversory (predator) in different information settings listed below. The rules of movement of prey and predator are set. We build a probablistic model based on these rules and using Markov Decision Process , we attempt to catch the prey.

# Building the Environment

- The environment is a graph of 50 interconnected nodes in a circular arrangement.
- Agent, prey, and predator move between these nodes.
- Edges are added randomly for greater connectivity:
  - Random nodes with degree less than 3 are chosen.
  - Edges between these nodes and others within 5 steps forward or backward are added.
  - This process continues until no more edges can be introduced.

# Entities' Behaviors:

- The Prey: Movement involves random selection among neighbors or the current cell, with equal probabilities.
- The Predator: Available neighbors are assessed for shortest distance to the Agent. Movement occurs to the nearest neighbor. In case of tie, random selection is made.
- The Agent: Movement follows a specific strategy. In situations with limited information, surveying a distant node for its content is an option. The Agent possesses awareness of the decisions of the Predator and Prey, although specific actions remain unknown.

# Strategy Descriptions

- Agent 1: Precise knowledge of Predator and Prey locations is possessed by the Agent.During its turn, available neighbors are examined and selected based on these criteria:
  * Closer to the Prey and farther from the Predator.
  * Closer to the Prey but not closer to the Predator.
  * Not farther from the Prey and farther from the Predator.
  * Not farther from the Prey but not closer to the Predator.
  * Farther from the Predator.
  * Not closer to the Predator.
  * Remaining stationary.
- Agent 2: Beats Agent 1
- Agent 3: Knows the location of predator but not the prey.
- Agent 4: Beats Agent 3
- Agent 5: Knows the location of the prey but not the predator.
- Agent 6: Beats Agent 5
- Agent 7: Does not know locations of both the entities. 

# Technologies and Libraries Used

- Python

# Concepts Used

- Graph theory
- Game theory
- Markov Decision Process

#GraphTheory #GameTheory #BeliefStates #PythonProject#NoisySurveys #Drones #PythonCoding #ArtificialIntelligence #MDP
