class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
    

class LinkedList:
    def __init__(self):
        self.head = None
        self.lenght = 0
    
    def get(self,idx):
        temp = self.head
        for i in range(idx):
            temp = temp.next
        return temp
    
    def insert(self,value,idx):
        if idx<0:
            return None
        else:
            node = Node(value)
            if self.head == None:
                self.head = node
            else:
                if idx == 0:
                    node.next = self.head
                    self.head = node
                elif idx == self.lenght:
                    prev = self.get(idx-1)
                    prev.next = node
                else:
                    prev = self.get(idx-1)
                    next = prev.next
                    prev.next = node
                    node.next = next
            self.lenght += 1
    
    def __str__(self):
        mystr = ''
        temp = self.head
        while temp:
            mystr += str(temp.value)
            if temp.next:
                mystr += '->'
            temp = temp.next
        
        return mystr

