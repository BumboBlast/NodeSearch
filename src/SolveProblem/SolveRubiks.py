
import traceback
from Node import Node
from Problem.Problem import Problem
from Problem.Rubiks import Rubiks
from SearchAlgorithm.Solver import Solver
from SearchAlgorithm.SearchBreadthFirst import BrFS
from SearchAlgorithm.SearchDepthFirst import DpFS
from SearchAlgorithm.SearchDepthLimited import DepthLimited
from SearchAlgorithm.SearchIterativeDeepening import IterativeDeepening
from SearchAlgorithm.SearchBidirectional import Bidirection
from SearchAlgorithm.SearchUniformCost import UniformCost
from SearchAlgorithm.SearchBestFirst import BestFirst
from MemoryTracking import track

import sys

''' puzzles '''

def getSomePuzzles() -> list:
    puzzleList : list = list()
    puzzleList.append(Rubiks()) # random puzzle
    puzzleList.append(Rubiks([ # custom init-state - one rotatios
        4,1,1,
        4,1,1,
        4,1,1,
        0,
        1,2,2,
        1,2,2,
        1,2,2,
        0,
        3,3,3,
        3,3,3,
        3,3,3,
        0,
        6,4,4,
        6,4,4,
        6,4,4,
        0,
        5,5,5,
        5,5,5,
        5,5,5,
        0,
        2,6,6,
        2,6,6,
        2,6,6,
    ])),
    puzzleList.append(Rubiks([ # custom init-state - two rotatios
        6, 6, 6,
        1, 1, 1,
        3, 3, 3,
        0,
        2, 2, 2,
        2, 2, 2,
        2, 2, 2,
        0,
        5, 5, 5,
        3, 3, 3,
        6, 6, 6,
        0,
        4, 4, 4,
        4, 4, 4,
        4, 4, 4,
        0,
        3, 3, 3,
        5, 5, 5,
        1, 1, 1,
        0,
        5, 5, 5,
        6, 6, 6,
        1, 1, 1
    ]))
    puzzleList.append(Rubiks("11421455601132236620223133214054654644605555524430331366162"))
    puzzleList.append(Rubiks(Rubiks.DEFAULT_STATE))
    return puzzleList

@track
def solveThePuzzle(solver: Solver, problem: Problem) -> Node:
    ''' Returns the solution Node.
    '''    
    print('init:\n' + Rubiks.print_state(problem.initial_state))
    print('solvable: ' + str(problem.is_solvable()))
    solution_node : Node = solver.search()
    return solution_node

def print_solution(solver: Solver, solution_node: Node, max_solution_len: int = 100, reverse: bool = False):
    solution_chain: list = solver.get_solution(solution_node, short=True)
    if len(solution_chain) <= 0:
        print('No solution ):')
        return
    print(f'solution is {len(solution_chain)} nodes long')
    if len(solution_chain) > max_solution_len:
        print('Solution to long to print')
        return
    if reverse:
        solution_chain.reverse()

    # display solution
    print("  TOP       FRONT     LEFT      BACK      RIGHT     BOTTOM")
    for n in solution_chain[::-1]:
        print(n)


search_algorithms: dict = {
    'breadth-first': BrFS,
    'depth-first': DpFS,
    'depth-limited': DepthLimited,
    'iterative-deepening': IterativeDeepening,
    'bidirectional' : Bidirection,
    'uniform-cost' : UniformCost,
    'best-first' : BestFirst
}


def solve_Rubiks():

    # get problem
    problem: Rubiks = getSomePuzzles()[-2]

    # get solver object and user argument
    user_arg : str = None
    solver : Solver = None
    Node.problem = problem
    try:
        user_arg = sys.argv[2]
        solver = search_algorithms[user_arg](problem)
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
