

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


from ChildNodeTest import Node
from ProblemTest import Problem
from queue import Queue
from Solver import Solver

class UniformCost(Solver):
    def __init__(self, problem: Problem):
        super().__init__()
        self.problem : Problem = problem
        self.solution: str = self.problem.solution_state
        self.root : Node = Node()
        self.root.state = self.problem.initial_state

        #initialize frontier and explored (both unique)
        self.qFrontier: dict = dict() # priority queue, ordered by path cost
        self.qFrontier[self.root.state] = self.root
        self.explored: set = set()
        # self.explored.add(self.root.state)

        
    
    def expandFrontier(self, node_to_expand: Node):
        ''' Modifies self.qFrontier, push_backs new nodes by expanding argument node for each action.
        '''
        for action in self.problem.actions:
            child : Node = node_to_expand.child_node(self.problem, action)
            if child.state == node_to_expand.state:
                continue
            if (child.state not in self.explored) and (child.state not in self.qFrontier):
                self.qFrontier[child.state] = child
            elif child.state in self.qFrontier:
                current_frontier_node: Node = self.qFrontier[child.state]
                if current_frontier_node.path_cost > child.path_cost:
                    self.qFrontier[child.state] = child
    
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
            min_cost : int = 100_000
            min_key = str()

            for k in self.qFrontier:
                this_node: Node = self.qFrontier[k]
                if min_cost > this_node.path_cost:
                    min_cost = this_node.path_cost
                    min_key = k

            chosen_leaf : Node = self.qFrontier.pop(min_key)
            if chosen_leaf.state == self.problem.solution_state:
                return chosen_leaf
            self.explored.add(chosen_leaf.state)
            self.expandFrontier(chosen_leaf)

            if len(self.qFrontier) % 1_000 == 0:
                print('size of frontier: ' + str(len(self.qFrontier)), end='\r')
        print('\n')
