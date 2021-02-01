def bubble_sort(lst):
    """
    ------ Pseudocode Steps -----
    begin BubbleSort(list)
            for all elements of list
                if list[i] > list[i+1]
                    swap(list[i], list[i+1])
                end if
            end for   
        return list   
    end BubbleSort
        
    ------ Doctests -----        
    >>> unsorted_list = [8,4,3,7,87,5,64,6,73]
    >>> sorted_list = insertion_sort(unsorted_list)
    >>> sorted_list
    [3, 4, 5, 6, 7, 8, 64, 73, 87]
    """

    for h in range(len(lst)):        
        for i in range(len(lst)-h-1):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
        
    return lst