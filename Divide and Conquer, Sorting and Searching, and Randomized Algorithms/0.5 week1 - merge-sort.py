def merge_and_sort(x,y):
    """
    ------ Pseudocode Steps -----
    Input: sorted arrays C and D (length n/2 each). 
    Output: sorted array B (length n). 
    Simplifying assumption: n is even. (did not assume)
    i := 1
    j := 1
    for k := 1 to n do 
        if C[i] <D [j] then 
            B[k] :=C[i]     // populate output array 
            i := i +1       // increment i 
        else                // D[j] <C [i] 
            B[k] :=D[j] 
            j := j +1
            
    ------ Doctests ------      
    >>> A, B = [4], [8]
    >>> C = sort_merge(A, B)
    >>> C
    [4, 8]
    >>> P, Q = [4, 8], [3, 7]
    >>> R = sort_merge(P, Q)
    >>> R
    [3, 4, 7, 8]
    """

    if len(x) == 1 and len(y) == 1: # handling single element
        c = [0, 0]
        if x < y:
            c[0] = x[0]
            c[1] = y[0]
        elif y < x:
            c[0] = y[0]
            c[1] = x[0]
    else:
        n_xy = len(x) + len(y)
        c = [0] * n_xy
        i, j = 0, 0
        while i < len(x) and j < len(y):
            for k in range(n_xy): # handling of if either left or right whole list is smaller than remaining list
                if i >= len(x):
                    c[k] = y[j]
                    j += 1
                elif j >= len(y):
                    c[k] = x[i]
                    i += 1
                else: # regular sorting
                    if x[i] < y[j]:
                        c[k] = x[i]
                        i += 1
                    elif y[j] < x[i]:
                        c[k] = y[j]
                        j += 1
    return c
    
def merge_sort(lst):
    """
    ------ Pseudocode Steps ------
    Step 1 − if it is only one element in the list it is already sorted, return.
    Step 2 − divide the list recursively into two halves until it can no more be divided.
    Step 3 − merge the smaller lists into new list in sorted order.

    Input: array A of n distinct integers. 
    Output: array with the same integers, sorted from smallest to largest.

    // ignoring base cases 
    C := recursively sort ﬁrst half of A 
    D := recursively sort second half of A 
    return Merge (C,D)

    ------ Doctests ------      
    >>> unsorted_list = [8,4,3,7,87,5,64,6,73]
    >>> sorted_list = merge_sort(unsorted_list)
    >>> sorted_list
    [3, 4, 5, 6, 7, 8, 64, 73, 87]
    """
    n = len(lst) 
    if n == 1:
        return lst
    if n > 1:            
        n_half = int(n/2)        
        A = merge_sort(lst[:n_half])
        B = merge_sort(lst[n_half:])        
        C = merge_and_sort(A, B)        
        return C