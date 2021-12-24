import collections as f

class Stack:
    def __init__(self):
        self.containers= f.deque()

    def push(self,a):
        for i in range(0,len(a)):
        #for i in range(0,len(a)):
           self.containers.append(a[i])

    def reverse_string(self):
        i=0
        li=[]
        while i < len(self.containers):
            li.append(self.containers.pop())
        return li
s=Stack()
stri="murthy"
print(stri)
s.push("murthy")
rev=''.join(s.reverse_string())
print(rev)