'''
#### oraginal prb link : https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/4_HashTable_2_Collisions/4_hash_table_exercise.md

Ex (1) weather.csv contains new york city weather for first few days in the month of January. Write a program that can answer following,
    I| What was the average temperature in first week of Jan?
    II| What was the maximum temperature in first 10 days of Jan?

*** Figure out data structure that is best for this problem

Ex (2) nyc_weather.csv contains new york city weather for first few days in the month of January. Write a program that can answer following,
    I| What was the temperature on Jan 9?
    II| What was the temperature on Jan 4?

*** Figure out data structure that is best for this problem

Ex (3) poem.txt Contains famous poem "Road not taken" by poet Robert Frost. You have to read this file in python 
and print every word and its count as show below. Think about the best data structure that you can use to solve 
this problem and figure out why you selected that specific data structure.

Ex (4) Implement hash table where collisions are handled using linear probing. We learnt about linear probing 
in the video tutorial. Take the hash table implementation that uses chaining and modify methods to use linear probing. 
Keep MAX size of arr in hashtable as 10.
'''
import csv

def print_csv_data(data_sheet):
    csv_file = open(data_sheet)
    reader = csv.reader(csv_file)

    data = [(i,j) for i, j in reader]
    
    print('c.s.v data set -->')
    itr = '-'*25
    for i in range(len(data)):
        print(f'{data[i][0]}   |   {data[i][1]} \n{itr}')

def print_txt_data(txt_file):
    with open(txt_file) as f:
        for line in f:
            print(line, end="")

def ex_1():
    print_csv_data('weather.csv')
    arr = []

    with open("weather.csv","r") as f:
        for line in f:
            tokens = line.split(',')
            try:
                temperature = int(tokens[1])
                arr.append(temperature)
            except:
                pass

    print(f'The average temperature in first week of Jan is {sum(arr[:7])}')
    print(f'The maximum temperature in first 10 days of Jan is {max(arr[:10])}')

def ex_2():
    print_csv_data('weather.csv')
    hash_map = {}

    with open("weather.csv","r") as f:
        for line in f:
            tokens = line.split(',')
            try:
                hash_map[tokens[0]] = int(tokens[1])
            except:
                pass

    print('The temperature on Jan 9 was', hash_map['Jan 9'])
    print('The temperature on Jan 4 was', hash_map['Jan 4'])
        
def ex_3():
    print_txt_data('poem.txt')
    print('\n')
    hash_map = {}

    with open("poem.txt","r") as f:
        for line in f:
            words = line.split()
            for word in words:
                if word in hash_map.keys():
                    hash_map[word] += 1
                else:
                    hash_map[word] = 1

    print(hash_map) 

# EX 4
class HashTable:  
    def __init__(self):
        self.MAX = 10 # I am keeping size very low to demonstrate linear probing easily but usually the size should be high
        self.arr = [None for i in range(self.MAX)]
        
    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX
    
    def __getitem__(self, key):
        h = self.get_hash(key)
        if self.arr[h] is None:
            return
        prob_range = self.get_prob_range(h)
        for prob_index in prob_range:
            element = self.arr[prob_index]
            if element is None:
                return
            if element[0] == key:
                return element[1]
           
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        if self.arr[h] is None:
            self.arr[h] = (key,val)
        else:
            new_h = self.find_slot(key, h)
            self.arr[new_h] = (key,val)
        print(self.arr)
        
    def get_prob_range(self, index):
        return [*range(index, len(self.arr))] + [*range(0,index)]
    
    def find_slot(self, key, index):
        prob_range = self.get_prob_range(index)
        for prob_index in prob_range:
            if self.arr[prob_index] is None:
                return prob_index
            if self.arr[prob_index][0] == key:
                return prob_index
        raise Exception("Hashmap full")
        
    def __delitem__(self, key):
        h = self.get_hash(key)
        prob_range = self.get_prob_range(h)
        for prob_index in prob_range:
            if self.arr[prob_index] is None:
                return # item not found so return. You can also throw exception
            if self.arr[prob_index][0] == key:
                self.arr[prob_index]=None
        print(self.arr)


if __name__ == "__main__":
    ex_3()
    
