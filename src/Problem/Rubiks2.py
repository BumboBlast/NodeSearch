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
    yellow : 2
    blue : 3
    green : 4
    orange : 5
    

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
        WHITE = 1
        RED = 2
        ORANGE = 3
        YELLOW = 4
        GREEN = 5
        BLUE = 6
    
    class Face(Enum):
        TOP = 1
        FRONT = 2
        LEFT = 3
        BACK = 4
        RIGHT = 5
        BOTTOM = 6
               
    def __init__(self, init_state: list = list()):
        # if no init-state passed, make one at random
        super().__init__()
        self.initial_state = init_state
        if init_state == list():
            self.initial_state = [ # default state; solved state - colored by their face value
            Rubiks.Face.TOP.value, Rubiks.Face.TOP.value, Rubiks.Face.TOP.value, # TOP face
            Rubiks.Face.TOP.value, Rubiks.Face.TOP.value, Rubiks.Face.TOP.value,
            Rubiks.Face.TOP.value, Rubiks.Face.TOP.value, Rubiks.Face.TOP.value,
            0, # this value is reserved so that the next face will start in index 10
            Rubiks.Face.FRONT.value, Rubiks.Face.FRONT.value, Rubiks.Face.FRONT.value, # FRONT face
            Rubiks.Face.FRONT.value, Rubiks.Face.FRONT.value, Rubiks.Face.FRONT.value,
            Rubiks.Face.FRONT.value, Rubiks.Face.FRONT.value, Rubiks.Face.FRONT.value,
            0, # this value is reserved so that the next face will start in index 20
            Rubiks.Face.LEFT.value, Rubiks.Face.LEFT.value, Rubiks.Face.LEFT.value, # LEFT face
            Rubiks.Face.LEFT.value, Rubiks.Face.LEFT.value, Rubiks.Face.LEFT.value,
            Rubiks.Face.LEFT.value, Rubiks.Face.LEFT.value, Rubiks.Face.LEFT.value,
            0, # this value is reserved so that the next face will start in index 30
            Rubiks.Face.BACK.value, Rubiks.Face.BACK.value, Rubiks.Face.BACK.value, # BACK face
            Rubiks.Face.BACK.value, Rubiks.Face.BACK.value, Rubiks.Face.BACK.value,
            Rubiks.Face.BACK.value, Rubiks.Face.BACK.value, Rubiks.Face.BACK.value,
            0, # this value is reserved so that the next face will start in index 40
            Rubiks.Face.RIGHT.value, Rubiks.Face.RIGHT.value, Rubiks.Face.RIGHT.value, # RIGHT face
            Rubiks.Face.RIGHT.value, Rubiks.Face.RIGHT.value, Rubiks.Face.RIGHT.value,
            Rubiks.Face.RIGHT.value, Rubiks.Face.RIGHT.value, Rubiks.Face.RIGHT.value,
            0, # this value is reserved so that the next face will start in index 50
            Rubiks.Face.BOTTOM.value, Rubiks.Face.BOTTOM.value, Rubiks.Face.BOTTOM.value, # BOTTOM face
            Rubiks.Face.BOTTOM.value, Rubiks.Face.BOTTOM.value, Rubiks.Face.BOTTOM.value,
            Rubiks.Face.BOTTOM.value, Rubiks.Face.BOTTOM.value, Rubiks.Face.BOTTOM.value,
            ]
         

    def get_state(self, state) -> object:
        ''' returns state (getter) '''
        print("get state (:")
        return str(state)

    def get_actions(self, state) -> list:
        ''' each state, you can always perform the same actions
        '''
        return [
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
    def print_net(state: str) -> str:
        netstr : str = str()
        netstr +=      f"\t\t\t{state[50:53]} BOTTOM\n" # BOTTOM face
        netstr +=      f"\t\t\t{state[53:56]}\n"
        netstr +=      f"\t\t\t{state[56:59]}\n"
        netstr +=      f"\t\t\t{state[30:33]} BACK\n" # BACK face
        netstr +=      f"\t\t\t{state[33:36]}\n"
        netstr +=      f"\t\t\t{state[36:39]}\n"
        netstr +=      f"\t LEFT {state[20:23]} {state[0:3]} {state[40:43]} RIGHT\n" # TOP face  RIGHT face
        netstr +=      f"\t      {state[23:26]} {state[3:6]} {state[43:46]}\n"
        netstr +=      f"\t      {state[26:29]} {state[6:9]} {state[46:49]}\n"
        netstr +=      f"\t\t\t{state[10:13]}\ \n" # FRONT face
        netstr +=      f"\t\t\t{state[13:16]} \ \n"
        netstr +=      f"\t\t  FRONT {state[16:19]}  TOP\n"
        return netstr
        
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
            
            Counter-Clockwise (CCW)
            [1 2 3 4 5 6 7 8 9] -> [3 6 9 2 5 8 1 4 7]
            
            Clockwise (CW)
            [1 2 3 4 5 6 7 8 9] -> [7 4 1 8 5 2 9 6 3]
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
    def rotateCube(state: object, z_axis: bool, cw: bool) -> object:
        ''' return the state as if the entire cube was rotated
            z_axis = true means rotating around vertical axis
            z_axiz = false means rotating around y-axis 
                (axis pointing forward and backwards relative to viewer)
            
            cw = true means rotating clockwise if the viewer were looking towards the negative axis.
            always rotates CW but if cw = false, means applying cw three times
            
            cube state = list of 59 integers. each value with a 9 is kept blank.
            ranges: [0-8] [10-18] [20-28] ... [50-58]
        '''
        
        if type(state) == list:
            if z_axis:
                if cw:
                    return [
                        state[6], state[3], state[0], # new TOP face
                        state[7], state[4], state[1], # = rotated CW
                        state[8], state[5], state[2],
                        0, # kept empty
                        state[46], state[43], state[40], # new FRONT face
                        state[47], state[44], state[41], # = old RIGHT face rotated CW
                        state[48], state[45], state[42],
                        0, # kept empty
                        state[16], state[13], state[10], # new LEFT face
                        state[17], state[14], state[11], # = old FRONT face rotated CW
                        state[18], state[15], state[12],
                        0, # kept empty
                        state[26], state[23], state[20], # new BACK face
                        state[27], state[24], state[21], # = old LEFT face rotated CW
                        state[28], state[25], state[22],
                        0, # kept empty
                        state[36], state[33], state[30], # new RIGHT face
                        state[37], state[34], state[31], # = old BACK face rotated CW
                        state[38], state[35], state[32],
                        0, # kept empty
                        state[52], state[55], state[58], # new BOTTOM face
                        state[51], state[54], state[57], # = rotated CCW
                        state[50], state[53], state[56],                    
                    ]
                # if z_axis, counter clockwise, rotate CW three times
                else:
                    rot1 : list = Rubiks.rotateCube(state, z_axis=True, cw=True)
                    rot2 : list = Rubiks.rotateCube(state=rot1, z_axis=True, cw=True)
                    return Rubiks.rotateCube(rot2, z_axis=True, cw=True)
                    
            # if NOT z_axis:
            else:
                if cw:
                    return [
                        state[20], state[21], state[22], # new TOP face
                        state[23], state[24], state[25], # = old LEFT face
                        state[26], state[27], state[28],
                        0, # kept empty
                        state[16], state[13], state[10], # new FRONT face
                        state[17], state[14], state[11], # = rotated CW
                        state[18], state[15], state[12],
                        0, # kept empty
                        state[58], state[57], state[56], # new LEFT face
                        state[55], state[54], state[53], # = old BOTTOM face rotated CW
                        state[52], state[51], state[50],
                        0, # kept empty
                        state[32], state[35], state[38], # new BACK face
                        state[31], state[34], state[37], # = rotated CCW
                        state[30], state[33], state[36],
                        0, # kept empty
                        state[0], state[1], state[2], # new RIGHT face
                        state[3], state[4], state[5], # = old TOP face
                        state[6], state[7], state[8],
                        0, # kept empty
                        state[48], state[47], state[46], # new BOTTOM face
                        state[45], state[44], state[43], # = old RIGHT face rotated twice?
                        state[42], state[41], state[40],                    
                    ]
                # if not z axis, counter clockwise, rotate cw three times.
                else:
                    rot1 : list = Rubiks.rotateCube(state, z_axis=False, cw=True)
                    rot2 : list = Rubiks.rotateCube(state=rot1, z_axis=False, cw=True)
                    return Rubiks.rotateCube(rot2, z_axis=False, cw=True)
            
        else:
            return None
        
        
    
    @staticmethod # fix me
    def rotateTopCW(state : object) -> object:
        ''' rotating top face clockwise '''
        return [
            state[6], state[3], state[0], # new TOP face
            state[7], state[4], state[1], # = old TOP face rot CW
            state[8], state[5], state[2],
            0, # kept empty
            state[40], state[43], state[46], # new FRONT face
            state[13], state[14], state[15], # = old FRONT face but
            state[16], state[17], state[18], # 1st row is from RIGHT
            0, # kept empty
            state[20], state[21], state[10], # new LEFT face
            state[23], state[24], state[11], # = old LEFT face but
            state[26], state[27], state[12], # 3rd col is from FRONT
            0, # kept empty
            state[30], state[31], state[32], # new BACK face
            state[33], state[34], state[35], # = old BACK face but
            state[28], state[25], state[22], # 3rd row is from from LEFT
            0, # kept empty
            state[36], state[41], state[42], # new RIGHT face
            state[37], state[44], state[45], # = old RIGHT face but
            state[38], state[47], state[48], # 1st col is from BACK
            0, # kept empty
            state[50], state[51], state[52], # new BOTTOM face
            state[53], state[54], state[55], # = doesnt change
            state[56], state[57], state[58], 
        ]
        
    @staticmethod # fix me
    def rotateTopCCW(this_state : dict) -> object:
        pass

    @staticmethod # GOOD
    def rotateFrontCW(state : object) -> object:
        ''' this rotatation is the same as rotating the whole cube:
            Y_axis clockwise once + Z_axis clockwise once
            then doing TOP-Clockwise
            then rotate back:
            Y_axis counter-clockwise once + Z_axis counter-clockwise once
        '''
        rot: object = Rubiks.rotateCube(state, z_axis=False, cw=True)
        rot = Rubiks.rotateCube(rot, z_axis=True, cw=True)
        rot = Rubiks.rotateTopCW(rot)
        # rotate back
        rot =  Rubiks.rotateCube(rot, z_axis=False, cw=False)
        rot =  Rubiks.rotateCube(rot, z_axis=True, cw=False)
        return rot

    @staticmethod # fix me
    def rotateFrontCCW(this_state : dict) -> object:
        pass

    @staticmethod # GOOD
    def rotateLeftCW(state : object) -> object:
        ''' this rotatation is the same as rotating the whole cube:
            Y_axis clockwise once
            then doing TOP-Clockwise
            then rotate back:
            Y_axis CounterClockwise once
        '''
        rot: object = Rubiks.rotateCube(state, z_axis=False, cw=True)
        rot = Rubiks.rotateTopCW(rot)
        # rotate back
        rot =  Rubiks.rotateCube(rot, z_axis=False, cw=False)
        return rot


    @staticmethod # fix me
    def rotateLeftCCW(this_state : dict) -> object:
        pass
        
    @staticmethod # GOOD
    def rotateBackCW(state : object) -> object:
        ''' this rotatation is the same as rotating the whole cube:
            Y_axis clockwise  + Z_axis counter-clockwise once
            then doing TOP-Clockwise
            then rotate back:
            Y_axis counter-clockwise + Z_axis clockwise once
        '''
        rot: object = Rubiks.rotateCube(state, z_axis=False, cw=True)
        rot = Rubiks.rotateCube(rot, z_axis=True, cw=False)
        rot = Rubiks.rotateTopCW(rot)
        # rotate back
        rot =  Rubiks.rotateCube(rot, z_axis=False, cw=False)
        rot =  Rubiks.rotateCube(rot, z_axis=True, cw=True)
        return rot

    @staticmethod # fix me
    def rotateBackCCW(this_state : dict) -> object:
        pass

    @staticmethod # GOOD
    def rotateRightCW(state : dict) -> object:
        ''' this rotatation is the same as rotating the whole cube:
            Y_axis counter-clockwise once
            then doing TOP-Clockwise
            then rotate back:
            Y_axis clockwise once
        '''
        rot: object = Rubiks.rotateCube(state, z_axis=False, cw=False)
        rot = Rubiks.rotateTopCW(rot)
        # rotate back
        rot =  Rubiks.rotateCube(rot, z_axis=False, cw=True)
        return rot

    @staticmethod # fix me
    def rotateRightCCW(this_state : dict) -> object:
        pass

    @staticmethod # GOOD
    def rotateBottomCW(state : object) -> object:
        ''' this rotatation is the same as rotating the whole cube:
            Y_axis clockwise TWICE
            then doing TOP-Clockwise
            then rotate back:
            Y_axis clockwise TWICE
        '''
        rot: object = Rubiks.rotateCube(state, z_axis=False, cw=True)
        rot = Rubiks.rotateCube(rot, z_axis=False, cw=True)
        rot = Rubiks.rotateTopCW(rot)
        # rotate back
        rot =  Rubiks.rotateCube(rot, z_axis=False, cw=True)
        rot =  Rubiks.rotateCube(rot, z_axis=False, cw=True)
        return rot    
    @staticmethod # fix me

    def rotateBottomCCW(this_state : dict) -> object:
        pass
