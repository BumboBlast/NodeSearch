

from ChildNodeTest import Node
from ProblemTest import EightPuzzle
from SearchBreadthFirst import BrFS
# import queue

print('(:')

# newPuzzle : EightPuzzle = EightPuzzle()
# coolNode : Node = Node()

# coolNode.state.info = newPuzzle.initial_state
# print(coolNode.state)
# print(coolNode.child_node(EightPuzzle, EightPuzzle.moveDown).state)
# print(coolNode.child_node(EightPuzzle, EightPuzzle.moveRight).state)


# newEightPuzzle : EightPuzzle = EightPuzzle('123456780')
# newEightPuzzle : EightPuzzle = EightPuzzle('876543210')
# newEightPuzzle : EightPuzzle = EightPuzzle('102345678')
# newEightPuzzle : EightPuzzle = EightPuzzle('376041825') # impossible to solve, odd # of inversions
# newEightPuzzle : EightPuzzle = EightPuzzle('402176583') # impossible to solve, odd # of inversions
newEightPuzzle : EightPuzzle = EightPuzzle() # random puzzle
newEightPuzzle.solution_state = '012345678'
solver: BrFS = BrFS(newEightPuzzle)

print('solvable: ' + str(newEightPuzzle.is_solvable()))

solution_node : Node = solver.breastFirstSearch()

if solution_node:
    solution_chain: list = Node.getNodeChainIterative(solution_node, short=True)
    print('solution chain is ' + str(len(solution_chain)) + ' nodes')
    for n in solution_chain[::-1]:
        print(str(n))
else:
    print('no solution ):')

