def printNumAlpha(s):
    count = 1
    index = 0
    length = len(s)
    for i in range(length):
        if i == (len(s)-1):
          print('Count of ' + s[i] + ': ' + str(count))
        elif(s[i]==s[i+1]):
            count += 1
        else:
            if count > 1:
                s[index] = s[i]
                s[index+1]= count
                index +=2
                print('s = ' + str(s))
            else:
                s[index] = s[i]
                index +=1
            print('Count of ' + str(s[i]) + ': ' + str(count))
            count = 1
    print(s)
    return s
        
