
# TREE TRAVERSAL
# ref:  https://en.wikipedia.org/wiki/Tree_traversal

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorder_recursive(node: TreeNode) -> [TreeNode]:
    visit = []
    def recursive_function(node: TreeNode) -> None:
        if node == None:
            return
        visit.append(node)
        recursive_function(node.left)
        recursive_function(node.right)
    recursive_function(node)
    return visit

def preorder(node: TreeNode) -> [TreeNode]:
    if node == None:
        return
    stack = []
    visit = []
    stack.append(node)
    while stack:
        node = stack.pop()
        visit.append(node)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return visit

def postorder_recursive(node: TreeNode) -> [TreeNode]:
    visit = []
    def recursive_function(node: TreeNode) -> None:
        if node == None:
            return
        recursive_function(node.left)
        recursive_function(node.right)
        visit.append(node)
    recursive_function(node)
    return visit


def postorder(node: TreeNode) -> [TreeNode]:
    visit = []
    stack = []
    lastNodeVisited = None
    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            peekNode = stack[-1]
            if peekNode.right and lastNodeVisited != peekNode.right:
                node = peekNode.right
            else:
                visit.append(peekNode)
                lastNodeVisited = stack.pop()
    return visit
    
def inorder_recursive(node: TreeNode) -> [TreeNode]:
    visit = []
    def recursive_function(node: TreeNode) -> None:
        if node == None:
            return
        recursive_function(node.left)
        visit.append(node)
        recursive_function(node.right)
    recursive_function(node)
    return visit
    


def inorder(node: TreeNode) -> [TreeNode]:
    stack = []
    visit = []
    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            visit.append(node)
            node = node.right
    return visit

def isSymmetric(root):
    def isMirror(left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        return (left.value == right.value) and isMirror(left.left, right.right) and isMirror(left.right, right.left)

    if not root:
        return True
    return isMirror(root.left, root.right)

def maxDepth(root):
    if not root:
        return 0
    left_depth = maxDepth(root.left)
    right_depth = maxDepth(root.right)
    return max(left_depth, right_depth) + 1

def sortedArrayToBST(nums):
    '''Given an integer array nums where the elements are sorted in ascending order, convert it to a 
       height-balanced binary search tree'''
    if not nums:
        return None

    mid = len(nums) // 2
    root = TreeNode(nums[mid])
    
    root.left = sortedArrayToBST(nums[:mid])
    root.right = sortedArrayToBST(nums[mid + 1:])
    
    return root


# re: https://stackoverflow.com/questions/10171844/breadth-first-traversal-for-a-tree-python?rq=3
from collections import deque

def bfs(node: TreeNode) -> dict[TreeNode:TreeNode]:
    P, Q = {node: None}, deque([node]) 
    while Q:
        u = Q.popleft() 
        for v in [u.left, u.right]:
            if v:
                if v in P: continue 
                P[v] = u 
                Q.append(v)
    return P


def buildTree(preorder_values, inorder_values):
    if not preorder_values or not inorder_values:
        return None
    root_val = preorder_values.pop(0)
    root = TreeNode(root_val)
    
    inorder_values_index = inorder_values.index(root_val)
    
    root.left = buildTree(preorder_values, inorder_values[:inorder_values_index])
    root.right = buildTree(preorder_values, inorder_values[inorder_values_index + 1:])
    
    return root

def printinorder_values(node):
    if node:
        printinorder_values(node.left)
        print(node.val, end=" ")
        printinorder_values(node.right)

# Input
preorder_values = ['F', 'B', 'A', 'D', 'C', 'E', 'G', 'I', 'H']
inorder_values = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
postorder_values = ['A', 'C', 'E', 'D', 'B', 'H', 'I', 'G', 'F']


# build the tree from preorder_values and inorder_values
root = buildTree(preorder_values, inorder_values)


#TESTS


print('Test all functions: inorder, inorder_recursive, preorder, preorder_recursive, postorder, postorder_recursive')
assert [node.val for node in inorder(root)] == ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'], 'inorder traversal iterative'
print('inorder traversal iterative have pass')
assert [node.val for node in inorder_recursive(root)] == ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'], 'inorder traversal recursive'
print('inorder traversal recursive have pass')
assert [node.val for node in postorder(root)  if node] == ['A', 'C', 'E', 'D', 'B', 'H', 'I', 'G', 'F'], 'postorder traversal iterative'
print('postorder traversal iterative have pass')
assert [node.val for node in postorder_recursive(root)] == ['A', 'C', 'E', 'D', 'B', 'H', 'I', 'G', 'F'], 'postorder traversal recursive'
print('postorder traversal recursive have pass')
assert [node.val for node in preorder(root)  if node] == ['F', 'B', 'A', 'D', 'C', 'E', 'G', 'I', 'H'], 'preorder traversal iterative'
print('preorder traversal iterative have pass')
assert [node.val for node in preorder_recursive(root)  if node] == ['F', 'B', 'A', 'D', 'C', 'E', 'G', 'I', 'H'], 'preorder traversal recursive'
print('preorder traversal recursive have pass')
print('All tests have pass')

