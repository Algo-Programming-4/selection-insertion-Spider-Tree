#bubble(list) - > sorted ist
def bubble(item):
    for i in range(len(item)-1):
        skip=True
        for j in range(len(item)-i-1):
            a=item[j]
            b=item[j+1]
            if a>b:
                item[j]=b
                item[j+1]=a
                skip=False
        if (skip):
           break
    return item
#selection(list) -> sorted list
def selection(unsorted):
    for i in range(len(unsorted)-1):
        small = i
        for j in range(i+1, len(unsorted)):
         if unsorted[j] < unsorted[small]:
            small = j
        temp = unsorted[i]
        unsorted[i] = unsorted[small]
        unsorted[small] = temp
    return unsorted
#insertion(list) > sorted list
def insertion(unsorted):
    for i in range(len(unsorted)):
        j=i
        if j>0 and unsorted[j-1]>unsorted[j]:
            unsorted[j-1],unsorted[j]=unsorted[j],unsorted[j-1]
            j=j-1
        
    return unsorted
