
def mergesort(array):
    if len(array) <=1:
        return array
    left_subarray,right_subarray=split(array)
    left=mergesort(left_subarray)
    right=mergesort(right_subarray)
    return merge(left,right)

def split(array):
    midpoint=len(array)//2
    left=array[:midpoint]
    right=array[midpoint:]
    return left,right
def merge(left,right):
    i=0
    j=0
    l=[]
    while (i<len(left)) and (j<len(right)):
        if left[i]<right[j]:
            l.append(left[i])
            i+=1
        else:
            l.append(right[j])
            j+=1
    while i<len(left):
        l.append(left[i])
        i+=1
    while j<len(right):
        l.append(right[j])
        j+=1
    return l

def verify(array):
    n=len(array)
    if n==0 or n==1:
        return True 
    return array[0]<array[1] and verify(array[1:])
my_array=[89,3,45,1,90,12,22,79]
sorted_array=mergesort(my_array)
print(verify(sorted_array))


    