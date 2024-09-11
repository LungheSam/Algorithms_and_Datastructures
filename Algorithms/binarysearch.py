
def binarysearch(array,target):
    first=0
    last=len(array)
    while first<=last:
        midpoint=(last-first)//2
        if array[midpoint]==target:
            return midpoint
        else:
            if array[midpoint]>target:
                last=midpoint-1
            else:
                first=midpoint+1
    return None

def verify(index):
    if index is not None:
        print(f"Target was found at index:{index}")
    else:
        print(f"Target was not found anywhere in the given array")
my_array=[6,7,8,9,10,11,12,14,18,20]
target=8
result_index=binarysearch(my_array,target)
verify(result_index)