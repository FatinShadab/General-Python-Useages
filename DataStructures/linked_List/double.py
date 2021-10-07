class Node:
    '''A class to store value as a class object.
        Its more like a container to store value'''
    def __init__(self, value=None, prev=None, next=None):
        '''Initializing the Node class and creating node objects with
            the given value, previous node link and next node link.'''
        self.prev = prev
        self.value = value
        self.next = next

class DoubleLinkList:
    '''A class for python implementation of Double Link-List'''
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert(self, value):
        '''Add a value'''
        node = Node(value)
        if self.tail is None:
            self.head = node
            self.tail = node
            self.size += 1
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
            self.size += 1

    def insert_at(self, index, value):
        '''Add a value in given index'''
        count = 0
        node = Node(value)
        itr = self.head
        while itr:
            if count == index-1:
                node.prev = itr
                node.next = itr.next
                itr.next = node
                self.size += 1
                break
            count += 1
            itr = itr.next

    def __remove(self, node):
        '''A private method to remove node'''
        if node.prev is None:
            self.head = node.next
        else:
            node.prev.next = node.next

        if node.next is None:
            self.tail = node.prev
        else:
            node.next.prev = node.prev
        self.size -= 1

    def remove_last(self):
        '''remove the tail'''
        if self.tail:
            self.__remove(self.tail)

    def remove_first(self):
        '''remove the head'''
        if self.head:
            self.__remove(self.head)

    def remove_same(self, value):
        '''remove all the same data which is equivalent to value'''
        node = self.head
        while node:
            if node.value == value:
                self.__remove(node)
            node = node.next

    def __len__(self):
        '''return the leanght'''
        return self.size
    
    def __str__(self):
        '''return all nodes as str'''
        itr = self.head
        output = []
        while itr:
            output.append(str(itr.value))
            itr = itr.next
        return '[' + ', '.join(output) + ']'

# for test and usage
if __name__ == "__main__":
    llst = DoubleLinkList()

    llst.insert(1)
    llst.insert(2)
    llst.insert(5)
    llst.insert(2)
    llst.insert(2)
    llst.insert(5)
    llst.insert(2)
    llst.insert(2)
    llst.insert(2)
    llst.insert(2)
    llst.insert(2)
    llst.insert(2)
    llst.insert(5)
    llst.insert(8)
    print(llst, len(llst))
    llst.remove_same(8)
    print(llst, len(llst))
    llst.remove_same(2)
    print(llst, len(llst))
    llst.remove_last()
    print(llst, len(llst))
    llst.insert_at(2, 10)
    print(llst, len(llst))
    print(llst.head.value, llst.tail.value)
