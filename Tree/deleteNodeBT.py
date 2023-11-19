from createBT import *
from Queue import *


def getDepestNode(rootNode):
    if not rootNode:
        return
    else:
        customQueue = Queue()
        customQueue.enqueue(rootNode)

        while not customQueue.isEmpty():
            root = customQueue.dequeue()

            if root.leftChild:
                customQueue.enqueue(root.leftChild)
            if root.rightChild:
                customQueue.enqueue(root.rightChild)
        
        deepestNode = root
        return deepestNode


def deleteDeepestNode(rootNode,dNode):
    if not rootNode:
        return
    else:
        customQueue = Queue()
        customQueue.enqueue(rootNode)

        while not customQueue.isEmpty():
            root = customQueue.dequeue()

            if root.value == dNode:
                root = None
                return
            
            if root.rightChild:
                if root.rightChild.value == dNode.value:
                    root.rightChild = None
                    return
                else:
                    customQueue.enqueue(root.rightChild)
            
            if root.leftChild:
                if root.leftChild.value == dNode.value:
                    root.rightChild = None
                    return
                else:
                    customQueue.enqueue(root.leftChild)


def deleteNodeBT(rootNode,node):
    if not rootNode:
        return
    
    else:
        customQueue = Queue()
        customQueue.enqueue(rootNode)

        while not customQueue.isEmpty():
            root = customQueue.dequeue()

            if root.value == node.value:

                dNode = getDepestNode(rootNode)
                root.value = dNode.value
                
                deleteDeepestNode(rootNode,dNode)
                return "The node has been deleted successfully"
            
            if root.leftChild:
                customQueue.enqueue(root.leftChild)
            
            if root.rightChild:
                customQueue.enqueue(root.rightChild)
        
        return "Failed to delete as there is not node with same value"


node = TreeNode('Cold')
deleteNodeBT(newBT,node)


# in this case we are deleting the node with value 'Cold' and we are replacing it with the deepest node in the tree and then deleting the deepest node, and we are doing this by using the custom queue