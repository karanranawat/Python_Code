def dedup(array):
    dict1 = {}

    for i in range(len(array)):
        if array[i] not in dict1:
            dict1[array[i]] = 1
        else:
            dict1[array[i]] += 1

    print dict1

    for i in range(len(array)):
        
        if dict1[array[i]] > 1:
            print array[i],
            dict1[array[i]] = 0
        
        if dict1[array[i]] == 1:
            print array[i],

if __name__ == '__main__':
    alist = [1,1,2,4,5]
    dedup(alist)

    alist = [1,1,1,1,1,1,2,4,5]
    dedup(alist)

    alist = [1,1,2,4,5,5,5,5,5,1]
    dedup(alist)

    alist = [1,1,1,1,1,1,1]
    dedup(alist)
