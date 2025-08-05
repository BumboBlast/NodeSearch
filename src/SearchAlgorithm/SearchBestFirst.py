'''
Best-first search is an instance of the general TREE-SEARCH or GRAPH-SEARCH algorithm in which a node
is selected for expansion based on an evaluation function.

The evaluation function is construed as a cost estimate, so the node with the lowest evaluation is expanded
first.
'''


from Node import Node
from Problem.Problem import Problem
from collections import deque
from queue import Queue
from Solver import Solver

class BestFirst(Solver):
    def __init__(self, problem: Problem):
        super().__init__()
        # initialize a new random puzzle
        self.problem : Problem = problem
        
        # initialize root node
        self.root : Node = Node()
        self.root.state = self.problem.initial_state

    '''
    '''

    def search(self) -> Node | str:
        ''' Best First search
            Implementation similar to Uniform-Cost search

            
        '''
        # check if this is solvable
        if not self.problem.is_solvable():
            return None
        
        ''' See src/SearchBreadthFirst.py
        '''
        plsHalt = 10_000_000
        while (plsHalt > 0):
            plsHalt -= 1