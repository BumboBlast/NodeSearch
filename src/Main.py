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
'''


import SolvePuzzle.SolveEightPuzzle
if __name__ == '__main__':
    SolvePuzzle.SolveEightPuzzle.solve_EightPuzzle()