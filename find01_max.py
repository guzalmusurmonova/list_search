def find_max(data):
    """
    Given the list of numbers, return the maximum number in the list
    args:
        data: list of numbers
    returns: maximum number in the list
    """ 
    i=0
    n=0
    a=data[0]
    while n<len(data):
        if a<data[n]:
            a=data[n]
        n=n+1
    return a
print(find_max([1, 2, 3, 4, 5]))
    