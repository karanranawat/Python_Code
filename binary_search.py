def search(l,e, low, high):
    ''' input : l - list of sorted elements
                e - element to be search

        output : True - if element is found
                 False - if element is not found
    '''
    global count
    count = count + 1
    print('Iteration No. :' + str(count))
    print('Low :' + str(low))
    print('High :' + str(high))
    if low==high:
        return l[low]==e
    else:
        mid = low + (int)((high-low)/2)
        if l[mid]==e:
            return True
        elif l[mid]>e:
            return search(l,e,low,mid-1)
        else:
            return search(l,e,mid+1,high)

def bs(l,e):
    global count
    count = 0
    if len(l)==0:
        return False
    else:
        return search(l,e,0,len(l)-1)

# Some more changes -----
