#Basic Operations on Linked List
# 1. Insertion --> insert method
# 2. Deletion --> pop method
# 3. Traversal --> __str__ method
# 4. Search --> get method
# 5. Update -> set method
# 6. Delete --> delete method
# 7. Length --> length variable

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0


    def get(self,idx):
        temp = self.head
        for i in range(idx):
            temp = temp.next
        return temp
    

    def insert(self,value,idx):
        node = Node(value)
        if self.head == None:
            self.head = node
        else:
            if idx ==0:
                node.next = self.head
                self.head = node
            
            elif idx == self.length:
                prev = self.get(idx-1)
                prev.next = node
            
            else:
                prev = self.get(idx-1)
                next = prev.next
                prev.next = node
                node.next = next
            self.length += 1
            print("Node inserted successfully")
    
    def __str__(self):
        mystr = ''
        temp = self.head
        while temp:
            mystr += str(temp.value)
            if temp.next:
                mystr += '->'
            temp = temp.next
        return mystr

    def set(self,value,idx):
        node = self.get(idx)
        node.value = value
        print("Value change successfully done")

    def delete(self):
        self.head = None
        self.length = 0
        return ("Linked List deleted successfully")
    
    def pop(self,idx):
        if self.head == None:
            return None
        else:
            if idx == 0:
                node = self.head
                self.head = self.head.next

            elif idx == self.length-1:
                prev = self.get(idx - 1)
                node = prev.next
                prev.next = None

            else:
                prev = self.get(idx - 1)
                node = prev.next
                next = node.next
                prev.next = next

            self.length -=1
            return f"Node {node.value} popped successfully"



if __name__ == "__main__":
    mylist = LinkedList()
    mylist.insert(10,0)
    mylist.insert(20,1)
    mylist.insert(30,2)
    mylist.insert(40,3)
    mylist.insert(50,4)
    print(mylist)
    print("------------------------")
    mylist.set(100,0)
    print(mylist)
    print("------------------------")
    print(mylist.pop(0))
    print(mylist)
    print("------------------------")
    print(mylist.pop(3))
    print(mylist)
    print("------------------------")
    print(mylist.delete())
    print('------------------------')

# output: -->

# Node inserted successfully
# Node inserted successfully      
# Node inserted successfully      
# Node inserted successfully      
# 10->20->30->40->50
# ------------------------        
# Value change successfully done  
# 100->20->30->40->50
# ------------------------        
# Node 100 popped successfully    
# 20->30->40->50
# ------------------------        
# Node 50 popped successfully     
# 20->30->40
# ------------------------        
# Linked List deleted successfully
# ------------------------     