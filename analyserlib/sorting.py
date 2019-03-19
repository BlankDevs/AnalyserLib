def bubble_sort(items):

    '''
    Return array of items, sorted in ascending order

    Args:
        items (array): array of integers to be sorted
    
    Returns:
        array (int): sorted array of integers
    
    Examples:
        >>> bubble_sort([1,3,2])
        [1,2,3]        
        >>> bubble_sort([3,1,7,5])
        [1,3,5,7]
        >>> bubble_sort([12,7,3,0])
        [0,3,7,12]
    '''
    
    n = len(items)
    # nested for-loops in specified range(s)
    for i in range(n):
        for k in range(0, n-i-1):
            if items[k] > items[k+1]:
                items[k], items[k+1] = items[k+1], items[k]
    return items



def merge_sort(items):

    '''
    Return array of items, sorted in ascending order

    Args:
        items (array): array of integers to be sorted
    
    Returns:
        array (int): sorted array of integers
    
    Examples:
        >>> merge_sort([1,3,2])
        [1,2,3]        
        >>> merge_sort([3,1,7,5])
        [1,3,5,7]
        >>> merge_sort([12,7,3,0])
        [0,3,7,12]
    '''
    
    if len(items) > 1:
    	# we split the array in halve
        middle = len(items)//2
        left = items[:middle]
        right = items[middle:]
        
        merge_sort(left)
        merge_sort(right)
        
        i=0
        j=0
        k=0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                items[k] = left[i]
                i += 1
            else:
                items[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            items[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            items[k] = right[j]
            j += 1
            k += 1
    return items



def quick_sort(items):

    '''
    Return array of items, sorted in ascending order

    Args:
        items (array): array of integers to be sorted
    
    Returns:
        array (int): sorted array of integers
    
    Examples:
        >>> quick_sort([1,3,2])
        [1,2,3]        
        >>> quick_sort([3,1,7,5])
        [1,3,5,7]
        >>> quick_sort([12,7,3,0])
        [0,3,7,12]
    '''

    if len(items) == 2:
        if items[0] > items[1]:
            return [items[1], items[0]]
        else:
            return items
    else:
        piv = items[0]
        left = []
        right = []
        mid = []
        
        for i in range(len(items)):
            if items[i] == piv:
                mid.append(items[i])
            elif items[i] < piv:
                left.append(items[i])
            else:
                right.append(items[i])
        if len(left) > 1:
            left = quick_sort(left)
        if len(right) > 1:
            right = quick_sort(right)

        # assign sorted parts to a single list    
        new = left + mid + right
        # return 'new' - the single list
        return new
