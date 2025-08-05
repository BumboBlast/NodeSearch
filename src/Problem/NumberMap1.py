''' Number Map 1: Figureate Chain
    Project Euler 61: https://projecteuler.net/problem=61

    Number 8134 maps to numbers that start with "34" or ends with "81"
    Numbers also have types (which poly function they could be from)
    example:
        8134 -> [3456, 3412, 5681]          | type      8134 -> [3, 4]
        3456 -> [8134, 5677]                | type      3456 -> [8]
    and so on.


    A state is a given chain consecutivley connected nodes on the map
    exmaple:
        8134, 3456, 5612, 1249
    
    Initial State could be any single node (chain size 1)
    example:
        8134    
    
    A solution is a chain of 6 length where the back could map to the front
    A solution ALSO requires representaiton from all 6 poly funciton types
    example:
    Nodes:  8134,   3456,   5612,   1249,   4977,   7781
    Types:  3,      5,      8,      7,      6,      4
    
    Actions:
        for each node in frontier:
            append_node()
'''

from Problem.Problem import Problem
from collections import deque

class FigurateChain(Problem):
    def __init__(self, initial_state: deque, node_map: dict, type_map: dict):
        super().__init__()
        self.initial_state: deque = initial_state
        self.node_map : dict = node_map
        self.node_type_map : dict = type_map 

    @staticmethod
    def step_cost(state: str, action: function) -> int:
        ''' returns the step cost of performing an action from a given state
            all actions are same weight / cost
        '''
        return 1

    def check_solution(self, state: object) -> bool:
        ''' Check if given figurate-chain is of 6 length
        '''
        return False

    @staticmethod
    def result(state : str, action: function) -> str:
        ''' returns a state, given an action
        '''
        return action(state)
    @staticmethod
    def is_solvable() -> bool:
        ''' assume this problem is solvable '''
        return True
    def get_actions(self, state: str) -> list:
        ''' return list of functions that evaluate to the next step
        '''
        action_list : list = list()
        for action_result in self.node_map[state]:
            def f(state: str) -> str:
                return action_result
            action_list.append(f)
        return action_list
    @staticmethod
    def print_state(state: str) -> str:
        '''
        '''
    
    def print_map(self) -> str:
        '''
        '''