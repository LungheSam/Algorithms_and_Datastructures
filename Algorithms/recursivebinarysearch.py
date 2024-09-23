
def recusrsivebinarysearch(array,target):
    if len(array)==0:
        return False
    else:  
        midpoint=len(array)//2
        if array[midpoint]==target:
            return True
        elif array[midpoint]>target:
                return recusrsivebinarysearch(array[:midpoint],target)
        elif array[midpoint]<target:
                return recusrsivebinarysearch(array[midpoint:],target)

        

def verify(index):
    if index is not False:
         print(f"Element found successfully")
    else:
         print("Element not found inside the array")

my_array=[12,15,18,19,29,30,32,38]
target=19
result=recusrsivebinarysearch(my_array,target)
verify(result)

