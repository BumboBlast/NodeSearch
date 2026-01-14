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

ASSUMPTION: Directions mean the following:
            Cube is held in front of viewer and directions always refer to teh same face regardless of actions
            meaning entire cube is never rotated at once

            TOP means highest face, pointed to the sky.
                TOP values start furthest-left away from viewer, left -> right up -> down
            FRONT means closest face to viewer
                FRONT values start top-left away from viewer, left -> right up -> down
            LEFT means face to the left of FRONT
                LEFT values start furthest-up away from viewer, left -> right up -> down
            BACK means opposite FRONT
                FRONT values start top-right away from viewer, right -> left, up -> down
            RIGHT means opposite LEFT
                RIGHT values start closest-up to the viewer, left-> right up -> down
            BOTTOM means opposite top
                BOTTOM values start closest-left from the viewer, left -> right up -> down
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
    
    class Face(Enum):
        TOP = 0
        FRONT = 1
        LEFT = 2
        BACK = 3
        RIGHT = 4
        BOTTOM = 5
               
    def __init__(self, init_state:list = list()):
        # if no init-state passed, make one at random
        super().__init__()
        self.init_state = init_state

    def get_state(self, state) -> object:
        ''' returns state (getter) '''
        print("get state (:")
        return str(state)

    def get_actions(self, state) -> list:
        ''' each state, you can always perform the same actions
        '''
        return [
            self.rotateTopCW,
            self.rotateTopCCW,
            self.rotateFrontCW,
            self.rotateFrontCCW,
            self.rotateLeftCW,
            self.rotateLeftCCW,
            self.rotateBackCW,
            self.rotateBackCCW,
            self.rotateRightCW,
            self.rotateRightCCW,
            self.rotateBackCW,
            self.rotateBackCCW,
            self.rotateBottomCW,
            self.rotateBottomCCW
        ]
        
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


    '''Rubiks Cube Actions - Corresponding to rotating each face either positively (CW) or negatively (CCW)

            Counter-Clockwise (CCW)     Clockwiswe (CW)         
            a b c       c f i           a b c       g d a
            d e f ->    b e h           d e f ->    h e b
            g h i       a d g           g h i       i f c
        
        but a rotation also affects other faces.
        TOP     affects Left, Right, Back, Front
        FRONT   affects Top, Left, Right, Bottom
        LEFT    affects Top, Front, Back, Bottom
        BACK    affects Top, Left, Right, Bottom
        RIGHT   affects Top, Back, Bottom, Front
        BOTTOM  affects Left, Right, Back, Front

        ASSUMPTION: Directions mean the following:
            Cube is held in front of viewer and directions always refer to teh same face regardless of actions
            meaning entire cube is never rotated at once

            TOP means highest face, pointed to the sky.
                TOP values start furthest-left away from viewer, left -> right up -> down
            FRONT means closest face to viewer
                FRONT values start top-left away from viewer, left -> right up -> down
            LEFT means face to the left of FRONT
                LEFT values start furthest-up away from viewer, left -> right up -> down
            BACK means opposite FRONT
                FRONT values start top-right away from viewer, right -> left, up -> down
            RIGHT means opposite LEFT
                RIGHT values start closest-up to the viewer, left-> right up -> down
            BOTTOM means opposite top
                BOTTOM values start closest-left from the viewer, left -> right up -> down
        

        [] instead of 12 functions, could have switch statement.
        only difference between the functions is 
            the top bit / bottom bit  (same per face) (6 faces)
            the middle bit (same per rotation type) (2 rotations)
        so 12 cases probably only 1/10th the line count

    '''   
    @staticmethod
    def rotateFaceNoCascade(face: list, clockwise : bool) -> list:
        ''' helper function to rotate a face without touchiung any other faces
            return 
            Counter-Clockwise (CCW)     Clockwiswe (CW)         
            a b c       c f i           a b c       g d a
            d e f ->    b e h           d e f ->    h e b
            g h i       a d g           g h i       i f c
        '''
        if clockwise:
            return [
                face[6], face[3], face[0],
                face[7], face[4], face[1],
                face[8], face[5], face[2],
            ]
        else: # counter clock wise
            return [
                face[2], face[5], face[8],
                face[1], face[4], face[7],
                face[0], face[3], face[6],
        ]

    @staticmethod
    def rotateTopCW(this_state : dict) -> object:
        # get current state, by assining this_state faces to relative cube as if you were always moving the TOP face
        # [] make case statement instead of having 12 functions
        relative_cube : dict = this_state.copy()
        rel_top_face : list = relative_cube[Rubiks.Face.TOP].copy()
        rel_front_face : list = relative_cube[Rubiks.Face.FRONT].copy()
        rel_left_face : list = relative_cube[Rubiks.Face.LEFT].copy()
        rel_back_face : list = relative_cube[Rubiks.Face.BACK].copy()
        rel_right_face : list = relative_cube[Rubiks.Face.RIGHT].copy()

        # make new state
        new_rel_top_face : list = [
            rel_top_face[6], rel_top_face[3], rel_top_face[0],
            rel_top_face[7], rel_top_face[4], rel_top_face[1],
            rel_top_face[8], rel_top_face[5], rel_top_face[2],
        ]
        new_rel_front_face : list = [
            rel_right_face[0], rel_right_face[1], rel_right_face[2],
            rel_front_face[3], rel_front_face[4], rel_front_face[5],
            rel_front_face[6], rel_front_face[7], rel_front_face[8],
        ]
        new_rel_left_face : list = [
            rel_front_face[0], rel_front_face[1], rel_front_face[2],
            rel_left_face[3], rel_left_face[4], rel_left_face[5],
            rel_left_face[6], rel_left_face[7], rel_left_face[8],
        ]
        new_rel_back_face : list = [
            rel_left_face[0], rel_left_face[1], rel_left_face[2],
            rel_back_face[3], rel_back_face[4], rel_back_face[5],
            rel_back_face[6], rel_back_face[7], rel_back_face[8],
        ]
        new_rel_right_face : list = [
            rel_back_face[0], rel_back_face[1], rel_back_face[2],
            rel_right_face[3], rel_right_face[4], rel_right_face[5],
            rel_right_face[6], rel_right_face[7], rel_right_face[8],
        ]

        # assign new state
        new_state = this_state.copy()
        new_state[Rubiks.Face.TOP] = new_rel_top_face
        new_state[Rubiks.Face.FRONT] = new_rel_front_face
        new_state[Rubiks.Face.LEFT] = new_rel_left_face
        new_state[Rubiks.Face.BACK] = new_rel_back_face
        new_state[Rubiks.Face.RIGHT] = new_rel_right_face
        return new_state










    @staticmethod 
    def rotateTopCCW(this_state : dict) -> object:
        # get current state, by assining this_state faces to relative cube as if you were always moving the TOP face
        # [] make case statement instead of having 12 functions
        relative_cube : dict = this_state.copy()
        rel_top_face : list = relative_cube[Rubiks.Face.TOP].copy()
        rel_front_face : list = relative_cube[Rubiks.Face.FRONT].copy()
        rel_left_face : list = relative_cube[Rubiks.Face.LEFT].copy()
        rel_back_face : list = relative_cube[Rubiks.Face.BACK].copy()
        rel_right_face : list = relative_cube[Rubiks.Face.RIGHT].copy()

        # make new state
        new_rel_top_face : list = [
            rel_top_face[2], rel_top_face[5], rel_top_face[8],
            rel_top_face[1], rel_top_face[4], rel_top_face[7],
            rel_top_face[0], rel_top_face[3], rel_top_face[6],
        ]
        new_rel_front_face : list = [
            rel_left_face[0], rel_left_face[1], rel_left_face[2],
            rel_front_face[3], rel_front_face[4], rel_front_face[5],
            rel_front_face[6], rel_front_face[7], rel_front_face[8],
        ]
        new_rel_left_face : list = [
            rel_back_face[0], rel_back_face[1], rel_back_face[2],
            rel_left_face[3], rel_left_face[4], rel_left_face[5],
            rel_left_face[6], rel_left_face[7], rel_left_face[8],
        ]
        new_rel_back_face : list = [
            rel_right_face[0], rel_right_face[1], rel_right_face[2],
            rel_back_face[3], rel_back_face[4], rel_back_face[5],
            rel_back_face[6], rel_back_face[7], rel_back_face[8],
        ]
        new_rel_right_face : list = [
            rel_front_face[0], rel_front_face[1], rel_front_face[2],
            rel_right_face[3], rel_right_face[4], rel_right_face[5],
            rel_right_face[6], rel_right_face[7], rel_right_face[8],
        ]

        # assign new state
        new_state = this_state.copy()
        new_state[Rubiks.Face.TOP] = new_rel_top_face
        new_state[Rubiks.Face.FRONT] = new_rel_front_face
        new_state[Rubiks.Face.LEFT] = new_rel_left_face
        new_state[Rubiks.Face.BACK] = new_rel_back_face
        new_state[Rubiks.Face.RIGHT] = new_rel_right_face
        new_state[Rubiks.Face.BOTTOM] = new_state[Rubiks.Face.BOTTOM]
        return new_state










    @staticmethod
    def rotateFrontCW(this_state : dict) -> object:
        # get current state, by assining this_state faces to relative cube as if you were always moving the TOP face
        # [] make case statement instead of having 12 functions
        # same as if front face was on top, bottom face was on front, ohh but then left / right would be rotate ):
        relative_cube : dict = this_state.copy()
        rel_top_face : list = relative_cube[Rubiks.Face.FRONT].copy()
        rel_front_face : list = relative_cube[Rubiks.Face.BOTTOM].copy()
        rel_left_face : list = Rubiks.rotateFaceNoCascade(relative_cube[Rubiks.Face.LEFT].copy(), clockwise=False)
        rel_back_face : list = relative_cube[Rubiks.Face.TOP].copy()
        rel_right_face : list = Rubiks.rotateFaceNoCascade(relative_cube[Rubiks.Face.RIGHT].copy(), clockwise=True)

        # make new state
        new_rel_top_face : list = [
            rel_top_face[6], rel_top_face[3], rel_top_face[0],
            rel_top_face[7], rel_top_face[4], rel_top_face[1],
            rel_top_face[8], rel_top_face[5], rel_top_face[2],
        ]
        new_rel_front_face : list = [
            rel_right_face[0], rel_right_face[1], rel_right_face[2],
            rel_front_face[3], rel_front_face[4], rel_front_face[5],
            rel_front_face[6], rel_front_face[7], rel_front_face[8],
        ]
        new_rel_left_face : list = [
            rel_front_face[0], rel_front_face[1], rel_front_face[2],
            rel_left_face[3], rel_left_face[4], rel_left_face[5],
            rel_left_face[6], rel_left_face[7], rel_left_face[8],
        ]
        new_rel_back_face : list = [
            rel_left_face[0], rel_left_face[1], rel_left_face[2],
            rel_back_face[3], rel_back_face[4], rel_back_face[5],
            rel_back_face[6], rel_back_face[7], rel_back_face[8],
        ]
        new_rel_right_face : list = [
            rel_back_face[0], rel_back_face[1], rel_back_face[2],
            rel_right_face[3], rel_right_face[4], rel_right_face[5],
            rel_right_face[6], rel_right_face[7], rel_right_face[8],
        ]

        # assign new state (rotate back from relative to original orientation)
        new_state = this_state.copy()
        new_state[Rubiks.Face.TOP] =  new_rel_back_face
        new_state[Rubiks.Face.FRONT] = new_rel_top_face
        new_state[Rubiks.Face.LEFT] = Rubiks.rotateFaceNoCascade(new_rel_left_face, clockwise=True)
        new_state[Rubiks.Face.BACK] = new_state[Rubiks.Face.BACK] # doesnt move
        new_state[Rubiks.Face.RIGHT] = Rubiks.rotateFaceNoCascade(new_rel_right_face, clockwise=False)
        new_state[Rubiks.Face.BOTTOM] = new_rel_front_face
        return new_state










    @staticmethod
    def rotateFrontCCW(this_state : dict) -> object:
        # get current state, by assining this_state faces to relative cube as if you were always moving the TOP face
        # [] make case statement instead of having 12 functions
        # same as if front face was on top, bottom face was on front, ohh but then left / right would be rotate ):
        relative_cube : dict = this_state.copy()
        rel_top_face : list = relative_cube[Rubiks.Face.FRONT].copy()
        rel_front_face : list = relative_cube[Rubiks.Face.BOTTOM].copy()
        rel_left_face : list = Rubiks.rotateFaceNoCascade(relative_cube[Rubiks.Face.LEFT].copy(), clockwise=False)
        rel_back_face : list = relative_cube[Rubiks.Face.TOP].copy()
        rel_right_face : list = Rubiks.rotateFaceNoCascade(relative_cube[Rubiks.Face.RIGHT].copy(), clockwise=True)

        # make new state
        new_rel_top_face : list = [
            rel_top_face[2], rel_top_face[5], rel_top_face[8],
            rel_top_face[1], rel_top_face[4], rel_top_face[7],
            rel_top_face[0], rel_top_face[3], rel_top_face[6],
        ]
        new_rel_front_face : list = [
            rel_left_face[0], rel_left_face[1], rel_left_face[2],
            rel_front_face[3], rel_front_face[4], rel_front_face[5],
            rel_front_face[6], rel_front_face[7], rel_front_face[8],
        ]
        new_rel_left_face : list = [
            rel_back_face[0], rel_back_face[1], rel_back_face[2],
            rel_left_face[3], rel_left_face[4], rel_left_face[5],
            rel_left_face[6], rel_left_face[7], rel_left_face[8],
        ]
        new_rel_back_face : list = [
            rel_right_face[0], rel_right_face[1], rel_right_face[2],
            rel_back_face[3], rel_back_face[4], rel_back_face[5],
            rel_back_face[6], rel_back_face[7], rel_back_face[8],
        ]
        new_rel_right_face : list = [
            rel_front_face[0], rel_front_face[1], rel_front_face[2],
            rel_right_face[3], rel_right_face[4], rel_right_face[5],
            rel_right_face[6], rel_right_face[7], rel_right_face[8],
        ]

        # assign new state (rotate back from relative to original orientation)
        new_state = this_state.copy()
        new_state[Rubiks.Face.TOP] =  new_rel_back_face
        new_state[Rubiks.Face.FRONT] = new_rel_top_face
        new_state[Rubiks.Face.LEFT] = Rubiks.rotateFaceNoCascade(new_rel_left_face, clockwise=True)
        new_state[Rubiks.Face.BACK] = new_state[Rubiks.Face.BACK] # doesnt move
        new_state[Rubiks.Face.RIGHT] = Rubiks.rotateFaceNoCascade(new_rel_right_face, clockwise=False)
        new_state[Rubiks.Face.BOTTOM] = new_rel_front_face
        return new_state










    @staticmethod # fix me
    def rotateLeftCW(this_state : dict) -> object:
        # get current state, by assining this_state faces to relative cube as if you were always moving the TOP face
        # [] make case statement instead of having 12 functions
        # same as if left was on top AND rotated CCW?
        # then front face would rotate, but since CCW it moves to right
        # then bottom face would move to new left, but since CCW it moves to front and rotated?
        # new left face is now old back rotated CCW?
        # new back face is now old top face rotated CW?
        relative_cube : dict = this_state.copy()
        rel_top_face : list = Rubiks.rotateFaceNoCascade(relative_cube[Rubiks.Face.LEFT].copy(), clockwise=False) # good
        rel_front_face : list = Rubiks.rotateFaceNoCascade(relative_cube[Rubiks.Face.BOTTOM].copy(), clockwise=True) # good
        rel_left_face : list = Rubiks.rotateFaceNoCascade(relative_cube[Rubiks.Face.BACK].copy(), clockwise=False) # good
        rel_back_face : list = Rubiks.rotateFaceNoCascade(relative_cube[Rubiks.Face.TOP].copy(), clockwise=False) # good
        rel_right_face : list = Rubiks.rotateFaceNoCascade(relative_cube[Rubiks.Face.FRONT].copy(), clockwise=True) # good

        # make new state
        new_rel_top_face : list = [
            rel_top_face[6], rel_top_face[3], rel_top_face[0],
            rel_top_face[7], rel_top_face[4], rel_top_face[1],
            rel_top_face[8], rel_top_face[5], rel_top_face[2],
        ]
        new_rel_front_face : list = [
            rel_right_face[0], rel_right_face[1], rel_right_face[2],
            rel_front_face[3], rel_front_face[4], rel_front_face[5],
            rel_front_face[6], rel_front_face[7], rel_front_face[8],
        ]
        new_rel_left_face : list = [
            rel_front_face[0], rel_front_face[1], rel_front_face[2],
            rel_left_face[3], rel_left_face[4], rel_left_face[5],
            rel_left_face[6], rel_left_face[7], rel_left_face[8],
        ]
        new_rel_back_face : list = [
            rel_left_face[0], rel_left_face[1], rel_left_face[2],
            rel_back_face[3], rel_back_face[4], rel_back_face[5],
            rel_back_face[6], rel_back_face[7], rel_back_face[8],
        ]
        new_rel_right_face : list = [
            rel_back_face[0], rel_back_face[1], rel_back_face[2],
            rel_right_face[3], rel_right_face[4], rel_right_face[5],
            rel_right_face[6], rel_right_face[7], rel_right_face[8],
        ]

        # assign new state (rotate back from relative to original orientation)
        new_state = this_state.copy()
        new_state[Rubiks.Face.TOP] = Rubiks.rotateFaceNoCascade(new_rel_back_face, clockwise=False) # good idk why this one is CCW ):
        new_state[Rubiks.Face.FRONT] = Rubiks.rotateFaceNoCascade(new_rel_right_face, clockwise=False) # good
        new_state[Rubiks.Face.LEFT] = Rubiks.rotateFaceNoCascade(new_rel_top_face, clockwise=True) # good
        new_state[Rubiks.Face.BACK] = Rubiks.rotateFaceNoCascade(new_rel_left_face, clockwise=True) # good
        new_state[Rubiks.Face.RIGHT] = new_state[Rubiks.Face.RIGHT] # doesnt move
        new_state[Rubiks.Face.BOTTOM] = Rubiks.rotateFaceNoCascade(new_rel_front_face, clockwise=False) # good
        return new_state










    @staticmethod # fix me
    def rotateLeftCCW(this_state : dict) -> object:
        # get current state, by assining this_state faces to relative cube as if you were always moving the TOP face
        # [] make case statement instead of having 12 functions
        # same as if left was on top AND rotated CCW?
        # then front face would rotate, but since CCW it moves to right
        # then bottom face would move to new left, but since CCW it moves to front and rotated?
        # new left face is now old back rotated CCW?
        # new back face is now old top face rotated CW?
        relative_cube : dict = this_state.copy()
        rel_top_face : list = Rubiks.rotateFaceNoCascade(relative_cube[Rubiks.Face.LEFT].copy(), clockwise=False) # good
        rel_front_face : list = Rubiks.rotateFaceNoCascade(relative_cube[Rubiks.Face.BOTTOM].copy(), clockwise=True) # good
        rel_left_face : list = Rubiks.rotateFaceNoCascade(relative_cube[Rubiks.Face.BACK].copy(), clockwise=False) # good
        rel_back_face : list = Rubiks.rotateFaceNoCascade(relative_cube[Rubiks.Face.TOP].copy(), clockwise=False) # good
        rel_right_face : list = Rubiks.rotateFaceNoCascade(relative_cube[Rubiks.Face.FRONT].copy(), clockwise=True) # good

        # make new state
        new_rel_top_face : list = [
            rel_top_face[2], rel_top_face[5], rel_top_face[8],
            rel_top_face[1], rel_top_face[4], rel_top_face[7],
            rel_top_face[0], rel_top_face[3], rel_top_face[6],
        ]
        new_rel_front_face : list = [
            rel_left_face[0], rel_left_face[1], rel_left_face[2],
            rel_front_face[3], rel_front_face[4], rel_front_face[5],
            rel_front_face[6], rel_front_face[7], rel_front_face[8],
        ]
        new_rel_left_face : list = [
            rel_back_face[0], rel_back_face[1], rel_back_face[2],
            rel_left_face[3], rel_left_face[4], rel_left_face[5],
            rel_left_face[6], rel_left_face[7], rel_left_face[8],
        ]
        new_rel_back_face : list = [
            rel_right_face[0], rel_right_face[1], rel_right_face[2],
            rel_back_face[3], rel_back_face[4], rel_back_face[5],
            rel_back_face[6], rel_back_face[7], rel_back_face[8],
        ]
        new_rel_right_face : list = [
            rel_front_face[0], rel_front_face[1], rel_front_face[2],
            rel_right_face[3], rel_right_face[4], rel_right_face[5],
            rel_right_face[6], rel_right_face[7], rel_right_face[8],
        ]

        # assign new state (rotate back from relative to original orientation)
        new_state = this_state.copy()
        new_state[Rubiks.Face.TOP] = Rubiks.rotateFaceNoCascade(new_rel_back_face, clockwise=False) # good idk why this one is CCW ):
        new_state[Rubiks.Face.FRONT] = Rubiks.rotateFaceNoCascade(new_rel_right_face, clockwise=False) # good
        new_state[Rubiks.Face.LEFT] = Rubiks.rotateFaceNoCascade(new_rel_top_face, clockwise=True) # good
        new_state[Rubiks.Face.BACK] = Rubiks.rotateFaceNoCascade(new_rel_left_face, clockwise=True) # good
        new_state[Rubiks.Face.RIGHT] = new_state[Rubiks.Face.RIGHT] # doesnt move
        new_state[Rubiks.Face.BOTTOM] = Rubiks.rotateFaceNoCascade(new_rel_front_face, clockwise=False) # good
        return new_state










    @staticmethod # fix me
    def rotateBackCW(this_state : dict) -> object:
        pass
    @staticmethod # fix me
    def rotateBackCCW(this_state : dict) -> object:
        pass
    @staticmethod # fix me
    def rotateRightCW(this_state : dict) -> object:
        pass

    @staticmethod # fix me
    def rotateRightCCW(this_state : dict) -> object:
        pass

    @staticmethod # fix me
    def rotateBottomCW(this_state : dict) -> object:
        pass

    @staticmethod # fix me
    def rotateBottomCCW(this_state : dict) -> object:
        pass