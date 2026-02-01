

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


''' !!!!! !!!!! !!!!! Note on heapq implementation !!!!! !!!!! !!!!!
    --> heapq is just a python list []
    --> each value in the heapq is a tuple (priority, insert_id, node)

    --> the slowest thing to do in a heapq is to delete a value from the middle
    so instead of straight up deleting it (and costly re-ordering it),
    set its node as "REMOVED"
'''

REMOVED = "<removed-task>"

from Node import Node
from Problem.Problem import Problem
from queue import Queue
from SearchAlgorithm.Solver import Solver
import heapq
import itertools

class UniformCost(Solver):
    def __init__(self, problem: Problem):
        super().__init__()
        self.problem : Problem = problem
        self.solution: str = self.problem.solution_state
        self.root : Node = Node()
        self.root.state = self.problem.initial_state

        #initialize frontier and explored (both unique)
        # priority queue, ordered by path cost
        # heapFrontier contains tuple, (priority , insert_order, task)
        self.insert_order = itertools.count()
        self.heapFrontier: list = list() 
        heap_entry : list = [0, next(self.insert_order), self.root]
        heapq.heappush(self.heapFrontier, heap_entry)

        # accompany a dict for associating states with nodes
        self.frontierLKP : dict = dict()
        self.frontierLKP[self.root.state] = heap_entry

        # explored set
        self.explored: set = set()
    
    def expandFrontier(self, node_to_expand: Node):
        ''' Modifies self.qFrontier, push_backs new nodes by expanding argument node for each action.

        for each action in problem.ACTIONS (node.STATE) do
            child ← CHILD-NODE(problem, node, action)
            if child.STATE is not in explored or frontier then
                frontier ← INSERT(child ,frontier)
            else if child.STATE is in frontier with higher PATH-COST then
                replace that frontier node with child
        '''
        for action in self.problem.get_actions(node_to_expand.state):
            child : Node = node_to_expand.child_node(self.problem, action)
            if child.state not in self.explored and child.state not in self.frontierLKP:
                # add to both heap and dict
                heap_entry : list = [child.path_cost, next(self.insert_order), child]
                heapq.heappush(self.heapFrontier, heap_entry)
                self.frontierLKP[child.state] = heap_entry

            elif child.state in self.frontierLKP:
                # check if this node is better than an existing frontier node
                # replace that frontier node with child
                if self.frontierLKP[child.state][-1].path_cost > child.path_cost:
                    # remove from heap and dict
                    removed_entry = self.frontierLKP.pop(child.state)
                    removed_entry[-1] = REMOVED

                    # add new cheaper child node to heap and dict
                    heap_entry : list = [child.path_cost, next(self.insert_order), child]
                    heapq.heappush(self.heapFrontier, heap_entry)
                    self.frontierLKP[child.state] = heap_entry

            # case when new node is IN EXPLORED but not in frontier
            # means ive already seen this node, can ignore
            else:
                continue

    def search(self) -> Node | None:
        ''' 
        '''
        print('Uniform-Cost (:')
        
        # check if this is solvable
        if not self.problem.is_solvable():
            return None

        plsHalt = 10_000_000
        while (plsHalt > 0):
            plsHalt -= 1

            # if EMPTY?(frontier) then return failure
            if len(self.heapFrontier) == 0:
                return None

            # node ← POP(frontier) /* chooses the lowest-cost node in frontier */
            # remove from both heap and frontier
            chosen_leaf  = heapq.heappop(self.heapFrontier)[-1]
            while chosen_leaf == REMOVED:
                priority, insert_id, task = heapq.heappop(self.heapFrontier)
                if task is not REMOVED:
                    del self.frontierLKP[task.state]
                    chosen_leaf = task
                    # break

            # if problem.GOAL-TEST(node.STATE) then return SOLUTION(node)
            if chosen_leaf.state == self.problem.solution_state:
                print('\n')
                print('done (;\n')
                return chosen_leaf

            # add node.STATE to explored
            self.explored.add(chosen_leaf.state)

            # expand frontier
            self.expandFrontier(chosen_leaf)

            if len(self.heapFrontier) % 10_000 == 0:
                print('size of frontier: ' + str(len(self.heapFrontier)), end='\r')
 