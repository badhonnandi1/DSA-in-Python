from createBT import *
from Queue import *

def levelOrderTraversal(rootNode):
    if not rootNode:
        return

    else:
        customQueue = Queue()
        customQueue.enqueue(rootNode)

        while not customQueue.isEmpty():
            root = customQueue.dequeue()
            print(root.value)
            if (root.leftChild):
                customQueue.enqueue(root.leftChild)

            if (root.rightChild):
                customQueue.enqueue(root.rightChild)

levelOrderTraversal(newBT)