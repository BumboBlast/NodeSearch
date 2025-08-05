from Solver import Solver
from Node import Node
from Problem.Problem import Problem
from collections import deque

''' 
Back Tracking search:
Only one successor is generated at a time rather than all successors; each partially expanded node
remembers which successor to generate next.

Backtracking search facilitates the idea of generating a successor by modifying the current state
description directly rather than copying it first.

For this to work, we must be able to undo each modification when we go back to generate the next successor.
'''


class BackTracking(Solver):
    def __init__(self, problem: Problem):
        super().__init__()
        # initialize a new random puzzle
        self.problem : Problem = problem
        # self.solution: str = self.problem.solution_state # actually ,the problem already knows about this.
        # initialize root node
        self.root : Node = Node()
        self.root.state = self.problem.initial_state

        #initialize frontier and explored (both unique)

        # self.dqFrontier: deque = deque() # FILO
#     #     self.explored: dict = dict() # idk if i should have explored??
#     #     # gen frontier
#         # self.explored[self.root.state] = self.root # idk if we should add root to explored
#         self.expandFrontier(self.root)
    
#     def expandFrontier(self, node_to_expand: Node):
#         ''' Modifies self.dqFrontier, push_backs new nodes by expanding argument node for each action.
#         '''
#         for action_a in self.problem.actions:
#             new_frontier_node : Node = node_to_expand.child_node(self.problem, action_a)
#             if new_frontier_node.state not in self.explored.keys():
#                 # self.qFrontier.put(new_frontier_node)
#                 self.dqFrontier.append(new_frontier_node)

    # def printFrontier(self, short: bool = False):
    #     # n: Node
    #     # for n in self.qFrontier.values():
    #     #     if short:
    #     #         print('action:\t' + str(n.action.__name__) + '  \t' + str(n.state))
    #     #     else:
    #     #         print('action: ' + str(n.action.__name__) + '\n' + Problem.print_state(n.state))
    #     n: Node
    #     for n in self.dqFrontier:
    #         if short:
    #             print('action:\t' + str(n.action.__name__) + '  \t' + str(n.state))
    #         else:
    #             print('action: ' + str(n.action.__name__) + '\n' + Problem.print_state(n.state))

    
    # def search(self) -> Node | None:
    #     '''
    #     Function GRAPH-SEARCH (problem) returns a solution, or failure
    #     initialize the frontier using the initial state of problem
    #     initialize the explored set to be empty
    #     loop do
    #     if the frontier is empty then return failure
    #     choose a leaf node and remove it from the frontier
    #     if the node contains a goal state then return the corresponding solution
    #     add the node to the explored set
    #     expand the chosen node, adding the resulting nodes to the frontier
    #     only if not in the frontier or explored set
    #     '''
    #     print('Depth First: (:')
    #     # check if this is solvable
    #     if not self.problem.is_solvable():
    #         return None

    #     plsHalt = 1_000_000
    #     while (plsHalt > 0):
    #         plsHalt -= 1
    #         # if the frontier is empty then return failure
    #         if (len(self.dqFrontier)) == 0:
    #             print('\n', end='\n')
    #             print('No soltion found ):')
    #             return None
    #         # choose a leaf node and remove it from the frontier
    #         # since frontier is a queu (FIFO), just pop_back (.get())
    #         chosenLeaf: Node = self.dqFrontier.pop()

    #         # if the node contains a goal state then return the corresponding solution
    #         if self.solution == chosenLeaf.state:
    #             print('\n')
    #             print('depth first search, done(:')
    #             print('nodes explroed: ', len(self.explored))
    #             return chosenLeaf
            
    #         # add the node to the explored set
    #         self.explored[chosenLeaf.state] = chosenLeaf

    #         # expand the chosen node, adding the resulting nodes to the frontier
    #         # only if not in the frontier or explored set (coverd in genFrontier)
    #         self.expandFrontier(chosenLeaf)
            
    #         if len(self.dqFrontier) % 10_000 == 0:
    #             print('size of frontier: ' + str(len(self.dqFrontier)), end='\r')
    #     print('\n')