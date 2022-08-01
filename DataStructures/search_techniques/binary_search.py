"""
        *** TO USE BINARY SEARCH IN A ARRAY, THE ARRAY HAS TO BE SORTED (ASENDING ORDER)! ***
        *** TIME COMPLEXITY : LOG(N)

        If the input is a array of size 10, given below,

        index - 0 1 2 3 4 5 6 7 8 9
                | | | | | | | | | |
        value - 1 2 3 4 5 6 7 8 9 10

        and if we want to search for the index of element 9 in the array
        with binary search, we need to find the lowerbound, upperbound and
        mid of the array.

        let lb = lowerbound,
            ub = upperbound,
            md = mid

        Attempt 1:

                    lb      md        ub          mid = int((lb+ub)/2)
                    |       |         |               = int((0+9)/2)
            index - 0 1 2 3 4 5 6 7 8 9               = int(4.5)
                    | | | | | | | | | |               = 4
            value - 1 2 3 4 5 6 7 8 9 10

            target value(9) > mid value(5)

            will do Attempt 2.

        Theory :

            Attempt 1:
                At first we will check if the value in "mid index" of the array is the target element
                if so we will return the mid index.

            If not so,

            we have to do 1 more task and then repeat "Attempt 1"

            Task:
                * check if the target element is greater than the value in mid or less then mid.
                
                    ** if the target_value > value in mid:
                        then set the lowerbound at mid+1 and recalculate the mid.
                        At the end repeat  "Attempt 1"

                    ** if the value < value in mid:
                        then set the upperbound at mid-1 and recalculate the mid.
                        At the end repeat  "Attempt 1"

            Retpeat those 2 tasks untill we found the element if it is in array.    

        Attempt 2:

                              lb  md  ub          mid = int((lb+ub)/2)
                              |   |   |               = int((5+9)/2)
            index - 0 1 2 3 4 5 6 7 8 9               = int(7)
                    | | | | | | | | | |               = 7
            value - 1 2 3 4 5 6 7 8 9 10

            target value(9) > mid value(8)

            will do Attempt 3.

        Attempt 3:                  
                                    md
                                    lbub          mid = int((lb+ub)/2)
                                    | |               = int((8+9)/2)
            index - 0 1 2 3 4 5 6 7 8 9               = int(8.5)
                    | | | | | | | | | |               = 8
            value - 1 2 3 4 5 6 7 8 9 10

            target value(9) == mid value(9)

            target value matched with value in mid. will return mid as index. 
"""

from datetime import timedelta
from timeit import default_timer as timer

def binary_search(array: list, ele: int, lb: int, ub: int) -> int:
    if lb <= ub:
        mid = int((lb+ub)/2)
        #print(f"lb - {lb}, ub - {ub}, mid - {mid}, target_ele - {ele}, mid_element - {array[mid]}")

        if ele == array[mid]:
            return mid
        elif ele > array[mid]:
            return binary_search(array, ele, mid+1, ub)
        else:
            return binary_search(array, ele, lb, mid-1)
    else:
        return -1
 
def binary_search_2(array: list, ele: int, lb: int, ub: int) -> int:
    mid = int((lb+ub)/2)
    while(lb<=ub):
        mid = int((lb+ub)/2)
        #print(f"lb - {lb}, ub - {ub}, mid - {mid}, target_ele - {ele}, mid_element - {array[mid]}")
        if ele == array[mid]:
            #print(f"found {mid}")
            return mid
        elif ele > array[mid]:
            lb = mid+1
        else:
            ub = mid-1
    return -1

if __name__ == "__main__":
    n = int(input("Enter number of elements : "))
    array = list(map(int,input("\nEnter the numbers : ").strip().split()))[:n]
    ele = int(input("Enter the element you want to search - "))

    print("\n")
    start1 = timer()
    ele_idx_1 = binary_search_2(array, ele, 0, len(array)-1)
    end1 = timer()
    start2 = timer()
    ele_idx_2 = binary_search_2(array, ele, 0, len(array)-1)
    end2 = timer()

    if ele_idx_1 >= 0 and ele_idx_2 >= 0:
        print(f"\n The element - {ele} is at index - {ele_idx_1} of array - {array} [Recursive Function][search time : {timedelta(seconds=end1-start1)}]")
        print(f"\n The element - {ele} is at index - {ele_idx_2} of array - {array} [While Loop][search time : {timedelta(seconds=end2-start2)}]")
    else:
        print(f"Didn't found element - {ele} in array - {array} [search time : {timedelta(seconds=end-start)}]")
    