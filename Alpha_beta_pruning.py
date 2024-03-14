import math

class Node:
    def __init__(self, value=None):
        self.value = value
        self.children = []

def minimax_alpha_beta(node, depth, alpha, beta, maximizingPlayer):
    if depth == 0 or not node.children:
        return node.value
    
    if maximizingPlayer:
        value = -math.inf
        for child in node.children:
            value = max(value, minimax_alpha_beta(child, depth - 1, alpha, beta, False))
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value
    
    else:
        value = math.inf
        for child in node.children:
            value = min(value, minimax_alpha_beta(child, depth - 1, alpha, beta, True))
            beta = min(beta, value)
            if beta <= alpha:
                break
        return value


    # Construct a simple game tree
root = Node(3)
node1 = Node(5)
node2 = Node(6)
node3 = Node(9)
node4 = Node(1)
node5 = Node(2)
node6 = Node(0)
    
root.children.extend([node1, node2])
node1.children.extend([node3, node4])
node2.children.extend([node5, node6])

# Perform minimax with alpha-beta pruning
result = minimax_alpha_beta(root, 3, -math.inf, math.inf, True)
print("Optimal value:", result) 
