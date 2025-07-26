'''
Iterative Deepening Search

The iterative deepening search algorithm, which repeatedly applies depth-limited search with increasing
limits. It terminates when a solution is found or if the depth-limited search returns failure, meaning
that no solution exists.

In general, iterative deepening is the preferred uninformed search method when the search space is large
and the depth of the solution is not known.
'''


from ChildNodeTest import Node
from ProblemTest import Problem
from collections import deque
from Solver import Solver

class IterativeDeepening(Solver):
    def __init__(self, problem: Problem):
        super().__init__()
        # initialize a new random puzzle
        self.problem : Problem = problem
        
        # initialize root node
        self.root : Node = Node()
        self.root.state = self.problem.initial_state

    '''
    function ITERATIVE-DEEPENING-SEARCH (problem) returns a solution, or failure
        for depth = 0 to ∞ do
            result ← DEPTH-LIMITED-SEARCH (problem, depth)
            if result != cutoff then return result

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
        for depth in range(0, 100):
            result = self.depthLimitedSearch(depth)
            # print(result)
            if result != 'cutoff':
                print('\n'); print('iterative-deepening-search, done(:')
                return result

    def depthLimitedSearch(self, limit) -> Node | str:
        # re-initialze explored set
        self.explored: dict = dict()
        self.explored[self.root.state] = self.root # idk if should add root to explored
        start_node : Node = Node(None, self.problem.initial_state)
        return self.recursive_DLS(start_node, limit)

    def recursive_DLS(self, node: Node, limit: int ) -> Node | str:
        if self.problem.solution_state == node.state:
            return node
        elif limit == 0:
            return 'cutoff'
        else:
            cutoff_occurred: bool = False
            for action in self.problem.actions:
                child_node : Node = node.child_node(self.problem, action)
                # check if explored or not
                if child_node.state in self.explored.keys():
                    continue
                self.explored[child_node.state] = child_node
                result : Node | str = self.recursive_DLS(child_node, limit - 1)
                if result == 'cutoff':
                    cutoff_occurred = True
                elif result:
                    return result
            if cutoff_occurred:
                return 'cutoff'
            else:
                return None

