"""
*** Python lists are 'Dynamic Arrays' .
*** Python has no Static Arrays .

*** the BigO time complexity for adding something to a Array ---> O(n)
*** the BigO time complexity for deleting something to a Array ---> O(n)
*** the BigO time complexity for retrive element by value from a Array ---> O(n)
*** the BigO time complexity for retrive element by index from a Array ---> O(1)
*** the BigO time complexity of Array travarsal ---> O(n)
________________________________

EX: I
oraginal problem link --> https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/2_Arrays/2_arrays_exercise.md
***Let us say your expense for every month are listed below,
         I) January - 2200
        II) February - 2350
       III) March - 2600
        IV) April - 2130
         V) May - 2190

Have to do with the data sored in array
1. In Feb, how many dollars you spent extra compare to January?
2. Find out your total expense in first quarter (first three months) of the year.
3. Find out if you spent exactly 2000 dollars in any month
4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
5. You returned an item that you bought in a month of April and
got a refund of 200$. Make a correction to your monthly expense list
based on this
______________________________

EX II
oraginal problem link --> https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/2_Arrays/2_arrays_exercise.md

You have a list of your favourite marvel super heros.
heros=['spider man','thor','hulk','iron man','captain america']

Tasks -->

1. Length of the list
2. Add 'black panther' at the end of this list
3. You realize that you need to add 'black panther' after 'hulk',
   so remove it from the list first and then add it after 'hulk'
4. Now you don't like thor and hulk because they get angry easily :)
   So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
   Do that with one line of code.
5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)
____________________________________

EX III
oraginal problem link --> https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/2_Arrays/2_arrays_exercise.md

Task -->

Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function
"""

# Ex: 1 Array
def ex_1():
    #--------(0:jan)-(1:feb)-(2:mar)-(3:Apr)-(4:may
    expense = [2200, 2350, 2600, 2130, 2190]


    # task 1: In Feb, how many dollars you spent extra compare to January
    print(f'Spent extra {expense[1]-expense[0]} dollars  In Feb compare to January')

    # task 2: Find out your total expense in first quarter (first three months) of the year.
    print(f'total expense in first quarter (first three months) of the year is {sum(expense[:3])} dollars')

    # task 3: Find out if you spent exactly 2000 dollars in any month
    def exactl_value(arr, val):
        if val in arr:
            return True
        else:
            return False

    print(f'spent exactly 2000 dollars in any month? --> {exactl_value(expense, 2000)}')

    # task 4: June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
    expense.append(1980)
    print(f'After June monthly expense is {expense}')

    # task 5: returned an item that you bought in a month of April and got a refund of 200$. Make a correction to your monthly expense list based on this
    expense[3] = expense[3]-200
    print(f'monthly expense list based on new data ---> {expense}')

def ex_2():

    heros = ['spider man','thor','hulk','iron man','captain america']

    # task 1: Length of the list
    print(f'Total {len(heros)} heros on the mission')

    # task 2: Add 'black panther' at the end of this list
    heros.append('black panther')
    print(f'After Black-panther joined the misson heros are -->{heros}')

    # task 3: Add 'black panther' after 'hulk'
    heros.insert(3, heros.pop())
    print(f'black panther stand side by side with hulk. after that --> {heros}')

    # task 4: Replace hulk and thor by doctor strange
    heros[1:3]=['doctor strange']
    print(f'''hulk and thor are going to do something else so doctor strange took thier place in the mission,
    and the team is --> {heros}''')

    # task 5: Sort the heros list in alphabetical order
    heros.sort()
    print(f'After the heros took there proper stand in alphabetical order --> {heros}')

def ex_3(max_num):
    return [num for num in range(1, max_num+1) if num%2 != 0]

if __name__ == "__main__":
    print(ex_3(12))