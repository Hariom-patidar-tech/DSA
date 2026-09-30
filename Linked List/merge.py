class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def merge_sorted_lists(head1, head2):

    dummy = Node(0)
    tail = dummy

    while head1 and head2:

        if head1.data < head2.data:
            tail.next = head1
            head1 = head1.next
        else:
            tail.next = head2
            head2 = head2.next

        tail = tail.next

    if head1:
        tail.next = head1

    if head2:
        tail.next = head2

    return dummy.next

head1 = Node(10)
head1.next = Node(20)
head1.next.next = Node(40)

head2 = Node(15)
head2.next = Node(30)
head2.next.next = Node(50)

merged = merge_sorted_lists(head1, head2)

temp = merged
while temp:
    print(temp.data, end=" -> ")
    temp = temp.next

print("None")