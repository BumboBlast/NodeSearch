'''
Bidirection-Search

The idea behind bidirectional search is to run two simultaneous searches—one forward from the initial
state and the other backward from the goal—hoping that the two searches meet in the middle.

Bidirectional search is implemented by replacing the goal test with a check to see whether the frontiers
of the two searches intersect; if they do, a solution has been found. The check can be done when each
node is generated or selected for expansion and, with a hash table, will take constant time.

We can reduce this by roughly half if one of the two searches is done by iterative deepening, but at
least one of the frontiers must be kept in memory so that the intersection check can be done.



Should each frontier have its own "explored" set?
'''

from Node import Node
from Problem import Problem
from collections import deque
from SearchAlgorithm.Solver import Solver

class Bidirection(Solver):
    def __init__(self, problem: Problem):
        super().__init__()
        # initialize a new random puzzle
        self.problem : Problem = problem
        
        # initialize root node
        self.root : Node = Node()
        self.root.state = self.problem.initial_state

        # initalize both frontiers (FIFO queue) and explored set
        self.qStartFrontier: deque = deque()
        self.qFinishFrontier: deque = deque()
        self.startDict : dict = {self.root.state : self.root}
        self.finishDict : dict = {self.problem.solution_state : Node(state=self.problem.solution_state)}
        self.qStartFrontier.appendleft(self.root.state)
        self.qFinishFrontier.appendleft(self.problem.solution_state)
        self.explored: dict = dict()
        # self.explored[self.root.state] = self.root # idk if we should add root to explored

        # stupid global to break out of BrFS loop
        self.midpoint : list = None

    @staticmethod
    def get_solution(solution_node_pair: list) -> list:
        solution_chain: list = list()
        if solution_node_pair and type(solution_node_pair) is list:
            first_half: list = Node.getNodeChainIterative(solution_node_pair[0], short=True)
            second_half: list = Node.getNodeChainIterative(solution_node_pair[1], short=True)
            second_half.reverse()
            solution_chain.extend(second_half[:-1])
            solution_chain.extend(first_half)
        return solution_chain

    ''' So i guess... modify BrFS to expand the frontier from both sides?
        Then at new node, check for intersections between both frontiers
    '''

    def search(self) -> Node | str:
        ''' Bidireciton search
        '''
        # check if this is solvable
        if not self.problem.is_solvable():
            return None
        
        ''' See src/SearchBreadthFirst.py
        '''
        plsHalt = 10_000_000
        while (plsHalt > 0):
            plsHalt -= 1
            if (len(self.qStartFrontier) == 0) or (len(self.qFinishFrontier) == 0):
                return None
            startLeafState: str = self.qStartFrontier.pop()
            finishLeafState: str = self.qFinishFrontier.pop()
            startLeaf: Node = self.startDict[startLeafState]
            finishLeaf: Node = self.finishDict[finishLeafState]

            self.expandFrontier(startLeaf, self.qStartFrontier, self.startDict)
            self.expandFrontier(finishLeaf, self.qFinishFrontier, self.finishDict)
            self.midpoint = self.checkFrontierIntersection()
            if self.midpoint:
                print('\n')
                return self.midpoint
                
            self.explored[startLeaf.state] = startLeaf
            self.explored[finishLeaf.state] = finishLeaf
            if len(self.explored) % 100 == 0:
                print(f'sFrontier: {len(self.qStartFrontier)}\tfFrontier:{len(self.qFinishFrontier)})', end='\r')

    def expandFrontier(self, node_to_expand: Node, frontier: deque, frontierDic: dict):
        ''' Modifies self.qFrontier, push_backs new nodes by expanding argument node for each action.
        '''
        for action_a in self.problem.actions:
            child : Node = node_to_expand.child_node(self.problem, action_a)
            if child.state == node_to_expand.state:
                continue
            if child.state not in self.explored:
                frontierDic[child.state] = child
                frontier.appendleft(child.state)
                


    def checkFrontierIntersection(self) -> Node:
        ''' return true if frontiers intersect
        '''
        for f in self.startDict:
            if f in self.finishDict:
                return [self.startDict[f], self.finishDict[f]]
        return None