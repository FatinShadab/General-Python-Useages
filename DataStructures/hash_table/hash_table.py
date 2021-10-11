class HashTable:
    '''A demo class of python dict and hashmap ds'''
    def __init__(self):
        '''initializing the HashTable class'''
        self.Max = 100
        self.arr = [[] for i in range(self.Max)]

    def _get_hash(self, key):
        '''get a index vlaue from the key to store data'''
        h = 0
        for char in key:
            h += ord(char)
        return h % self.Max

    def __setitem__(self, key, val):
        '''Set the data at index generated from the key'''
        h = self._get_hash(key)
        found = False

        for idx, ele in enumerate(self.arr[h]):
            if len(ele) == 2 and ele[0] == key:
                self.arr[h][idx] = (key, val)
                found = True
                break
        
        if not found:
            self.arr[h].append((key, val))

    def __getitem__(self, key):
        '''get the item by key'''
        h = self._get_hash(key)
        for ele in self.arr[h]:
            if ele[0] == key:
                return self.arr[self._get_hash(key)][0][1]

    def __delitem__(self, key):
        '''delete item by key'''
        h = self._get_hash(key)
        for idx, ele in enumerate(self.arr[h]):
            if ele[0] == key:
                del self.arr[h][idx]

# for test usages
if __name__ == "__main__":
    day = ['march 6', '7-Mar', '8-Mar', '9-Mar', '10-Mar', '11-Mar']
    stock_price = [310, 340, 380, 302, 297, 323]

    hashtable = HashTable()
    for i in range(len(day)):
        hashtable[day[i]] = stock_price[i]
    print(hashtable['march 6'])
    print(hashtable['7-Mar'])
    print(hashtable['8-Mar'])
    print(hashtable['9-Mar'])
    hashtable['7-Mar'] = 1020
    del hashtable['9-Mar']
    print(hashtable['9-Mar'])
