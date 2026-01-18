import random


class Problem:
    def __init__(self):
        self.initial_state : object
        self.solution_state : object

    def get_state(self, state) -> object:
        ''' returns state (getter)'''
        return state

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
    def print_state(state: str) -> str:
        pass
    @staticmethod
    def get_solution() -> list:
        pass
    
    def gen_random_solvable_state(self, start_state: object, depth=10) -> object:
        ''' apply random actions (depth times) to achieve a randomly gen cube
        '''
        action_list : list = self.get_actions(start_state)
        mut = start_state
        for d in range(0, depth):
            random_index: int = random.randrange(0, len(action_list))
            random_action: function = action_list[random_index]
            mut = random_action(mut)
        return mut