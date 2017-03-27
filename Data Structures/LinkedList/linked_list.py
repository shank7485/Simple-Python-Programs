class Node(object):
    def __init__(self, data):
        self.next = None
        self.data = data


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_head(self, data):
        new_node = Node(data)
        # Check if list is empty. If empty,  both head, tail are same.
        if self.head == None and self.tail == None:
            self.head = new_node
            self.tail = new_node
        else:
            # Update list head with new node.
            old_head = self.head
            new_node.next = old_head
            self.head = new_node

    def add_to_tail(self, data):
        new_node = Node(data)
        # Check if list is empty. If empty,  both head, tail are same
        if self.head == None and self.tail == None:
            self.head = new_node
            self.tail = new_node
        else:
            # Update list tail with new node.
            old_tail = self.tail
            old_tail.next = new_node
            self.tail = new_node


    def print_all_elements(self):
        if self.head:
            # Check if list is not empty.
            current = self.head
            while current.next != None:
                print(current.data),
                current = current.next
            # current.next in while loop does not print the last element. Hence
            # the follwing is done.
            print(current.data),
        else:
            print("List Empty.")

    def delete_element(self, data):
        current = self.head
        if current.data == data:
            # Deleting in head.
            self.head = current.next
            current = current.next
        while current.next != None:
            # Here prev is used to store the the previous node.
            if current.data == data:
                prev.next = current.next
            else:
                # This condition to check if deletion occur even when there are
                # entries back to back. Without it, the logic will skip.
                prev = current
            current = current.next
        # Finally, to check if the final element is the data. prev will have
        # the previous node. That will become the tail.
        if current.data == data:
            prev.next = None
        self.tail = prev

a = LinkedList()
a.add_to_tail(1)
a.add_to_tail(3)
a.add_to_tail(2)
a.add_to_tail(4)
a.add_to_tail(3)
a.add_to_tail(3)
a.add_to_head(3)
a.delete_element(3)
a.print_all_elements()