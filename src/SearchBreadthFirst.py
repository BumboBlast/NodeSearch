
from ChildNodeTest import Node
from ProblemTest import Problem
from queue import Queue
from Solver import Solver

class BrFS(Solver):
    def __init__(self, problem: Problem):
        super().__init__()
        # initialize a new random puzzle
        self.problem : Problem = problem
        self.solution: str = self.problem.solution_state
        # initialize root node
        self.root : Node = Node()
        self.root.state = self.problem.initial_state

        #initialize frontier and explored (both unique)
        
        self.qFrontier: Queue = Queue()
        self.explored: set = set()
        self.explored.add(self.root.state)
        # gen frontier
        self.expandFrontier(self.root)
        
    
    def expandFrontier(self, node_to_expand: Node):
        ''' Modifies self.qFrontier, push_backs new nodes by expanding argument node for each action.
        '''
        for action_a in self.problem.actions:
            new_frontier_node : Node = node_to_expand.child_node(self.problem, action_a)
            if new_frontier_node.state not in self.explored:
                self.qFrontier.put(new_frontier_node)

    def printFrontier(self, short: bool = False):
        # n: Node
        # for n in self.qFrontier.values():
        #     if short:
        #         print('action:\t' + str(n.action.__name__) + '  \t' + str(n.state))
        #     else:
        #         print('action: ' + str(n.action.__name__) + '\n' + Problem.print_state(n.state))
        n: Node
        for n in self.qFrontier.queue:
            if short:
                print('action:\t' + str(n.action.__name__) + '  \t' + str(n.state))
            else:
                print('action: ' + str(n.action.__name__) + '\n' + Problem.print_state(n.state))

    
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
            if (self.qFrontier.qsize()) == 0:
                print('\n', end='\n')
                print('No soltion found ):')
                return None
            # choose a leaf node and remove it from the frontier
            # since frontier is a queu (FIFO), just pop_back (.get())
            chosenLeaf: Node = self.qFrontier.get()

            # if the node contains a goal state then return the corresponding solution
            if self.solution == chosenLeaf.state:
                print('\n')
                print('breast first search, done(:')
                print('nodes explroed: ', len(self.explored))
                return chosenLeaf
            
            # add the node to the explored set
            self.explored.add(chosenLeaf.state)

            # expand the chosen node, adding the resulting nodes to the frontier
            # only if not in the frontier or explored set (coverd in genFrontier)
            self.expandFrontier(chosenLeaf)
            
            if self.qFrontier.qsize() % 10_000 == 0:
                print('size of frontier: ' + str(self.qFrontier.qsize()), end='\r')
        print('\n')