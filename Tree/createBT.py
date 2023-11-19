class TreeNode:
    def __init__(self,value):
        self.value = value
        self.leftChild = None
        self.rightChild = None

newBT = TreeNode("Drinks")
leftChild = TreeNode("Cold")
rightChild = TreeNode("Hot")

newBT.leftChild = leftChild
newBT.rightChild = rightChild
