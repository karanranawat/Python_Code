def gem_stones():
    s = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
    t = (int)(raw_input())
    while t>0:
        t = t-1
        q = (set)(raw_input())
        s = s.intersection(q)
    print(len(s))

        
            
