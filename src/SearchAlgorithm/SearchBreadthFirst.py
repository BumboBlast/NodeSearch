
from Node import Node
from Problem.Problem import Problem
from collections import deque
from SearchAlgorithm.Solver import Solver


class BrFS(Solver):
    def __init__(self, problem: Problem):
        super().__init__()
        # initialize a new random puzzle
        self.problem : Problem = problem
        self.solution: str = self.problem.solution_state
        # initialize root node
        self.root : Node = Node()
        self.root.set_state(self.problem.initial_state)
        
        # initialize frontier and explored (both unique)
        self.qFrontier: deque = deque()
        self.explored: set = set()
        # problem "gets the state" so it can optionally return a hashable.
        self.explored.add(problem.get_state(self.root.state))
        # gen frontier
        self.expandFrontier(self.root)

    ''' -------------- SEARCH -----------------
    '''
        
    def expandFrontier(self, node_to_expand: Node):
        ''' Modifies self.qFrontier, push_backs new nodes by expanding argument node for each action.
        '''
        for action_a in self.problem.get_actions(node_to_expand.get_state()):
            new_frontier_node : Node = node_to_expand.child_node(self.problem, action_a)
            if new_frontier_node.get_state() not in self.explored:
                self.qFrontier.appendleft(new_frontier_node)

    def search(self) -> Node | None:
        '''
        Function GRAPH-SEARCH (problem) returns a solution, or failure
        initialize the frontier using the initial state of problem
        initialize the explored set to be empty
        loop do
        if the frontier is empty then return failure
        choose a leaf node and remove it from the frontier
        if the node contains a goal state then return the corresponding solution
        add the node to the explored set
        expand the chosen node, adding the resulting nodes to the frontier
        only if not in the frontier or explored set
        '''
        print('Breadth First: (:')

        # check if this is solvable
        if not self.problem.is_solvable():
            return None

        plsHalt = 10_000_000
        while (plsHalt > 0):
            plsHalt -= 1
            # if the frontier is empty then return failure
            if len(self.qFrontier) == 0:
                print('\n', end='\n')
                print('No soltion found ):')
                return None
            # choose a leaf node and remove it from the frontier
            # since frontier is a queu (FIFO), just pop_back (.get())
            chosenLeaf: Node = self.qFrontier.pop()

            # if the node contains a goal state then return the corresponding solution
            if self.problem.check_solution(chosenLeaf.get_state()):
                print('\n')
                print('breast first search, done(:')
                print('nodes explroed: ', len(self.explored))
                return chosenLeaf
            
            # add the node to the explored set
            self.explored.add(chosenLeaf.get_state())

            # expand the chosen node, adding the resulting nodes to the frontier
            # only if not in the frontier or explored set (coverd in genFrontier)
            self.expandFrontier(chosenLeaf)
            
            if len(self.qFrontier) % 10_000 == 0:
                print('size of frontier: ' + str(len(self.qFrontier)), end='\r')
        print('\n')