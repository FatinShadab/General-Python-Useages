class Node:
    '''A class to make node objects to store values of linked list.'''
    def __init__(self, data=None, next=None):
        '''Makes a node with a value and a reference of the next node object.'''
        self.data = data
        self.next = next

class SinglyLinkedList:
    ''' Implementation of singly linked-list data structure.'''
    def __init__(self):
        ''' Initializing LinkedList class with a head default none.'''
        self.head = None

    def add_at_start(self, data):
        '''Add value as a node with next object link at index 0,
        replace old head with the new node.'''
        node = Node(data, self.head)
        self.head = node

    def add_at_end(self, data):
        ''' Add a value as a node object at the end'''
        if self.head is None:
            self.head = Node(data)
        else:
            itr = self.head
            while itr.next:
                itr = itr.next

            itr.next = Node(data)

    def append_values(self, data):
        '''Add a list of values at the end'''
        for d in data:
            self.add_at_end(d)

    def insert_values(self, data):
        '''Add a list of values at front'''
        for d in data:
            self.add_at_start(d)

    def get_len(self):
        '''Get the len or number of total nodes stored in the list.'''
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def remove_at(self, index):
        ''' Remove the element of the given index'''
        if index < 0 or index >= self.get_len():
            raise ValueError("Invalid index !")
        if index == 0:
            self.head = self.head.next
            return
        else:
            count = 0
            itr = self.head
            while itr:
                if count == index-1:
                    itr.next = itr.next.next
                    break
                count += 1
                itr = itr.next

    def add_at(self, index, value):
        ''' Add the value at the giveing index'''
        if index < 0 or index > self.get_len():
            raise ValueError("Invalid Index !")
        if index == 0:
            self.add_at_start(value)
        count = 0
        node = Node(value)
        itr = self.head
        while itr:
            if count == (index-1):
                node.next = itr.next
                itr.next = node
                break
            count += 1
            itr = itr.next

    def remove(self, value):
        '''Remove node by its value'''
        itr = self.head
        while itr:
            if itr.data == value:
                itr.data = itr.next.data
                itr.next = itr.next.next
                break
            itr = itr.next

    def __len__(self):
        '''Return the lenght ''' 
        return self.get_len()

    def __str__(self):
        '''return all nodes as str'''
        if self.head is None:
            return ("The linked list is empty !")
        else:
            itr = self.head
            llstr = []
            while itr:
                llstr.append(str(itr.data))
                itr = itr.next
            return '['+', '.join(llstr)+']'

#  for testing and use
if __name__ == "__main__":
    llst = SinglyLinkedList()
    print(llst)
    llst.add_at_start(5)
    llst.add_at_start(7)
    llst.add_at_end(10202)
    llst.append_values(['Red', 'Black', 'Blue', 'Yellow'])
    llst.add_at_start('Hello')
    print(llst.get_len())
    print(llst)
    llst.remove_at(3)
    print(llst)
    llst.remove_at(0)
    print(llst)
    llst.insert_values(['I', 'Am', 'Number', 'One'])
    print(llst)
    print(type(llst))
    llst.add_at(3, "Turja")
    print(llst)
    llst.add_at(0, "Ji")
    print(llst)
    llst.remove('Number')
    print(llst, len(llst))