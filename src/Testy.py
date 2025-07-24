

from ChildNodeTest import Node
from ProblemTest import EightPuzzle, Problem
from SearchBreadthFirst import BrFS
from SearchDepthFirst import DpFS
from MemoryTracking import track

import sys

print('(:')

''' puzzles '''
def getSomePuzzles() -> list:
    puzzleList : list = list()
    puzzleList.append(EightPuzzle('123456780'))
    puzzleList.append(EightPuzzle('876543210'))
    puzzleList.append(EightPuzzle('102345678'))
    puzzleList.append(EightPuzzle('376041825')) # impossible to solve, odd # of inversions
    puzzleList.append(EightPuzzle('402176583')) # impossible to solve, odd # of inversions
    puzzleList.append(EightPuzzle('327615084')) # a very long solution
    puzzleList.append(EightPuzzle()) # random puzzle
    return puzzleList

''' set up solver object(s) '''
def getSolverObjects(problem: Problem) -> dict:
    problem.solution_state = '012345678'
    BrFSsolver: BrFS = BrFS(problem)
    DpFSsolver:  DpFS = DpFS(problem)
    return {
        'BrFS' : BrFSsolver,
        'DpFS' : DpFSsolver
    }

@track
def solveThePuzzle(solver: object, problem: Problem) -> Node:
    ''' Returns the solution Node.
    '''    
    print('init:\n' + EightPuzzle.print_state(problem.initial_state))
    print('solvable: ' + str(problem.is_solvable()))

    # solution_node : Node = solver.breastFirstSearch()
    solution_node : Node = solver.depthFirstSearch()
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
    problem: EightPuzzle = getSomePuzzles()[0]
    # solver : object = getSolverObjects(problem)['BrFS']
    solver : object = getSolverObjects(problem)['DpFS']
    solution_node : Node = solveThePuzzle(solver, problem)
    # printSolution(solution_node, 60)