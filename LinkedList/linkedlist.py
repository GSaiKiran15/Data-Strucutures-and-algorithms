class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self, head=None):
        self.head = head
    
    def insert_head(self, value):
        node = Node(value, self.head)
        self.head = node

    def insert_last(self, value):
        if self.head is None:
            self.head = Node(value, None)
        iterator = self.head
        while iterator.next:
            iterator = iterator.next
        iterator.next = Node(value, None)
        
    def insert_values(self, data: list):
        for i in data:
            self.insert_last(i)

    def print_ll(self):
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
            iterator.next = Node(value, temp)

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
                iterator.next = Node(data_to_insert, iterator.next.next)
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

ll = LinkedList()
ll.insert_values(["banana","mango","grapes","orange"])
ll.print_ll()
ll.insert_after_value("mango","apple") # insert apple after mango
ll.print_ll()
ll.remove_by_value("orange") # remove orange from linked list
ll.print_ll()
ll.remove_by_value("figs")
ll.print_ll()
ll.remove_by_value("banana")
ll.remove_by_value("mango")
ll.remove_by_value("apple")
ll.remove_by_value("grapes")
ll.print_ll()