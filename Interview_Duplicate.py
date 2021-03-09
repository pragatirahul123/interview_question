def duplicate(array):
    i=0
    new=[]
    while i<len(array):
        j=i+1
        while j<len(array):
            a=array[i]==array[j]
            new.append(a)
            j=j+1
            i=i+1
            return(a)
print(duplicate([1,2,3,4,5]))
print(duplicate([1,1,3,4,5]))
print(duplicate([1,1,2,2,3,3,4,4,5]))
              
################################################################################################################################################################

def duplicate_num(array):
    a=set(array)    
    return len(array) !=len(a)     
print(duplicate_num([1,2,3,4,5]))
print(duplicate_num([1,2,3,4, 4]))
print(duplicate_num([1,1,2,2,3,3,4,4,5]))

    
