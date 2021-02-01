def insertion_sort(lst):
    """
    ------ Pseudocode Steps -----
    Step 1 − If it is the first element, it is already sorted. return 1;
    Step 2 − Pick next element
    Step 3 − Compare with all elements in the sorted sub-list
    Step 4 − Shift all the elements in the sorted sub-list that is greater than the 
            value to be sorted
    Step 5 − Insert the value
    Step 6 − Repeat until list is sorted

    Useful diagram:
    https://media.geeksforgeeks.org/wp-content/uploads/insertionsort.png

    ------ Doctests -----        
    >>> unsorted_list = [8,4,3,7,87,5,64,6,73]
    >>> sorted_list = insertion_sort(unsorted_list)
    >>> sorted_list
    [3, 4, 5, 6, 7, 8, 64, 73, 87]
    """
    for i in range(len(lst)):
        low_val = lst[i]
  
        j = i-1
        while j >= 0 and low_val < lst[j] : 
                lst[j + 1] = lst[j] 
                j -= 1
                
        lst[j + 1] = low_val
    
    return lst
