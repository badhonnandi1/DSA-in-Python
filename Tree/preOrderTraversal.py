from createBT import *

def preOrderTraversal(rootNode):
    if not rootNode:                        #---> O(1)
        return

    print(rootNode.value)                   #--->O(1)

    preOrderTraversal(rootNode.leftChild)    #---->O(n/2)
    preOrderTraversal(rootNode.rightChild)   #---->O(n/2)

preOrderTraversal(newBT)                     #final --> O(n) time complexity and space complexity
                                              #as we are using stack memory so same space complexity