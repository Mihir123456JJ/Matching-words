def match(words):
    ctr=0
    x=[]
    for i in words:
        if len(i)>1 and i[0]==i[-1]:
            ctr=ctr+1
            x.append(i)
    print("List:",x)
    return ctr
count=match(['cat','rat','mom','pop','1902','wow','8787877'])
print("The count is",count) 
       


