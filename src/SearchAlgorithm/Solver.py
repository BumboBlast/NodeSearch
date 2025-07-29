
from Node import Node

class Solver:
    def __init__(self):
        pass

    def search(self):
        pass

    @staticmethod
    def get_solution(solution_node: Node | object) -> list:
        solution_chain: list = list()
        if solution_node:
            solution_chain = Node.getNodeChainIterative(solution_node, short=True)
        return solution_chain