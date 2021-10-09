class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class CircularLinkedList:
    def __init__(self):
        self.head = Node(data='head')
        self.head.next = self.head
        
        
        self.size = 0
    
    def is_empty(self):
        '''Checks if the class is empty'''
        return self.size == 0

    def add(self, value):
        '''Adding value as node object to the class'''
        node = Node(data=value, next=self.head.next)
        self.head.next = node
        self.size += 1

    def delete(self, value):
        '''Delete a node by it's a value'''
        node = self.head
        while (node.next.data != node.data):
            if node.data == value:
                node.data = node.next.data
                node.next = node.next.next
                self.size -= 1
                break
            node = node.next

    def __len__(self):
        '''returning the len of the list'''
        return self.size

    def __str__(self):
        '''print's the nodes of the class as string'''
        if self.is_empty():
            return "[]"
        else:
            node = self.head
            output = []
            for i in range(self.size+2):
                exec(f"output.append(str(node{'.next'*i}.data))")
            return '['+', '.join(output)+']'


# for testing
if __name__ == "__main__":
    clst = CircularLinkedList()
    
    clst.add(1)
    clst.add(2)
    clst.add(3)
    clst.add(4)
    clst.add(5)
    clst.add(6)
    print('The circle \n')
    print(clst.head.data)
    print(clst.head.next.data)
    print(clst.head.next.next.data)
    print(clst.head.next.next.next.data)
    print(clst.head.next.next.next.next.data)
    print(clst.head.next.next.next.next.next.data)
    print(clst.head.next.next.next.next.next.next.data)
    print(clst.head.next.next.next.next.next.next.next.data)
    print(clst.head.next.next.next.next.next.next.next.next.data)
    print(clst.head.next.next.next.next.next.next.next.next.next.data,'\n')
    print('The len and print output \n')
    print('len :',len(clst),' list :',clst)
    clst.delete(6)
    print('len :',len(clst),' list :',clst)
    clst.delete(3)
    print('len :',len(clst),' list :',clst)