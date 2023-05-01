def find_max_index(data):
    """
    Given the list of numbers, return the index of maximum number in the list
    args:
        data: list of numbers
    returns: index of maximum number in the list
    """  
    i=0
    n=0
    a=data[0]
    while n<len(data):
        if a<data[n]:
            a=data[n]
        n=n+1
    return data.index(a)
print(find_max_index( [1, 2, 3, 4, 5]))
    
