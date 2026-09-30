class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    def delete_position(self, position):

        if self.head is None:
            return

        if position == 0:
            self.head = self.head.next
            return

        temp = self.head

        for i in range(position - 1):
            if temp is None or temp.next is None:
                return
            temp = temp.next

        if temp.next:
            temp.next = temp.next.next

ll = LinkedList()

ll.insert_end(10)
ll.insert_end(20)
ll.insert_end(30)
ll.insert_end(40)

ll.delete_position(2)

temp = ll.head
while temp:
    print(temp.data, end=" -> ")
    temp = temp.next
print("None")