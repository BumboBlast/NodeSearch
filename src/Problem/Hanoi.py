
''' Tower of Hanoi
    Represented with a 2-D array
    [
        [4, 3, 2],
        [],
        [1]
    ]
    
    one line
    [[4,3,2],[],[1]]
    hashable options?
    string '432,0,1'
    tuple {[432], [0], [1]}
'''

from Problem.Problem import Problem
import random


class Hanoi(Problem):
    DIMENSIONS = [3, 5]
    def __init__(self, init_state:list = list()):
        # if no init-state passed, make one at random
        super().__init__()
        nonhashable_init_state : list = list()
        if init_state:
            nonhashable_init_state = init_state
        else:
            new_init_state : list = list()
            for _ in range(0, self.DIMENSIONS[0]):
                new_init_state.append(list())
            for inc in range(self.DIMENSIONS[1], 0, -1):
                random_slot = random.randint(0, self.DIMENSIONS[0] - 1)
                new_init_state[random_slot].append(inc)
            nonhashable_init_state = new_init_state
        
        # self.initial_state = nonhashable_init_state
        # translate list -> something hashable (str? tuple?)
        # self.initial_state = ''.join([str(s) for s in nonhashable_init_state])
        self.initial_state = str(nonhashable_init_state)
        
    def get_actions(self, state) -> list:
        ''' returns list of actions (functions) available at this state '''
        # for each slot, get list of slots which a move_disk would be legal.
        # will be a subset of:
        # 0, 1 | 0, 2 | 1, 0 | 1, 2 | 2, 0 | 2, 1
        return [
            self.move_disk_0_1,
            self.move_disk_0_2,
            self.move_disk_1_0,
            self.move_disk_1_2,
            self.move_disk_2_0,
            self.move_disk_2_1
        ]
        
    def result(self, state, action) -> object:
        ''' returns a state, given an action.
            checks legality, if illegal state, return inputted state.
        '''
        new_state: str = action(state)
        for slot in new_state.split(']'):
            if len(slot) > 0:
                prev_disk : str = slot[0]
                for disk in slot[1:]:
                    if disk.isnumeric():
                        if prev_disk.isnumeric() and disk > prev_disk:
                            return state
                        prev_disk = disk
        return action(state)
        
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
    
    ''' Hanoi Puzzle Actions - Moving disk from stack A to stack B
        current state -> new state 
    '''
    @staticmethod
    def move_disk(current_state: list, from_slot: int, to_slot: int) -> list:
        # moves a disk regardless of legality. returns new state
        if len(current_state) > 0 and len(current_state[from_slot]) > 0:
            disk: int = current_state[from_slot].pop()
            current_state[to_slot].append(disk)
        return current_state
    
    # hard code the case with 3 slots
    @staticmethod
    def move_disk_0_1(current_state: str) -> str:
        modified: list = eval(current_state)
        try:
            modified[1].append(modified[0].pop())
        finally:
            return str(modified)
            
    @staticmethod        
    def move_disk_0_2(current_state: str) -> str:
        modified: list = eval(current_state)
        try:
            modified[2].append(modified[0].pop())
        finally:
            return str(modified)
            
    @staticmethod        
    def move_disk_1_0(current_state: str) -> str:
        modified: list = eval(current_state)
        try:
            modified[0].append(modified[1].pop())
        finally:
            return str(modified)
    
    @staticmethod
    def move_disk_1_2(current_state: str) -> str:
        modified: list = eval(current_state)
        try:
            modified[2].append(modified[1].pop())
        finally:
            return str(modified)
    
    @staticmethod
    def move_disk_2_0(current_state: str) -> str:
        modified: list = eval(current_state)
        try:
            modified[0].append(modified[2].pop())
        finally:
            return str(modified)
    
    @staticmethod
    def move_disk_2_1(current_state: str) -> str:
        modified: list = eval(current_state)
        try:
            modified[1].append(modified[2].pop())
        finally:
            return str(modified)