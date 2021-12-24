
import ctypes

class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.nextNode=None



class LinkedList:
    def __init__(self):
        self.head= None

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next

    def insert_at_begining(self,data):
        n = Node(data,self.head)
        self.head=n
        print(self.head.data,self.head.nextNode)

    def insert_at(self, index, data):
       if index < 0 or index > self.get_length():
          raise Exception("Invalid Index")
       if index == 0:
          self.insert_at_begining(data)
          return

       count = 0
       itr = self.head
       while itr:
         if count == index - 1:
           node = Node(data, itr.next)
           itr.next = node
           break

         itr = itr.next
         count += 1

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)



l=LinkedList()
l.insert_at(0,2)
l.insert_at(2,4)
l.insert_at(1,4)
'''
n=Node(5)
n1=Node(6)
n2=Node(7)

n.nextNode=n1
n1.nextNode=n2


print(n.data,n.nextNode)
print(n1.data,n1.nextNode)
print(n2.data,n2.nextNode)

'''