
from Datastructions.linkedList import LinkedList
from Datastructions.linkedList import Node



def merge_sort(linked_list:LinkedList):
    if linked_list.size()==1 or linked_list.head is None:
        return linked_list
    left_sub_list,right_sub_list=split(linked_list)
    left=merge_sort(left_sub_list)
    right=merge_sort(right_sub_list)
    return merge(left,right)

def split(linked_list:LinkedList):
    if linked_list==None or linked_list.head==None:
        left=linked_list
        right=None 
        return left,right
    else:
        midpoint=linked_list.size()//2
        node_at_midpoint=linked_list.node_at_index(midpoint-1)
        left=linked_list
        right=LinkedList()
        right.head=node_at_midpoint.next_node
        node_at_midpoint.next_node=None
        return left,right 
def merge(left:LinkedList,right:LinkedList):
    #merge left and right
    merged=LinkedList()
    #add a fake head that is discarded later 
    merged.add_node_to_head(10)
    #set current to the head of the linkedlist
    current_node=merged.head
    #obtain head nodes for left and right linked lists
    left_head=left.head 
    right_head=right.head
    #iterate through list
    while left_head or right_head:
        if left_head is None:
            current_node.next_node=right_head



