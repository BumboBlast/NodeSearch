'''
    todo:
        [] refactor MemoryTracking into generic tracking module (basically just rename)
        [] add functions in MemoryTracking module to export statistics
        [] create unit testing module for executing these puzzles in batch
        [] generalize EightPuzzle to N-Puzzle
        [] create other problems
            sudoku, 8 queens, chess, navigation, rubicks cube, hanoi?
        [] organize all teh search modules into a folder
        [] create more search algorithms
        [] if create more problems, could move eightPuzzle and rest of problems into separate files
'''



from Node import Node
from Problem import EightPuzzle, Problem
from SearchAlgorithm.Solver import Solver
from SearchAlgorithm.SearchBreadthFirst import BrFS
from SearchAlgorithm.SearchDepthFirst import DpFS
from SearchAlgorithm.SearchDepthLimited import DepthLimited
from SearchAlgorithm.SearchIterativeDeepening import IterativeDeepening
from SearchAlgorithm.SearchBidirectional import Bidirection
from SearchAlgorithm.SearchUniformCost import UniformCost
from MemoryTracking import track

import sys

''' puzzles '''
def getSomePuzzles() -> list:
    puzzleList : list = list()
    puzzleList.append(EightPuzzle()) # random puzzle
    puzzleList.append(EightPuzzle('123456780'))
    puzzleList.append(EightPuzzle('876543210'))
    puzzleList.append(EightPuzzle('102345678'))
    puzzleList.append(EightPuzzle('376041825')) # impossible to solve, odd # of inversions
    puzzleList.append(EightPuzzle('402176583')) # impossible to solve, odd # of inversions
    return puzzleList

@track
def solveThePuzzle(solver: Solver, problem: Problem) -> Node:
    ''' Returns the solution Node.
    '''    
    print('init:\n' + EightPuzzle.print_state(problem.initial_state))
    print('solvable: ' + str(problem.is_solvable()))
    solution_node : Node = solver.search()
    return solution_node

def print_solution(solver: Solver, solution_node: Node, max_solution_len: int = 100, reverse: bool = False):
    solution_chain: list = solver.get_solution(solution_node)
    if len(solution_chain) <= 0:
        print('No solution ):')
        return
    print(f'solution is {len(solution_chain)} nodes long')
    if len(solution_chain) > max_solution_len:
        print('Solution to long to print')
    if reverse:
        solution_chain.reverse()
    for n in solution_chain[::-1]:
        print(str(n))


search_algorithms: dict = {
    'breadth-first': BrFS,
    'uniform-cost' : UniformCost,
    'depth-first': DpFS,
    'depth-limited': DepthLimited,
    'iterative-deepening': IterativeDeepening,
    'bidirectional' : Bidirection,
}

if __name__ == '__main__':
    # get problem
    problem: EightPuzzle = getSomePuzzles()[3]
    problem.solution_state = '012345678' # hard coded probably in the wrong place
    
    # get solver object and user argument
    user_arg : str = None
    solver : Solver = None
    try:
        user_arg : str = sys.argv[1]
        solver = search_algorithms[user_arg](problem)
    except Exception as e:
        print(e)
        algo_names: str = ',\n\t'.join([name for name in search_algorithms.keys()])
        print(f'Run with argument:\n\t{algo_names}')
    
    # solve the problem
    if solver: # better way to do this?
        solution_node : Node = solveThePuzzle(solver, problem)
        if type(solution_node) is str:
            print(solution_node)
        print_solution(solver, solution_node, 60)