from createBT import *

def inOrderTraversal(rootNode):
    if not rootNode:
        return

    inOrderTraversal(rootNode.leftChild)
    print(rootNode.value)
    inOrderTraversal(rootNode.rightChild)

inOrderTraversal(newBT)