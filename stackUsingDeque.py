import collections as f

class Stack:

    def __init__(self,deque):
        self.actions=deque

    def push(self,a):
        self.actions.append(a)
        print("element added ", self.actions)

#creating dequee collection objecty
stk= f.deque()
#passing deque object to our class object for constructtor
s=Stack(stk)
s.push("murthy")
s.push("vinutha")
s.push("shubhada")





