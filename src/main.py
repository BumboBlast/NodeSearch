'''
    todo:
        [] refactor MemoryTracking into generic tracking module (basically just rename)
        [] add functions in MemoryTracking module to export statistics
        [] create unit testing module for executing these puzzles in batch
        [] generalize EightPuzzle to N-Puzzle
        [] create other problems
            sudoku, 8 queens, chess, navigation, rubicks cube, hanoi?, Map Solving
        [] organize all teh search modules into a folder
        [] create more search algorithms
        [] if create more problems, could move eightPuzzle and rest of problems into separate files
        [] separate the main menu stuff (probably into Main) to not be entangled / rewritten for each problem
        [] do a ton of refactoring:
            [] either make hanoi use strings
            [] or make the algorithms not need to use immutable types??
'''
import traceback
import sys

import SolveProblem.SolveEightPuzzle
import SolveProblem.SolveHanoi
import SolveProblem.SolveRubiks



def dbg():
    print("START dbg")
    
    from Problem.Rubiks2 import Rubiks
    from SearchAlgorithm.SearchBreadthFirst import BrFS
    from Node import Node
    from SearchAlgorithm.Solver import Solver

    # puzzle 0 -> solved
    # r0 = {
        # Rubiks.Face.TOP     : [0, 0, 0, 0, 0, 0, 0, 0, 0],
        # Rubiks.Face.FRONT   : [1, 1, 1, 1, 1, 1, 1, 1, 1],
        # Rubiks.Face.LEFT    : [2, 2, 2, 2, 2, 2, 2, 2, 2],
        # Rubiks.Face.BACK    : [3, 3, 3, 3, 3, 3, 3, 3, 3],
        # Rubiks.Face.RIGHT   : [4, 4, 4, 4, 4, 4, 4, 4, 4],
        # Rubiks.Face.BOTTOM  : [5, 5, 5, 5, 5, 5, 5, 5, 5],
    # }

    # # puzzle 1 -> scrambled
    # r1 = {
        # "TOP" : [],
        # "FRONT" : [],
        # "LEFT" : [],
        # "BACK" : [],
        # "RIGHT" : [],
        # "BOTTOM" : []
    # }

    # def solveThePuzzle(solver: Solver, problem: Problem) -> Node:
    #     ''' Returns the solution Node.
    #     '''    
    #     print('init:\n' + Rubiks.print_state(problem.initial_state))
    #     print('solvable: ' + str(problem.is_solvable()))
    #     solution_node : Node = solver.search()
    #     return solution_node

    newRubiks : Rubiks = Rubiks()
    # newRubiks.initial_state = r0.copy()
    newRubiks.solution_state = newRubiks.initial_state # hard coded probably in the wrong place
    solver : BrFS = BrFS(newRubiks)

    print(f"init:\n{Rubiks.print_net(newRubiks.initial_state)}")
    func1 : function = Rubiks.rotateTopCW
    
    rot1 : object = Rubiks.rotateLeftCW(state=newRubiks.initial_state)
    # rot2 : object = 

    print(f"{func1.__name__}:\n{Rubiks.print_net(rot1)}")
    # print(f"next:\n{rot2}")

    print("END dbg")


problemList = {
    # debug
    "dbg" : dbg,

    # eight puzzle
    "Eight" : SolveProblem.SolveEightPuzzle.solve_EightPuzzle,
    "eight" : SolveProblem.SolveEightPuzzle.solve_EightPuzzle,
    "EightPuzzle" : SolveProblem.SolveEightPuzzle.solve_EightPuzzle,
    "eightPuzzle" : SolveProblem.SolveEightPuzzle.solve_EightPuzzle,
    "eightpuzzle" : SolveProblem.SolveEightPuzzle.solve_EightPuzzle,
    "Eight-Puzzle" : SolveProblem.SolveEightPuzzle.solve_EightPuzzle,
    "eight-puzzle" : SolveProblem.SolveEightPuzzle.solve_EightPuzzle,
    "eight-Puzzle" : SolveProblem.SolveEightPuzzle.solve_EightPuzzle,

    # hanoi
    "Hanoi" : SolveProblem.SolveHanoi.solve_Hanoi, 
    "hanoi" : SolveProblem.SolveHanoi.solve_Hanoi,
    "HanoiTower" : SolveProblem.SolveHanoi.solve_Hanoi,
    "Hanoi-Tower" : SolveProblem.SolveHanoi.solve_Hanoi,
    "hanoiTower" : SolveProblem.SolveHanoi.solve_Hanoi,
    "hanoitower" : SolveProblem.SolveHanoi.solve_Hanoi,
    "Tower-of-Hanoi" : SolveProblem.SolveHanoi.solve_Hanoi,
    "tower-of-hanoi" : SolveProblem.SolveHanoi.solve_Hanoi,
    "tower-of-Hanoi" : SolveProblem.SolveHanoi.solve_Hanoi,
    "Tower-of-hanoi" : SolveProblem.SolveHanoi.solve_Hanoi,
    
    # rubicks cube
    "rubicks" : SolveProblem.SolveRubiks.solve_Rubiks,
    "Rubicks" : SolveProblem.SolveRubiks.solve_Rubiks,
    "rubicksCube" : SolveProblem.SolveRubiks.solve_Rubiks,
    "RubicksCube" : SolveProblem.SolveRubiks.solve_Rubiks,
    "rubickscube" : SolveProblem.SolveRubiks.solve_Rubiks,
    "rubicks-cube" : SolveProblem.SolveRubiks.solve_Rubiks,
    "Rubicks-cube" : SolveProblem.SolveRubiks.solve_Rubiks,
    "rubicks-Cube" : SolveProblem.SolveRubiks.solve_Rubiks,
    "rubiks" : SolveProblem.SolveRubiks.solve_Rubiks,
    "Rubiks" : SolveProblem.SolveRubiks.solve_Rubiks,
    "rubiksCube" : SolveProblem.SolveRubiks.solve_Rubiks,
    "RubiksCube" : SolveProblem.SolveRubiks.solve_Rubiks,
    "rubikscube" : SolveProblem.SolveRubiks.solve_Rubiks,
    "rubiks-cube" : SolveProblem.SolveRubiks.solve_Rubiks,
    "Rubiks-cube" : SolveProblem.SolveRubiks.solve_Rubiks,
    "rubiks-Cube" : SolveProblem.SolveRubiks.solve_Rubiks,
}

if __name__ == '__main__':
        # get solver object and user argument
    user_arg : str = None
    try:
        user_arg : str = sys.argv[1]
        problemList[user_arg]()
    except Exception as e:
        tb = traceback.format_exc()
        print(tb)
    




    # SolveProblem.SolveEightPuzzle.solve_EightPuzzle()
    # SolveProblem.SolveHanoi.solve_Hanoi()
    
