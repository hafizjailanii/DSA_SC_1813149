class Node:  
    def __init__(self, data):  
        self.data = data  
        self.next = None
          
start = None
  
def isPairWiseSorted(head) : 
  
    flag = True
    temp = head  
  
    while (temp != None and temp.next != None) : 
      
        if (temp.data > temp.next.data) : 
            flag = False
            break
          
        temp = temp.next.next
      
    return flag  

def push(head_ref, new_data) : 
  
    global start 
    new_node = Node(0)  
    new_node.data = new_data  
    new_node.next = head_ref  
    head_ref = new_node  
    start = head_ref 

start = None
  
push(start, 40)  
push(start, 60)  
push(start, 9)  
push(start, 36)  
push(start, 54)  
push(start, 20)  
  
if (isPairWiseSorted(start)) : 
    print("True") 
else: 
    print("False") 
