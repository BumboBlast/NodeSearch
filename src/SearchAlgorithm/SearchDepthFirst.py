
from Node import Node
from Problem import Problem
from collections import deque
from SearchAlgorithm.Solver import Solver

class DpFS(Solver):
    def __init__(self, problem: Problem):
        super().__init__()
        # initialize a new random puzzle
        self.problem : Problem = problem
        self.solution: str = self.problem.solution_state
        # initialize root node
        self.root : Node = Node()
        self.root.state = self.problem.initial_state

        #initialize frontier and explored (both unique)

        self.dqFrontier: deque = deque() # FILO
        self.explored: set = set()
        # gen frontier
        self.explored.add(self.root.state) # idk if we should add root to explored
        self.expandFrontier(self.root)
    
    def expandFrontier(self, node_to_expand: Node):
        ''' Modifies self.qFrontier, push_backs new nodes by expanding argument node for each action.
        '''
        for action_a in self.problem.actions:
            new_frontier_node : Node = node_to_expand.child_node(self.problem, action_a)
            if new_frontier_node.state not in self.explored:
                # self.qFrontier.put(new_frontier_node)
                self.dqFrontier.append(new_frontier_node)
    
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
        print('Depth First: (:')
        # check if this is solvable
        if not self.problem.is_solvable():
            return None

        plsHalt = 1_000_000
        while (plsHalt > 0):
            plsHalt -= 1
            # if the frontier is empty then return failure
            if (len(self.dqFrontier)) == 0:
                print('\n', end='\n')
                print('No soltion found ):')
                return None
            # choose a leaf node and remove it from the frontier
            # since frontier is a queu (FIFO), just pop_back (.get())
            chosenLeaf: Node = self.dqFrontier.pop()

            # if the node contains a goal state then return the corresponding solution
            if self.problem.check_solution(chosenLeaf.state):
                print('\n')
                print('depth first search, done(:')
                print('nodes explroed: ', len(self.explored))
                return chosenLeaf
            
            # add the node to the explored set
            self.explored.add(chosenLeaf.state)

            # expand the chosen node, adding the resulting nodes to the frontier
            # only if not in the frontier or explored set (coverd in genFrontier)
            self.expandFrontier(chosenLeaf)
            
            if len(self.dqFrontier) % 10_000 == 0:
                print('size of frontier: ' + str(len(self.dqFrontier)), end='\r')
        print('\n')