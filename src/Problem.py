
from itertools import combinations, permutations
import random

class Problem:
    def __init__(self):
        self.initial_state : object
        self.solution_state : object
        self.actions : list
        pass
    def result(self, state, action) -> object:
        ''' returns a state, given an action'''
        pass
    def step_cost(self, state, action) -> int:
        ''' returns the step cost of performing an action from a given state'''
        pass
    def is_solvable(self) -> bool:
        pass
    @staticmethod
    def print_state(state: str) -> str:
        '''print the state of the puzzle as a rectangle
        x = i % width;    // % is the "modulo operator", the remainder of i / width;
        y = i / width;    // where "/" is an integer division
        '''
        ret_str : str = str()
        _iter : int = 0
        for _ in range(0, EightPuzzle.DIMENSIONS[0]):
            row : list = list()
            for _ in range(0, EightPuzzle.DIMENSIONS[1]):
                row.append(state[_iter])
                _iter += 1
            ret_str += str(row) + '\n'
        return(str(ret_str))

class EightPuzzle(Problem):
    BLANK = '0'
    DIMENSIONS = [3, 3]
    def __init__(self, seed: str = ''):
        # generate initial state from seed
        super().__init__()
        _perm: list = list(permutations('012345678'))
        if seed:
            self.initial_state = seed
        else:
            _seed_index = random.randint(0, len(_perm))
            # convert tuple -> str
            self.initial_state : str  = ''.join(list(_perm[_seed_index]))
        self.actions = {
            self.moveLeft,
            self.moveRight,
            self.moveUp,
            self.moveDown
        }
        self.dimensions = [3, 3]

    @staticmethod
    def step_cost(state, action) -> int:
        ''' returns the step cost of performing an action from a given state
            all actions are same weight / cost
        '''
        return 1

    @staticmethod
    def result(state : str, action) -> str:
        ''' returns a state, given an action
        '''
        return action(state)
    
    def is_solvable(self) -> bool:
        ''' Counts inversions for self.initial_state
        an inversion is a pair of tiles in reverse order
        if inversions are even, then solvable.
        [] currently assumes solution is '012345678', blank tile is '0', and all values are numbers
        '''
        inversions : int = 0
        pairs : list = list(combinations(self.initial_state, 2))
        for p in pairs:
            if p[1] < p[0] and '0' not in [p[0], p[1]]:
                inversions += 1
        return inversions % 2 == 0

    '''Eight Puzzle Actions - Corresponding to moving the "space" tile
    '''    
    @staticmethod
    def moveLeft(this_state : str) -> object:
        '''Swap blank with the tile on the left
        '''
        _split: list = this_state.split(EightPuzzle.BLANK)
        if (len(_split[0]) % EightPuzzle.DIMENSIONS[1] == 0) or (this_state.find(EightPuzzle.BLANK) == -1):
            return this_state
        _leftChar: str = _split[0][-1]
        return _split[0][:-1] + EightPuzzle.BLANK + _leftChar + _split[1]
    @staticmethod
    def moveRight(this_state : str) -> object:
        '''Swap blank with the tile on the right
        '''
        _split: list = this_state.split(EightPuzzle.BLANK)
        if (len(_split[0]) % EightPuzzle.DIMENSIONS[1]) == (EightPuzzle.DIMENSIONS[1] - 1): return this_state
        _rightChar: str = _split[1][0]
        new_state: str = _split[0] + _rightChar + EightPuzzle.BLANK + _split[1][1:]
        return new_state
    @staticmethod
    def moveUp(this_state : str) -> object:
        '''Swap blank with the tile above
        '''
        _blankIndex = this_state.find(EightPuzzle.BLANK)
        _upIndex = _blankIndex - EightPuzzle.DIMENSIONS[1]
        if _upIndex < 0: return this_state
        new_state: str = this_state[:_upIndex] + EightPuzzle.BLANK + this_state[_upIndex+1:_blankIndex] \
            + this_state[_upIndex] + this_state[_blankIndex+1:]
        return new_state
    @staticmethod
    def moveDown(this_state : str) -> str:
        '''Swap blank with the tile below
        '''
        _blankIndex = this_state.find(EightPuzzle.BLANK)
        _downIndex = _blankIndex + EightPuzzle.DIMENSIONS[1]
        if _downIndex >= len(this_state): return this_state
        
        new_state: str = this_state[:_blankIndex] + this_state[_downIndex] + this_state[_blankIndex+1:_downIndex]\
              + EightPuzzle.BLANK + this_state[_downIndex+1:]
        return new_state