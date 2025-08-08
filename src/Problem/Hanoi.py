
''' Tower of Hanoi
    Represented with a 2-D array
    [
        [5, 3, 2],
        [1],
        [4]
    ]
'''

from Problem.Problem import Problem



class Hanoi(Problem):
    def __init__(self):
        self.initial_state : object
        self.solution_state : object

    def get_actions(self, state) -> list:
        ''' returns list of actions (functions) available at this state '''
        pass
    def result(self, state, action) -> object:
        ''' returns a state, given an action'''
        pass
    def step_cost(self, state, action) -> int:
        ''' returns the step cost of performing an action from a given state'''
        pass
    def check_solution(self, state: object) -> bool:
        pass
    def is_solvable(self) -> bool:
        pass
    @staticmethod
    def print_state() -> str:
        pass
    @staticmethod
    def get_solution() -> list:
        pass