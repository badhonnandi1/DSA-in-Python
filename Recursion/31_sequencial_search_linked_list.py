from linked_list_create import LinkedList

mylist = LinkedList()
mylist.insert(1,0)
mylist.insert(2,1)
mylist.insert(3,2)
mylist.insert(4,0)
mylist.insert(5,1)

#4->5->1->2->3
#Implement a recursive function for Sequential search in a sequence for linked list?

def findElement(head,target,idx):
    if head == None:
        return -1
    elif head.value == target:
        return idx
    else:
        return findElement(head.next,target,idx+1)

print(findElement(mylist.head,3,0)) # 4
