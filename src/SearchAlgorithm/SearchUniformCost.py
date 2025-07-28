

'''
Uniform-cost search on a graph. The algorithm is identical to the general graph search algorithm in,
except for the use of a priority queue and the addition of an extra check in case a shorter path to
a frontier state is discovered. The data structure for frontier needs to support efficient membership
testing, so it should combine the capabilities of a priority queue and a hash table.


function UNIFORM-COST-SEARCH(problem) returns a solution, or failure
    node ← a node with STATE = problem.INITIAL-STATE ,PATH-COST = 0
    frontier ← a priority queue ordered by PATH-COST , with node as the only element
    explored ← an empty set
    loop do
        if EMPTY?(frontier) then return failure
        node ← POP(frontier) /* chooses the lowest-cost node in frontier */
        if problem.GOAL-TEST(node.STATE) then return SOLUTION(node)
        add node.STATE to explored
        for each action in problem.ACTIONS (node.STATE) do
            child ← CHILD-NODE(problem, node, action)
            if child.STATE is not in explored or frontier then
                frontier ← INSERT(child ,frontier)
            else if child.STATE is in frontier with higher PATH-COST then
                replace that frontier node with child
'''


from Node import Node
from Problem import Problem
from queue import Queue
from SearchAlgorithm.Solver import Solver
import heapq

class UniformCost(Solver):
    def __init__(self, problem: Problem):
        super().__init__()
        self.problem : Problem = problem
        self.solution: str = self.problem.solution_state
        self.root : Node = Node()
        self.root.state = self.problem.initial_state

        #initialize frontier and explored (both unique)
        self.qFrontier: list = list() # priority queue, ordered by path cost
        self.frontierHash : dict = dict()
        self.qFrontier.append([self.root.path_cost, self.root.state])
        self.frontierHash[self.root.state] = self.root
        self.explored: set = set()
        # self.explored.add(self.root.state)
    
    def expandFrontier(self, node_to_expand: Node):
        ''' Modifies self.qFrontier, push_backs new nodes by expanding argument node for each action.
        '''
        for action in self.problem.actions:
            child : Node = node_to_expand.child_node(self.problem, action)
            if child.state == node_to_expand.state:
                continue
            entry = [child.path_cost, child.state]
            # if (child.state not in self.explored) and (child.state not in self.qFrontier):
            if (child.state not in self.explored) and (child.state not in self.frontierHash):
                heapq.heappush(self.qFrontier, entry)
                self.frontierHash[child.state] = child
            elif child.state in self.frontierHash:
                current_frontier_node: Node = self.frontierHash[child.state]
                if current_frontier_node.path_cost > child.path_cost:
                    self.qFrontier[self.qFrontier.index(child.state)] = child
                    self.frontierHash[child.state] = entry
    
    def search(self) -> Node | None:
        ''' See src/SearchBreadthFirst.py
        '''
        print('Unifrome-Cost (:')

        # check if this is solvable
        if not self.problem.is_solvable():
            return None

        plsHalt = 1_000_000
        while (plsHalt > 0):
            plsHalt -= 1
            if len(self.qFrontier) == 0:
                return None
            
            # pop node (pop lowest path cost)
            chosen_leaf_state: str  = heapq.heappop(self.qFrontier)[1]
            chosen_leaf: Node = self.frontierHash[chosen_leaf_state]
            self.frontierHash.pop(chosen_leaf.state)

            if chosen_leaf.state == self.problem.solution_state:
                return chosen_leaf
            self.explored.add(chosen_leaf.state)
            self.expandFrontier(chosen_leaf)

            if len(self.qFrontier) % 1_000 == 0:
                print('size of frontier: ' + str(len(self.qFrontier)), end='\r')
        print('\n')
