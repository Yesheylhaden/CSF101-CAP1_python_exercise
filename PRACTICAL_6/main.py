# this is to find the middle value
class linked_list:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = self.Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(" -> ".join(map(str, elements)))
    
    def insert(self, data, position):
        new_node = self.Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        for _ in range(position - 1):
            if current is None:
                raise IndexError("Position out of range")
            current = current.next
        new_node.next = current.next
        current.next = new_node

    def find_middle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data if slow else None

ll = linked_list()
ll.append(1)
ll.append(2)
ll.append(3)
ll.insert(2, 1)
ll.display()
print("middle element:", ll.find_middle())

# find cycle in linked list
class linked_list:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = self.Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def cycle(self):
        slow_pointer = self.head
        fast_pointer = self.head
        while fast_pointer and fast_pointer.next:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
            if slow_pointer == fast_pointer:
                return True
        return False

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print("->".join(map(str, elements)))

ll = linked_list()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)

# creat a cycle to test
ll.head.next.next = ll.head
print("cycle exist:", ll.cycle())

# task 3 remove duplicate
class linked_list:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = self.Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def remove_duplicate(self):
        if not self.head:
            return
        # use set to detect duplicate
        unique_value = set()
        current = self.head
        unique_value.add(current.data) # add the head of linked list to set
        while current.next:
            if current.next.data in unique_value:
                # if duplicate is found, skip the node
                current.next = current.next.next
            else:
                # if unique node found, add the data to set and move to next node
                unique_value.add(current.next.data)
                current = current.next

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print("->".join(map(str, elements)))

ll = linked_list()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)

ll.remove_duplicate()

ll.display()

# task 4_merge two linked list
class linked_list:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = self.Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print("->".join(map(str, elements)))

    def merge_sorted_linked_list(self, sorted_linked_list):
        dummy = self.Node(0) # dummy node for starting point
        tail = dummy
        first_list_pointer = self.head
        second_list_pointer = sorted_linked_list.head

        while first_list_pointer and second_list_pointer:
            if first_list_pointer.data < second_list_pointer.data:
                tail.next = first_list_pointer
                first_list_pointer = first_list_pointer.next
            else:
                tail.next = second_list_pointer
                second_list_pointer = second_list_pointer.next
            tail = tail.next

        tail.next = list1 or list2

        if first_list_pointer:
            tail.next = first_list_pointer
        else:
            tail.next = second_list_pointer

        self.head = dummy.next

list1 = linked_list()
list1.append(1)
list1.append(4)
list1.append(5)
list1.append(7)
list1.append(8)
list1.append(10)

list2 = linked_list()
list2.append(2)
list2.append(5)
list2.append(6)
list2.append(7)
list2.append(8)
list2.append(9)
list2.append(12)
list2.append(15)

list1.merge_sorted_linked_list(list2)
list1.display()

