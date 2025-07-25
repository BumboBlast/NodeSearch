

from ChildNodeTest import Node
from ProblemTest import EightPuzzle, Problem
from Solver import Solver
from SearchBreadthFirst import BrFS
from SearchDepthFirst import DpFS
from SearchDepthLimited import DepthLimited
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

def printSolution(solution_node: Node, max_solution_length: int):
    if solution_node:
        solution_chain: list = Node.getNodeChainIterative(solution_node, short=True)
        print('solution chain is ' + str(len(solution_chain)) + ' nodes')
        if len(solution_chain) < max_solution_length:
            for n in solution_chain[::-1]:
                print(str(n))
        else:
            print('solution too long to print')
    else:
        print('no solution ):')

if __name__ == '__main__':
    # get problem
    problem: EightPuzzle = getSomePuzzles()[2]
    problem.solution_state = '012345678' # hard coded probably in the wrong place
    
    # get solver object and user argument
    user_arg : str = None
    solver : Solver = None
    if len(sys.argv) == 2:
        user_arg : str = sys.argv[1]
    if user_arg == 'breadth-first':
        solver = BrFS(problem)
    elif user_arg == 'depth-first':
        solver: Solver = DpFS(problem)
    elif user_arg == 'depth-limited':
        solver: Solver = DepthLimited(problem)
    else:
        print('Choose search algorithm: \"breath-first\", \"depth-first\", \"depth-limited\"')
    
    # solve the problem
    if solver: # better way to do this?
        solution_node : Node = solveThePuzzle(solver, problem)
        if type(solution_node) is str:
            print(solution_node)
        else:
            printSolution(solution_node, 60)