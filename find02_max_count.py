def find_max_count(data):
    """
    Given the list of numbers, Find count of maximum numbers in the list
    args:
        data: list of numbers
    returns: count of maximum numbers in the list
    """
    i=0
    n=0
    a=data[0]
    while n<len(data):
        if a<data[n]:
            a=data[n]
        n=n+1
    return data.count(a)
print(find_max_count([1, 8, 3, 8, 5]))