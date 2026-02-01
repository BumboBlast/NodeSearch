'''
Best-first (or greedy best first) search is an instance of the general TREE-SEARCH or GRAPH-SEARCH algorithm in which a node
is selected for expansion based on an evaluation function.

The evaluation function is construed as a cost estimate, so the node with the lowest evaluation is expanded
first.

This is implemented the exact same as uniform cost but instead of using node.path_cost, use evaluating function

A start (A*) search is an example pf Best-first where its evaluating function is path_cost + distance_to_solution
'''


REMOVED = "<removed-task>"

from Node import Node
from Problem.Problem import Problem
from queue import Queue
from SearchAlgorithm.Solver import Solver
import heapq
import itertools
import sys

class BestFirst(Solver):
    def __init__(self, problem: Problem):
        super().__init__()
        self.problem : Problem = problem
        self.solution: str = self.problem.solution_state
        self.root : Node = Node()
        self.root.state = self.problem.initial_state

        # obtain evaluating function from input or pick one at default
        def default_evaluating(state: str) -> int:
            return 1
        try:
            evaluating_function_input : str = sys.argv[3]
        except Exception as e:
            print(e)
            evaluating_function_input : str = ""
            
        # Get a list of methods using dir()
        methods_list = [method for method in dir(self.problem) if callable(getattr(self.problem, method))\
            and not method.startswith("__")]
        if evaluating_function_input in methods_list:
            self.evaluating_function = getattr(self.problem, evaluating_function_input)
        else:
            self.evaluating_function = default_evaluating

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
            child_evaluation : int = self.evaluating_function(child.state)
            
            if child.state not in self.explored and child.state not in self.frontierLKP:
                # add to both heap and dict
                heap_entry : list = [child_evaluation, next(self.insert_order), child]
                heapq.heappush(self.heapFrontier, heap_entry)
                self.frontierLKP[child.state] = heap_entry


                ''' TODO: do i needthis?? '''
            # elif child.state in self.frontierLKP:
            #     # check if this node is better than an existing frontier node
            #     # replace that frontier node with child
            #     if self.frontierLKP[child.state][-1].path_cost > child.path_cost:
            #         # remove from heap and dict
            #         removed_entry = self.frontierLKP.pop(child.state)
            #         removed_entry[-1] = REMOVED
                    
            #         # add new cheaper child node to heap and dict
            #         heap_entry : list = [child_evaluation, next(self.insert_order), child]
            #         heapq.heappush(self.heapFrontier, heap_entry)
            #         self.frontierLKP[child.state] = heap_entry

            # case when new node is IN EXPLORED but not in frontier
            # means ive already seen this node, can ignore
            else:
                continue

    def search(self) -> Node | None:
        ''' 
        '''
        print('Best-First(:')
        print(f"Using evaluating function: {self.evaluating_function.__name__}")
        
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

            if len(self.heapFrontier) % 1_000 == 0:
                print('size of frontier: ' + str(len(self.heapFrontier)), end='\r')
 