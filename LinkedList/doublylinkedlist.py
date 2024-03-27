class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class LinkedList:
    def __init__(self, head=None):
        self.head = head
    
    def insert_head(self, value):
        node = Node(value, self.head, None)
        self.head = node
        self.head.prev = None # Change node

    def insert_last(self, value):
        if self.head is None:
            self.head = Node(value, None, None)
            return
        iterator = self.head
        while iterator.next:
            iterator = iterator.next
        iterator.next = Node(value, None, iterator)
        
    def insert_values(self, data: list):
        for i in data:
            self.insert_last(i)

    def print_forward(self):
        iterator = self.head
        output = ""
        while iterator:
            output += f"{iterator.data} --> "
            iterator = iterator.next
        print(output)

    def get_length(self):
        length = 0
        iterator = self.head
        while iterator:
            length += 1
            iterator = iterator.next
        return length

    def insert_at(self, index, value):
        if index == 0:
            self.insert_head(value)
        elif index == self.get_length() + 1:
            self.insert_last(value)
        elif index > self.get_length() or index < 0:
            raise Exception("Recheck Index Value.")
        else:
            iterator = self.head
            for _ in range(index-2):
                iterator = iterator.next
            print(iterator.data)
            temp = iterator.next
            iterator.next = Node(value, temp, iterator)

    def remove_at(self, index):
        if index > self.get_length() or index < 0:
            print("Recheck Index!")
        
        else:
            iterator = self.head
            for _ in range(index-2):
                iterator = iterator.next
            iterator.next = iterator.next.next

#Exercise
    #1
    def insert_after_value(self, data_after, data_to_insert):
        iterator = self.head
        while iterator:
            if iterator.data == data_after:
                iterator.next = Node(data_to_insert, iterator.next.next, iterator.next)
                return
            iterator = iterator.next
        raise Exception("data_after value not found!")

    def remove_by_value(self, data):
        iterator = self.head
        while iterator.next:
            if iterator.next.data == data:
                iterator.next = iterator.next.next
                break
            iterator = iterator.next

    def print_backward(self):
        iterator = self.head
        output = ""
        while iterator.next:
            iterator = iterator.next
        while iterator:
            output += f"{iterator.data} --> "
            iterator = iterator.prev
        print(output)
        return output

    # def print_backward(self):
    #     if self.head is None:
    #         print("Linked list is empty")
    #         return

    #     last_node = self.get_last_node()
    #     itr = last_node
    #     llstr = ''
    #     while itr:
    #         llstr += f"{itr.data} -->"
    #         itr = itr.prev
    #     print("Link list in reverse: ", llstr)

    def get_last_node(self):
        itr = self.head
        while itr.next:
            itr = itr.next

        return itr

linked_list = LinkedList()
linked_list.insert_values([1,2,3,4,5,6,7,8,9,10])
linked_list.print_forward()
linked_list.print_backward()