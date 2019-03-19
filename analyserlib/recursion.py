def sum_array(array):

    '''
    Return sum of all items in array
    
    Args:
        array (int): array of integers to sum
    Returns:
        sum of given array

    Examples:
        >>> sum_array([1, 2, 3])
        6
        >>> sum_array([1, 4, 0, -1])
        4
        >>> sum_array([1])
        1
    '''
    
    # if length of array is 1 return that single element
    if len(array) == 1:
        return array[0]
    # else take first element and add it to the others
    else:
        return array[0] + sum_array(array[1:])



def fibonacci(n):

    '''
    Return nth term in fibonacci sequence
    
    Args:
        n (int): nth term in fibonacci sequence to calculate
    
    Returns:
        int: nth term of fibonacci sequence,
             equal to sum of previous two terms
    
    Examples:
        >>> fibonacci(1)
        1        
        >>> fibonacci(2)
        1
        >>> fibonacci(3)
        2
    '''
    
    if n <= 1:
        return n

    else:
        return fibonacci(n - 1) + fibonacci(n - 2)



def factorial(n):

    '''
    Return n!

    Args:
        n (int): nth term for which factorial must be calculated
    
    Returns:
        int: factorial of nth term
    
    Examples:
        >>> factorial(3)
        6        
        >>> fibonacci(5)
        120
        >>> fibonacci(9)
        362880    
    '''
    
    return 1 if (n == 1 or n == 0) else n * factorial(n-1)



def reverse(word):

    '''
    Return word in reverse

    Args:
        word (string): string which must be reversed
    
    Returns:
        string: reversed string
    
    Examples:
        >>> reverse('hello')
        olleh        
        >>> reverse('first')
        tsrif
        >>> reverse('live')
        evil
    '''
    if len(word) == 0:
        return word
    else:
        return reverse(word[1:]) + word[0]


