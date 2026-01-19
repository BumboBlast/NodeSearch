'''
function CHILD-NODE ( problem, parent, action) returns a node
    return a node with
        STATE = problem.RESULT (parent.STATE , action),
        PARENT = parent, 
        ACTION = action,
        PATH-COST = parent.PATH-COST + problem.STEP-COST (parent.STATE , action )
'''
from __future__ import annotations
from Problem.Problem import Problem

class Node:
    # hopefully static
    problem : Problem = None

    def __init__(self, parent : Node | None = None, state: str | None = ''):
        self.state : str = state
        self.parent : Node | None = parent
        self.action : function | None = None
        self.path_cost : int = 0
    
    def __str__(self):
        _parent: Node | None = None
        if (not self.parent):
            _parent = Node()
        else:
            _parent = self.parent
        str_dict: dict = {
            "state" : str(self.state),
            "action" : self.action.__name__,
            "path_cost (cumulative)" : self.path_cost,
            "parent_state" : str(_parent.state)
        }
        return str(str_dict)

    def get_state(self) -> object:
        ''' returns the state, but in a getter so can return a hashable or something maybe'''
        # print('called get state')
        return self.state

    def set_state(self, new_state: object) -> None:
        ''' assigns state, but in a setter so can insert whatever i want in the call '''
        self.state = new_state

    #@staticmethod
    def child_node(self, problem: Problem, action: function) -> Node:
        '''Return a child node from this node, given an aciton
        '''
        child_node : Node = Node()
        child_node.state = problem.result(self.state, action)
        child_node.parent = self
        child_node.action = action
        child_node.path_cost = self.path_cost + problem.step_cost(self.state, action)
        return child_node

    chainStr: str = str()
    @staticmethod
    def getNodeChainRecursive(myNode: Node, short: bool = True) -> str:
        ''' Return str for each node, starting with self going up through its parent and so on
        until root (no parent).
        '''
        if myNode.parent:
            Node.chainStr += Node.getNodeChainRecursive(myNode.parent, short)
        
        if myNode.action:
            Node.chainStr += myNode.get_state() + '\t' + myNode.action.__name__ + '\n'
        else:
            Node.chainStr += myNode.get_state() + '\t' + 'Root' + '\n'
        return Node.chainStr
    
    @staticmethod
    def getNodeChainIterative(myNode: Node, short: bool = False) -> list:
        ''' Return list of str for each node, starting with self going up through its parent and so on
        until root (no parent).
        '''
        orderedNodeChain: list = list()
        for __ in range(0, 100_000):
            if myNode.action:
                orderedNodeChain.append({Node.problem.print_state(myNode.get_state(), short) : myNode.action.__name__})
            else:
                orderedNodeChain.append({Node.problem.print_state(myNode.get_state(), short) : 'Root'})
            
            if myNode.parent:
                myNode = myNode.parent
            else:
                break
        return orderedNodeChain
