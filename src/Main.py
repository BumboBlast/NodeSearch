'''
    todo:
        [] refactor SearchUniformCost to use a heapQ isntead of dict for its frontier (implement prioQ)
        [] refactor SearchBreadthFirst to search dict keys using \\ if str in dic \\ instead of dic.keys()
        [] refactor Testy -> printSolution into class specific methods. 
            Each algorithm should be able to print its own solution
        [] refactor Bidrectional to be a little better
        [] fix bug in Bidrectional. puzzle 3 '102345678'
        [] refactor MemoryTracking into generic tracking module (basically just rename)
        [] add functions in MemoryTracking module to export statistics
        [] create unit testing module for executing these puzzles in batch
        [] generalize EightPuzzle to N-Puzzle
        [] create other problems
            sudoku, 8 queens, chess, navigation, rubicks cube?
        [] organize all teh search modules into a folder
        [] create more search algorithms
        [] rename childNodeTest -> childNode or just Node
        [] rename ProblemTest -> Problem
        [] if create more problems, could move eightPuzzle and rest of problems into separate files
'''



from ChildNodeTest import Node
from ProblemTest import EightPuzzle, Problem
from Solver import Solver
from SearchBreadthFirst import BrFS
from SearchDepthFirst import DpFS
from SearchDepthLimited import DepthLimited
from SearchIterativeDeepening import IterativeDeepening
from SearchBidirectional import Bidirection
from SearchUniformCost import UniformCost
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

def printSolution(solution_node: Node, max_solution_length: int, reverse: bool = False):
    if solution_node:
        solution_chain: list = Node.getNodeChainIterative(solution_node, short=True)
        print('solution chain is ' + str(len(solution_chain)) + ' nodes')
        if len(solution_chain) < max_solution_length:
            if reverse:
                solution_chain.reverse()
            for n in solution_chain[::-1]:
                print(str(n))
        else:
            print('solution too long to print')
    else:
        print('no solution ):')


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
    problem: EightPuzzle = getSomePuzzles()[2]
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
        elif type(solution_node) is list:
            printSolution(solution_node[0], 60)
            printSolution(solution_node[1], 60, reverse=True)
        else:
            printSolution(solution_node, 60)