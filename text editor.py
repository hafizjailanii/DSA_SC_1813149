#group 6
#text editor

# Create the Node class
class Node:
   def __init__(self, data):
      self.data = data
      self.next = None
      self.prev = None

# Create the doubly linked list
class doubly_linked_list:

   def __init__(self):
      self.head = None

# Define the append method to add elements at the end
   def append(self, NewVal):

      NewNode = Node(NewVal)
      NewNode.next = None
      if self.head is None:
         NewNode.prev = None
         self.head = NewNode
         return
      last = self.head
      while (last.next is not None): 
         last = last.next
      last.next = NewNode
      NewNode.prev = last
      return

# Define the method to print the linked list 
   def listprint(self, node):
      while (node is not None):
         print(node.data),
         node = node.next


characterList = doubly_linked_list()
val = input("Text Editor:\n") + input("")

while input() != '':
    val += input('')

for element in val:
    characterList.append(element)

characterList.listprint(characterList.head)