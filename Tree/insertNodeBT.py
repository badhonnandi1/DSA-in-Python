from createBT import *
from Queue import *

def insertNodeBT(rootNode,node): #----->O(n) time complexity and space complexity O(n) --> because we are using custom queue
    if not rootNode:
        rootNode = node
        return

    else:
        customQueue = Queue()
        customQueue.enqueue(rootNode)

        while not customQueue.isEmpty():
            root = customQueue.dequeue()

            if root.leftChild:
                customQueue.enqueue(root.leftChild)
            else:
                root.leftChild = node
                return "Node inserted as a empty left child"

            if root.rightChild:
                customQueue.enqueue(root.rightChild)
            else:
                root.rightChild = node
                return "Node inserted as a right left child"

cola = TreeNode("Cola")
tree = insertNodeBT(newBT,cola)
fanta = TreeNode("Fanta")
tree = insertNodeBT(newBT,fanta)
