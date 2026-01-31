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
            [] or make sure Node.state always returns a hashable
'''
import traceback
import sys

import SolveProblem.SolveEightPuzzle
import SolveProblem.SolveHanoi
import SolveProblem.SolveRubiks



def dbg():
    print("START dbg")
    
    from Problem.Rubiks import Rubiks
    from SearchAlgorithm.SearchBreadthFirst import BrFS
    from Node import Node
    from SearchAlgorithm.Solver import Solver
    from Problem.EightPuzzle import EightPuzzle

    e = EightPuzzle('123456789ABCDEF0')

    print(e.initial_state)
    print(EightPuzzle.moveUp(e.initial_state))
    

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
    
