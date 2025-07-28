'''
Depth-Limited Search

To solve infinite-depth problems, introduce a depth limiter, based off the diameter of the problem.

if the depth-limit is too shallow, (l < d), problem may be incomplete. (This is likely when d is unknown.)
if the depth-limit is too deep, (l > d), solution may be non-optimal

Notice that depth-limited search can terminate with two kinds of failure: the standard failure
value indicates no solution; the cutoff value indicates no solution within the depth limit.


I'm not sure why this isn't working. It should find any solution of depth < limit,
but this won't find any solution with limit 35, when BrFS finds solutinon of depth 29.
puzzle: '876543210'
'''


from Node import Node
from Problem import Problem
from collections import deque
from SearchAlgorithm.Solver import Solver

class DepthLimited(Solver):
    def __init__(self, problem: Problem):
        super().__init__()
        # initialize a new random puzzle
        self.problem : Problem = problem
        # self.solution: str = self.problem.solution_state # actually ,the problem already knows about this.
        # initialize root node
        self.root : Node = Node()
        self.root.state = self.problem.initial_state

        # initialze search limit
        self.limit = 50 # hardcoded
        self.explored: set = set()
        self.explored.add(self.root.state) # idk if should add root to explored

    '''
    function DEPTH-LIMITED-SEARCH (problem, limit ) returns a solution, or failure/cutoff
        return RECURSIVE-DLS(MAKE-NODE (problem.INITIAL-STATE), problem, limit)

    function RECURSIVE-DLS(node,problem,limit) returns a solution, or failure/cutoff
        if problem.GOAL-TEST (node.STATE) then return SOLUTION (node)
        else if limit = 0 then return cutoff
        else
            cutoff_occurred? ← false
            for each action in problem.ACTIONS (node.STATE) do
                child ← CHILD-NODE (problem, node, action)
                result ← RECURSIVE-DLS(child , problem, limit - 1)
                if result = cutoff then cutoff_occurred? ← true
                else if result != failure then return result
            if cutoff_occurred? then return cutoff else return failure
    '''

    def search(self) -> Node | str:
        # check if this is solvable
        if not self.problem.is_solvable():
            return None
        start_node : Node = Node(None, self.problem.initial_state)
        return self.recursive_DLS(start_node, self.limit)

    # @staticmethod
    def recursive_DLS(self, node: Node, limit: int ) -> Node | str:
        if self.problem.solution_state == node.state:
            print('\n'); print('depth-limited search, done(:')
            # print('nodes explroed: ', len(self.explored))
            return node
        elif limit == 0:
            return 'cutoff'
        else:
            cutoff_occurred: bool = False
            for action in self.problem.actions:
                child_node : Node = node.child_node(self.problem, action)
                # check if explored or not
                if child_node.state in self.explored:
                    continue
                self.explored.add(child_node.state)
                result : Node | str = self.recursive_DLS(child_node, limit - 1)
                if result == 'cutoff':
                    cutoff_occurred = True
                elif result:
                    return result
            return 'cutoff' if cutoff_occurred else None

