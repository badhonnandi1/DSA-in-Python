class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None


class Queue:
  def __init__(self):
    self.linkedlist = LinkedList()

  def enqueue(self,value):
    node = Node(value)
    if self.linkedlist.head == None:
      self.linkedlist.head = node
      self.linkedlist.tail = node
    else:
      self.linkedlist.tail.next = node
      self.linkedlist.tail = node

  def dequeue(self):
    popped = self.linkedlist.head
    if self.linkedlist.head == self.linkedlist.tail:
      self.linkedlist.head = None
      self.linkedlist.tail = None
    else:
      self.linkedlist.head = self.linkedlist.head.next
    return popped.value

  def isEmpty(self):
    if self.linkedlist.head == None:
      return True
    else:
      return False

  def delete(self):
    if self.isEmpty():
      print("Noting to delete from the empty queue")
    else:
      self.linkedlist.head = None
      self.linkedlist.tail = None
      print("Full Queue deleted")

  def peek(self):
    if self.isEmpty():
      return "The queue is Empty"
    else:
      return self.linkedlist.head.value