def find_average(alist):
    delMax = alist.index(max(alist)) #or remMax=max(alist)
    del alist[delMax]                #   alist.remove(remMax)
    delMin=alist.index(min(alist))   #   remMin=min(alist)
    del alist[delMin]                #   alist.remove(remMin)
    list_average = sum(alist)/len(alist)
    return list_average
