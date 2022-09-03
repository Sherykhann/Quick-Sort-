# Define a function which take as an input the unsorted sequence
def qsort(sequence):
    length=len(sequence)
    if length<=1:
        return sequence
    else:
        pivot=sequence.pop()
    begin_id=0
    end_index=length-1 
    greater_list=[]
    lesser_list=[]
    
    print(f'The end index is {end_index}')
    
    #pivot=sequence[end_index]
    print(f'The pivot point is {pivot}')
    
    for k in sequence:
        if(k < pivot):
            greater_list.append(k)
        else:
            lesser_list.append(k)
    return qsort(greater_list) + [pivot] + qsort(lesser_list)

print(qsort([100,1,1000]))  
