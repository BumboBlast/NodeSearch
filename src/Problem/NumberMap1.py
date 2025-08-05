''' Number Map 1: Figureate Chain

    Number 8134 maps to numbers that start with "34" or ends with "81"
    example:
        8134 -> [3456, 3412, 5681]
        3456 -> [8134, 5677]
    
    and so on
'''

from Problem.Problem import Problem

class FigurateChain(Problem):
    def __init__(self, initial_state: str, four_digit_map: dict):
        super().__init__()
        self.initial_state: str = initial_state
        self.map :dict = four_digit_map

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
        return True
    def get_actions(self, state: str) -> list:
        ''' return list of functions that evaluate to the next step
        '''
        action_list : list = list()
        for action_result in self.map[state]:
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