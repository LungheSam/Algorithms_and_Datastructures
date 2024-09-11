
def linearsearch(array,target):
    for i in range(len(array)):
        if array[i]==target:
            return i
    return None 
def verify(index):
    if index != None:
        print(f"Target was found at index:{index}")
    else:
        print(f"Target was not found anywhere in the given array")

my_array=[9,7,882,5,3,5]
target=5
result_index=linearsearch(my_array,target)
verify(result_index)