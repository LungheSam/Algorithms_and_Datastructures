class Node:

    def __init__(self,data,next_node=None):
        self.data=data
        self.next_node=next_node
    def __repr__(self):
        return f"[<Node data:{self.data} ->Next Node:{self.next_node}]"
class LinkedList:
    def __init__(self):
        self.head=None 
        self.tail=None
    def isempty(self):
        return self.head==None
    def size(self):
        current_node=self.head 
        count=0
        while current_node:
            count+=1

            current_node=current_node.next_node
        return count
    def insert_node(self,data,index):
        if index==0:
            LinkedList.add_node_to_head(data)
        elif index==LinkedList.size(self):
            LinkedList.add_node_to_tail(self,data)
        elif index>0:
            new_node=Node(data)
            position=0
            current_node=self.head 
            previous_node=self.head
            while position<index:
                previous_node=current_node
                current_node=current_node.next_node
                position+=1
            new_node.next_node=current_node
            previous_node.next_node=new_node
    def remove_node(self,index):
        if LinkedList.isempty(self):
            print("Cannot Remove a node on an empty list")
            return None
        elif index>LinkedList.size(self):
            print("Index Out Of Bound Range")
            return None
        elif LinkedList.size(self)==1:
            self.head=None
            return None
        else:
            position=0
            current_node=self.head
            previous_node=self.head 
            while position <=index:
                if position==index:
                    previous_node.next_node=current_node.next_node
                previous_node=current_node
                current_node=current_node.next_node
                position+=1
            return None

    def add_node_to_head(self,data):
        # new_node=Node(data)
        # new_node.next_node=self.head 
        # self.head=new_node
        new_node=Node(data)
        if LinkedList.isempty(self):
            self.head=new_node
            self.tail=self.head
        else:
            new_node.next_node=self.head 
            self.head=new_node
    def add_node_to_tail(self,data):
        # LinkedList.insert_node(self,data=data,index=LinkedList.size(self))
        new_node=Node(data)
        if LinkedList.isempty(self):
            self.tail=new_node
            self.head=self.tail 
        elif LinkedList.size(self)==1:
            self.tail=self.head
            self.tail.next_node=new_node
            self.tail=new_node
        else:
            self.tail.next_node=new_node
            self.tail=new_node

    def search(self,data):
        current_node=self.head 
        while current_node.next_node!=None:
            if current_node.data==data:
                return data 
            else:
                current_node=current_node.next_node
        return None
    def node_at_index(self,index):
        if index==0:
            return self.head
        else:
            count=0
            current_node=self.head
            while count<index:
                current_node=current_node.next_node
                count+=1
            return current_node
    def __repr__(self):
        current_node=self.head 
        nodes=[]
        while current_node:
            if current_node==self.head:
                nodes.append(f"Head:[{current_node.data}]")
            elif current_node.next_node==None:
                nodes.append(f"Tail:[{current_node.data}]")
            else:
                nodes.append(f"[{current_node.data}]")
            current_node=current_node.next_node
        return "->".join(nodes)
    
            

    
# N1=Node(10)
# print(N1)
# N2=Node(20)
# N1.next_node=N2
# print(N1)
my_linked_list=LinkedList()
my_linked_list.add_node_to_tail(111)
print(f"Tail={my_linked_list.tail}")
print(f"Size={my_linked_list.size()}")
print(my_linked_list)
my_linked_list.add_node_to_head(40)
my_linked_list.add_node_to_head(70)
my_linked_list.add_node_to_head(33)
my_linked_list.add_node_to_head(87)
print(my_linked_list)
result_search=my_linked_list.search(336)
print(result_search)
my_linked_list.insert_node(88,my_linked_list.size())
print(my_linked_list)
my_linked_list.add_node_to_tail(91)
my_linked_list.add_node_to_tail(15)
print(my_linked_list)
my_linked_list.remove_node(2)
print(my_linked_list)
