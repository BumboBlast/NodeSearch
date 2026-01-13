
'''
'''

from Problem.Problem import Problem
# import random


class Rubiks(Problem):
    # DIMENSIONS = [3, 5]
    def __init__(self, init_state:list = list()):
        # if no init-state passed, make one at random
        super().__init__()
        
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