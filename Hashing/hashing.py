class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
    
arr = [None] * 7
existing_array = ['Apple', 'Orange', 'Banana', 'Mango', 'Pineapple', 'Grapes', 'Watermelon']

def hash_function(value,size):
    val = 0
    for i in value:
        val += ord(i)
    return val % size

def insert(arr,final):
    for i in range(len(arr)):
        hash_idx = hash_function(arr[i],7)
        node = Node(arr[i])
        if final[hash_idx] == None:
            final[hash_idx] = node
        else:
            node.next = final[hash_idx]
            final[hash_idx] = node

def search(value,arr):
    hash_idx = hash_function(value,7)
    temp = arr[hash_idx]
    while temp:
        if temp.value == value:
            return True
        temp = temp.next
    return False

def delete(new,element):
    hash_key = hash_function(element,new)
    temp = new[hash_key]
    if temp.value == element:
        new[hash_key] = temp.next
    else:
        while temp and temp.next:
            if temp.next.value == element:
                temp.next = temp.next.next
                break
            temp = temp.next


def print_linked_list(head):
    while head != None:
        print(head.value, end = '-> ')
        head = head.next
    print('None')
    print()

# print(arr)
def print_arr(arr):
    for i in range(len(arr)):
        print_linked_list(arr[i])

print_arr(arr)
insert(existing_array,arr)
