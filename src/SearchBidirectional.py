'''
Bidirection-Search

The idea behind bidirectional search is to run two simultaneous searches—one forward from the initial
state and the other backward from the goal—hoping that the two searches meet in the middle.

Bidirectional search is implemented by replacing the goal test with a check to see whether the frontiers
of the two searches intersect; if they do, a solution has been found. The check can be done when each
node is generated or selected for expansion and, with a hash table, will take constant time.

We can reduce this by roughly half if one of the two searches is done by iterative deepening, but at
least one of the frontiers must be kept in memory so that the intersection check can be done.
'''

from ChildNodeTest import Node
from ProblemTest import Problem
from collections import deque
from queue import Queue
from Solver import Solver

class Bidirection(Solver):
    def __init__(self, problem: Problem):
        super().__init__()
        # initialize a new random puzzle
        self.problem : Problem = problem
        
        # initialize root node
        self.root : Node = Node()
        self.root.state = self.problem.initial_state

        # initalize both frontiers (FIFO queue) and explored set
        self.qStartFrontier: Queue = Queue()
        self.qFinishFrontier: Queue = Queue()
        self.qStartFrontier.put(self.root)
        self.qFinishFrontier.put(Node(state=self.problem.solution_state))
        self.startDict : dict = {self.root.state : self.root}
        self.finishDict : dict = {self.problem.solution_state : Node(state=self.problem.solution_state)}
        self.explored: dict = dict()
        self.explored[self.root.state] = self.root # idk if we should add root to explored

        # stupid global to break out of BrFS loop
        self.midpoint : list = None

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
            if (self.qStartFrontier.qsize() == 0) or (self.qFinishFrontier.qsize() == 0):
                return None
            startLeaf: Node = self.qStartFrontier.get()
            finishLeaf: Node = self.qFinishFrontier.get()
            # if self.problem.solution_state == startLeaf.state:
            #     return startLeaf
            # if self.problem.solution_state == finishLeaf.state:
            #     return finishLeaf
            self.expandFrontier(startLeaf, self.qStartFrontier, self.startDict)
            self.expandFrontier(finishLeaf, self.qFinishFrontier, self.finishDict)
            self.midpoint = self.checkFrontierIntersection()
            if self.midpoint:
                # print(f'left node:{self.midpoint[0]}')
                # print(f'right node:{self.midpoint[1]}')
                return self.midpoint
                
            self.explored[startLeaf.state] = startLeaf
            self.explored[finishLeaf.state] = finishLeaf
            if len(self.explored) % 100 == 0:
                print(f'sFrontier: {self.qStartFrontier.qsize()}\tfFrontier:{self.qFinishFrontier.qsize()})', end='\r')
  

    def expandFrontier(self, node_to_expand: Node, frontier: Queue, frontierDic: dict):
        ''' Modifies self.qFrontier, push_backs new nodes by expanding argument node for each action.
        '''
        for action_a in self.problem.actions:
            new_frontier_node : Node = node_to_expand.child_node(self.problem, action_a)
            if new_frontier_node.state not in self.explored.keys():
                frontier.put(new_frontier_node)
                frontierDic[new_frontier_node.state] = new_frontier_node


    def checkFrontierIntersection(self) -> Node:
        ''' return true if frontiers intersect
        '''
        for f in self.startDict.keys():
            if f in self.finishDict.keys():
                return [self.startDict[f], self.finishDict[f]]
        return None