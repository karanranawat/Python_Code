def maxSubString(s):
    ans = s[0]
    mainCntr = 0
    while mainCntr < len(s):        
        if mainCntr == len(s)-1:
            break
        subCntr = mainCntr        
        while s[subCntr+1] >= s[subCntr]:
            subCntr +=1            
            if(subCntr == len(s)-1):
                break
        if(len(ans)<=(subCntr-mainCntr)):
            ans = s[mainCntr:subCntr+1]
        mainCntr +=1        
    return str(ans)
            
s = 'azcbobobegghakl'
maxSubString(s)
