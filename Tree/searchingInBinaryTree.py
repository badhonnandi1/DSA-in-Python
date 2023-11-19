from createBT import *
from Queue import *

def searchBT(rootNode,node):    #----->O(n) time complexity and space complexity O(n) --> because we are using custom queue
    if not rootNode:
        return 
    else:
        customQueue = Queue()
        customQueue.enqueue(rootNode)

        while not customQueue.isEmpty():
            root = customQueue.dequeue()
            if root.value == node:
                print("Node found in this tree")
                return root.value
            
            if root.leftChild:
                customQueue.enqueue(root.leftChild)
            if root.rightChild:
                customQueue.enqueue(root.rightChild)

        return "Not found in this tree"

print(searchBT(newBT,'Hot')) 