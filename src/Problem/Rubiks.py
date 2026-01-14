''' Rubiks Cube!! (;

    State: represented as 6 arrays of 9 integers.
    
    Solved:
    [
        [0, 0, 0, 0, 0, 0, 0, 0, 0], # TOP
        [1, 1, 1, 1, 1, 1, 1, 1, 1], # FRONT
        [2, 2, 2, 2, 2, 2, 2, 2, 2], # LEFT
        [3, 3, 3, 3, 3, 3, 3, 3, 3], # BACK
        [4, 4, 4, 4, 4, 4, 4, 4, 4], # RIGHT
        [5, 5, 5, 5, 5, 5, 5, 5, 5], # BOTTOM
    ]

    Mixed up:
    [
        [1, 2, 3, 4, 0, 0, 4, 4, 0], # TOP
        [0, 2, 3, 0, 5, 3, 5, 2, 1], # FRONT
        [5, 3, 2, 5, 4, 5, 3, 3, 0], # LEFT
        [5, 4, 4, 0, 1, 0, 3, 3, 4], # BACK
        [2, 1, 1, 1, 3, 4, 5, 1, 0], # RIGHT
        [0, 2, 4, 1, 2, 2, 1, 2, 2], # BOTTOM
    ]

    white : 0
    red : 1
    orange : 5
    blue : 3
    green : 4
    yellow : 2

    How can I ensure
        1. relationship between faces and indices in array
            meaning, face 1 and face 2 are the same distance as face 4 and face 5
        2. integers represent order of colors in some standard orientation
            meaning, i can accidently rotate the rubiks cube and 
            be sure which way to orient the face im looking at.

    I could just assume these and if i end up picking up an actual rubiks cube, just try to follow that convention.
'''

from enum import Enum
from Problem.Problem import Problem
# import random

class Rubiks(Problem):
    class Color(Enum):
        WHITE = 0
        RED = 1
        ORANGE = 2
        YELLOW = 3
        GREEN = 4
        BLUE = 5
               
    def __init__(self, init_state:list = list()):
        # if no init-state passed, make one at random
        super().__init__()
        self.init_state = init_state

    def get_state(self, state) -> object:
        ''' returns state (getter) '''
        print("get state (:")
        return state

    def get_actions(self, state) -> list:
        ''' returns list of actions (functions) available at this state '''
        
    def result(self, state, action) -> object:
        ''' returns a state, given an action.
            checks legality, if illegal state, return inputted state.
        '''
        
    def step_cost(self, state, action) -> int:
        ''' returns the step cost of performing an action from a given state'''
        return 1
        
    def check_solution(self, state: object) -> bool:
        return str(state) == str(self.solution_state)
        
    def is_solvable(self) -> bool:
        ''' returns TRUE for now until i can prove which problems are solvable or not'''
        return True
    @staticmethod
    def print_state(state: str) -> str:
        return state
        
    @staticmethod
    def get_solution() -> list:
        pass
