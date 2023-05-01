def find_max_min_sum(data):
    """
    Given the list of numbers, return the sum of the maximum and minimum numbers in the list
    args:
        data: list of numbers
    returns: sum of the maximum and minimum numbers in the list
    """ 
    i=0
    n=0
    a=data[0]
    while n<len(data):
        if a<data[n]:
            a=data[n]
        n=n+1 
    x=0
    y=0
    b=data[0]
    while n<len(data):
        if b>data[n]:
            b=data[n]
        y=y+1
    return a+b 
print(find_max_min_sum([1, 2, 3, 4, 5]))
