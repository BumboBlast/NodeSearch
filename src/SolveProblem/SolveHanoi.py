
import traceback
from Node import Node
from Problem.Problem import Problem
from Problem.Hanoi import Hanoi
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
    puzzleList.append(Hanoi()) # random puzzle
    puzzleList.append(Hanoi([[4, 3, 2, 1],[],[]])) # custom init-state
    puzzleList.append(Hanoi([[], [5,4,3,2,1], []]))
    return puzzleList

@track
def solveThePuzzle(solver: Solver, problem: Problem) -> Node:
    ''' Returns the solution Node.
    '''    
    print('init:\n' + Hanoi.print_state(problem.initial_state))
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
        return
    if reverse:
        solution_chain.reverse()
    for n in solution_chain[::-1]:
        print(str(n))


search_algorithms: dict = {
    'breadth-first': BrFS,
    'depth-first': DpFS,
    'depth-limited': DepthLimited,
    'iterative-deepening': IterativeDeepening,
    'bidirectional' : Bidirection,
    'uniform-cost' : UniformCost,
}


def solve_Hanoi():
    # get problem
    problem: Hanoi = getSomePuzzles()[1]
    problem.solution_state = [[],[],[4, 3, 2, 1]] # hard coded probably in the wrong place
    print(problem.initial_state)
    print(problem.solution_state)
    print(problem.move_disk_0_1(problem.initial_state))
    # get solver object and user argument
    user_arg : str = None
    solver : Solver = None
    try:
        user_arg = sys.argv[1]
        solver = search_algorithms[user_arg](problem)
        print('here')
    except Exception as e:
        tb = traceback.format_exc()
        print(tb)
        algo_names: str = ',\n\t'.join([name for name in search_algorithms.keys()])
        print(f'Run with argument:\n\t{algo_names}')
    
    # solve the problem
    if solver: # better way to do this?
        solution_node : Node = solveThePuzzle(solver, problem)
        if type(solution_node) is str:
            print(solution_node)
        print_solution(solver, solution_node, 100)