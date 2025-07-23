

from ChildNodeTest import Node
from ProblemTest import EightPuzzle
from SearchBreadthFirst import BrFS
from SearchDepthFirst import DpFS
# import queue

print('(:')

''' puzzles '''
# newEightPuzzle : EightPuzzle = EightPuzzle('123456780')
# newEightPuzzle : EightPuzzle = EightPuzzle('876543210')
# newEightPuzzle : EightPuzzle = EightPuzzle('102345678')
# newEightPuzzle : EightPuzzle = EightPuzzle('376041825') # impossible to solve, odd # of inversions
# newEightPuzzle : EightPuzzle = EightPuzzle('402176583') # impossible to solve, odd # of inversions
newEightPuzzle : EightPuzzle = EightPuzzle('327615084') # a very long solution
# newEightPuzzle : EightPuzzle = EightPuzzle() # random puzzle

''' set up solver object(s) '''
newEightPuzzle.solution_state = '012345678'
BrFSsolver: BrFS = BrFS(newEightPuzzle)
DpFSsolver:  DpFS = DpFS(newEightPuzzle)


''' solve the puzzle '''
print('init:\n' + EightPuzzle.print_state(newEightPuzzle.initial_state))
print('solvable: ' + str(newEightPuzzle.is_solvable()))

# solution_node : Node = BrFSsolver.breastFirstSearch()
solution_node : Node = DpFSsolver.depthFirstSearch()

if solution_node:
    solution_chain: list = Node.getNodeChainIterative(solution_node, short=True)
    print('solution chain is ' + str(len(solution_chain)) + ' nodes')
    # for n in solution_chain[::-1]:
        # print(str(n))
else:
    print('no solution ):')