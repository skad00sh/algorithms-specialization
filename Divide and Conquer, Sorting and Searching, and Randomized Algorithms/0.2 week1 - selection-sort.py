def selection_sort(lst):
    """
    *Pseudo code*
    Step 1 − Set MIN to location 0
    Step 2 − Search the minimum element in the list
    Step 3 − Swap with value at location MIN
    Step 4 − Increment MIN to point to next element
    Step 5 − Repeat until list is sorted

    Useful diagram:
    https://media.geeksforgeeks.org/wp-content/cdn-uploads/Selection-sort-flowchart.jpg

    ------- Doctest -------
    >>> unsorted_list = [8,4,3,7,87,5,64,6,73]
    >>> sorted_list = selection_sort(unsorted_list)
    >>> sorted_list
    [3, 4, 5, 6, 7, 8, 64, 73, 87]

    """
    
    for i in range(len(lst)):
        min_index = i
        
        for j in range(i+1, len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j
        
        lst[i], lst[min_index] = lst[min_index], lst[i]
    
    return lst

