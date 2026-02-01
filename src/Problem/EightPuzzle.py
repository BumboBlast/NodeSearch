from Problem.Problem import Problem
from itertools import combinations, permutations
import random
import math

class EightPuzzle(Problem):
    BLANK = '0'
    STATE_SPACE = '0123456789ABCDEFGHIKLMNOPRSTUVWXYZa'

    # dynamic class attr
    dimensions = [None, None]
    row_convert : list = list()
    col_convert : list = list()


    def __init__(self, init_state: str = None):
        super().__init__()
        if init_state:
            self.initial_state = init_state
        else:
            self.initial_state = self.get_random_state()
        
        # dynamic class attr
        EightPuzzle.dimensions[0] = int(math.sqrt(len(self.initial_state)))
        EightPuzzle.dimensions[1] = int(math.sqrt(len(self.initial_state)))
        EightPuzzle.row_convert  = [i // EightPuzzle.dimensions[1] for i in range(0, EightPuzzle.dimensions[0] * EightPuzzle.dimensions[1])]
        EightPuzzle.col_convert  = [i % EightPuzzle.dimensions[0] for i in range(0, EightPuzzle.dimensions[0] * EightPuzzle.dimensions[1])]

        # instance attr (might as well be class)
        self.solution_state = EightPuzzle.STATE_SPACE[0 : EightPuzzle.dimensions[0] * EightPuzzle.dimensions[1]]

    def get_random_state(self) -> str:
        ''' quickly generate a random state with given dimensions
        '''
        ls_state_space : list = list(EightPuzzle.STATE_SPACE[0 : EightPuzzle.DIMENSIONS[0] * EightPuzzle.DIMENSIONS[1]])
        random.shuffle(ls_state_space)
        random_state : str = "".join( x for x in ls_state_space)
        return random_state
            
    def get_actions(self, state) -> list:
        ''' each state, you can move any direction 
            if you try to move into the wall, just returns arg state
        '''
        return [
            self.moveLeft,
            self.moveRight,
            self.moveUp,
            self.moveDown
        ]

    @staticmethod
    def step_cost(state, action) -> int:
        ''' returns the step cost of performing an action from a given state
            all actions are same weight / cost
        '''
        return 1

    def check_solution(self, state: object) -> bool:
        ''' Return true is [state] is solution state
        '''
        return state == self.solution_state

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

        if EightPuzzle.DIMENSIONS[0] == 3:

            inversions : int = 0
            pairs : list = list(combinations(self.initial_state, 2))
            for p in pairs:
                if p[1] < p[0] and '0' not in [p[0], p[1]]:
                    inversions += 1
            print(f"solvable?: {str(bool(inversions % 2 == 0))}")
            return inversions % 2 == 0
        
        elif EightPuzzle.DIMENSIONS[0] == 4:
            inversions : int = 0
            pairs : list = list(combinations(self.initial_state, 2))
            for p in pairs:
                if p[1] < p[0] and '0' not in [p[0], p[1]]:
                    inversions += 1
            empty_space_row = (self.initial_state.index(EightPuzzle.BLANK) // EightPuzzle.DIMENSIONS[0]) # 4
            return (inversions + empty_space_row) % 2 == 0

    @staticmethod
    def print_state(state: str, short: bool = False) -> str:
        '''print the state of the puzzle as a rectangle
        x = i % width;    // % is the "modulo operator", the remainder of i / width;
        y = i / width;    // where "/" is an integer division
        '''
        if short:
            return state
        ret_str : str = str()
        _iter : int = 0
        for _ in range(0, EightPuzzle.DIMENSIONS[0]):
            row : list = list()
            for _ in range(0, EightPuzzle.DIMENSIONS[1]):
                row.append(state[_iter])
                _iter += 1
            ret_str += str(row) + '\n'
        return(ret_str)

    '''Eight Puzzle Actions - Corresponding to moving the "space" tile
    '''    
    @classmethod
    def moveLeft(cls, this_state: str) -> str:
        ''' Swap blank with the tile on the left
            if left is O.B., return this-state
            index of LEFT tile is same row, -1 column
        ''' 
        blank_ndx : int = this_state.index(cls.BLANK)
        blank_row : int = blank_ndx // cls.dimensions[1] # num cols
        blank_col : int = blank_ndx % cls.dimensions[0] # num rows

        # if blank already in left column
        if blank_col == 0:
            return this_state

        # which number [0 .. n] is b div N  AND (b mod N) - 1
        left_ndx : int = -1
        for i in range(0, len(this_state)):
            if cls.row_convert[i] == blank_row and cls.col_convert[i] == blank_col - 1:
                left_ndx = i
                break

        # swap blankndx and leftndx
        strlst = list(this_state)
        strlst[blank_ndx], strlst[left_ndx] = strlst[left_ndx], strlst[blank_ndx]
        return "".join(strlst)

    @classmethod
    def moveRight(cls, this_state: str) -> str:
        ''' Swap blank with the tile on the right
            if right is O.B., return this-state
            index of RIGHT tile is same row, +1 column
        ''' 
        blank_ndx : int = this_state.index(cls.BLANK)
        blank_row : int = blank_ndx // cls.dimensions[1] # num cols
        blank_col : int = blank_ndx % cls.dimensions[0] # num rows

        # if blank already in right column. - 1 because 0 indexed
        if blank_col == cls.dimensions[1] - 1:
            return this_state

        # which number [0 .. n] is b div N  AND (b mod N) + 1
        right_ndx : int = -1
        for i in range(0, len(this_state)):
            if cls.row_convert[i] == blank_row and cls.col_convert[i] == blank_col + 1:
                right_ndx = i
                break

        # swap blankndx and right_ndx
        strlst = list(this_state)
        strlst[blank_ndx], strlst[right_ndx] = strlst[right_ndx], strlst[blank_ndx]
        return "".join(strlst)

    @classmethod
    def moveUp(cls, this_state: str) -> str:
        ''' Swap blank with the tile above
            if up is O.B., return this-state
            index of UP tile is same col, -1 row
        ''' 
        blank_ndx : int = this_state.index(cls.BLANK)
        blank_row : int = blank_ndx // cls.dimensions[1] # num cols
        blank_col : int = blank_ndx % cls.dimensions[0] # num rows

        # if blank already in top row. 
        if blank_row == 0:
            return this_state

        # which number [0 .. n] is (b div N) - 1  AND b mod N
        up_ndx : int = -1
        for i in range(0, len(this_state)):
            if cls.row_convert[i] == blank_row - 1 and cls.col_convert[i] == blank_col:
                up_ndx = i
                break
        
        # swap blankndx and leftndx
        strlst = list(this_state)
        strlst[blank_ndx], strlst[up_ndx] = strlst[up_ndx], strlst[blank_ndx]
        return "".join(strlst)

    # @staticmethod
    # def moveDown(this_state : str) -> str:
    #     '''Swap blank with the tile below
    #     '''
    #     _blankIndex = this_state.find(EightPuzzle.BLANK)
    #     _downIndex = _blankIndex + EightPuzzle.DIMENSIONS[1]
    #     if _downIndex >= len(this_state): return this_state
        
    #     new_state: str = this_state[:_blankIndex] + this_state[_downIndex] + this_state[_blankIndex+1:_downIndex]\
    #           + EightPuzzle.BLANK + this_state[_downIndex+1:]
    #     return new_state

    @classmethod
    def moveDown(cls, this_state: str) -> str:
        ''' Swap blank with the tile below
            if down is O.B., return this-state
            index of DOWN tile is same col, +1 row
        ''' 
        blank_ndx : int = this_state.index(cls.BLANK)
        blank_row : int = blank_ndx // cls.dimensions[1] # num cols
        blank_col : int = blank_ndx % cls.dimensions[0] # num rows

        # if blank already in bottom row. - 1 because of 0 indexed 
        if blank_row == cls.dimensions[0] - 1:
            return this_state

        # which number [0 .. n] is (b div N) - 1  AND b mod N
        down_ndx : int = -1
        for i in range(0, len(this_state)):
            if cls.row_convert[i] == blank_row + 1 and cls.col_convert[i] == blank_col:
                down_ndx = i
                break
        
        # swap blankndx and leftndx
        strlst = list(this_state)
        strlst[blank_ndx], strlst[down_ndx] = strlst[down_ndx], strlst[blank_ndx]
        return "".join(strlst)


    ''' ------------ Evaluating Functions as Heuristics ----------
    '''

    @staticmethod
    def manhattanDistance(state: str) -> int:
        ''' return the sum of the manhattan distances for each tile in the eight puzzle
        manhattan distance means counting the number of vert/horiz spaces away a tile is from its solution.

        for each tile:
            Manhattan Distance = (row diff + col diff)
            col diff = tileValue div 3 - tileIndex div 3
            tow diff = tileValue mod 3 - tileIndex mod 3
        '''
        sum : int = 0
        for i in range(0, len(state)):
            # tile value
            tv : int = int(state[i])
            # Manhattan Distance = (row diff + col diff)
            md : int = abs((tv // 3) - (i // 3)) + abs((tv % 3) - (i % 3))
            sum += md
        return md
    
    @staticmethod
    def displacedCount(state: str) -> int:
        ''' return the count of tiles which are displaced at all
        '''
        cnt : int = 0
        for i in range(0, len(state)):
            if state[i] != i:
                cnt += 1
        return cnt