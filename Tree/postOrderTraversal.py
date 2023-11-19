from createBT import *

def preOrderTraversal(rootNode):
    if not rootNode:
        return
  
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)
  
    print(rootNode.value)

preOrderTraversal(newBT)