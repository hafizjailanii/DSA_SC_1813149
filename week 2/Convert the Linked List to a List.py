class node:  
    def __init__(self, data):  
        self.data = data  
        self.next = None
  
def add(data): 
  
    newnode = node(0) 
    newnode.data = data 
    newnode.next = None
    return newnode 
  
def printArr(a, n): 
  
    i = 0
    while(i < n): 
        print (a[i], end = " ") 
        i = i + 1
  
def findlength( head): 
  
    curr = head 
    cnt = 0
    while (curr != None): 
      
        cnt = cnt + 1
        curr = curr.next
      
    return cnt 
  
def convertArr(head): 
  
    len1 = findlength(head) 
  
    arr = [0] 
    curr = head 
  
    while (curr != None):  
        arr.append( curr.data) 
        curr = curr.next
      
    printArr(arr, len1) 
  
head = node(0) 
head = add(1) 
head.next = add(2) 
head.next.next = add(3) 
head.next.next.next = add(4) 
head.next.next.next.next = add(5) 
convertArr(head) 