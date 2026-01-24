

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
from Problem.Problem import Problem
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
        # priority queue, ordered by path cost
        # heapFrontier contains tuple, (priority ,  task)
        self.heapFrontier: list = list() 
        heapq.heappush(self.heapFrontier, (0, self.root.state))
        self.explored: set = set()
    
    def expandFrontier(self, node_to_expand: Node):
        ''' Modifies self.qFrontier, push_backs new nodes by expanding argument node for each action.
        '''

    
    def search(self) -> Node | None:
        ''' 
        '''
        print('Uniform-Cost (:')
        return None
        # check if this is solvable
        if not self.problem.is_solvable():
            return None

        plsHalt = 1_000_000
        while (plsHalt > 0):
            plsHalt -= 1
            if len(self.qFrontier) == 0:
                return None
            
            # pop node (pop lowest path cost)
 