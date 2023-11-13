from linked_list import LinkedList
mylist = LinkedList()
mylist.insert(1,0)
mylist.insert(2,1)
mylist.insert(3,2)
mylist.insert(4,0)
mylist.insert(5,1)
print(mylist)

#Implement a recursive function to find the length of a linked list?

def lenthOfLinkedList(head):
    temp = head
    if temp == None:
        return 0
    else:
        return 1 + lenthOfLinkedList(temp.next)

print(lenthOfLinkedList(mylist.head))

