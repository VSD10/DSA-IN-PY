class Node:
    def __init__(self,val):
        self.value=val
        self.next=None
        self.prev=None

class DLL:
    def __init__(self):
        self.head=None
        self.tail=None
    def __iter__(self):
        t=self.head
        while t:
            yield t
            t=t.next

    def create(self,val):
        new=Node(val)
        new.next=None
        new.prev=None
        self.head=new
        self.tail=new
    def inatbig(self,val):
        nn=Node(val)
        if self.head is None:
            return "first create a linked list to insert"
        else:
            nn.next=self.head
            self.head.prev=nn
            self.head=nn
    def inatend(self,val):
        nn=Node(val)
        if self.head is None:
            return "first create a linked list to insert"
        else:
            nn.prev=self.tail
            self.tail.next=nn
            self.tail=nn
    def inatloc(self,val,loc):
        nn=Node(val)
        s=self.length()
        if self.head is None:
            return "first create a linked list to insert"
        elif loc==0:
            self.inatbig(val)
        elif loc==s:
            self.inatend(val)
        else:
            tem=self.head
            for _ in range(loc-1):
                tem=tem.next
            nn.next=tem.next
            nn.prev=tem
            
            tem.next.prev=nn
            tem.next=nn
    def reverse(self):
        t=self.tail
        a=[]
        while t:
            a.append(t.value)
            t=t.prev
        print(a)

    def length(self):
        t=self.head
        a=[]
        len=0
        while t:
            len+=1
            a.append(t.value)
            t=t.next
        return len
    def traverse(self):
        t=self.head
        a=[]
        while t:
            a.append(t.value)
            t=t.next
        print(a)
    def delete(self,pos):
        if pos==0:
            self.head=self.head.next
            self.head.prev=None
        elif pos==self.length():
            self.tail=self.tail.prev
            self.tail.next=None
        else:
            t=self.head
            for _ in range(pos-1):
                t=t.next
            t.next=t.next.next
            t.next.next.prev=t
            
        self.traverse()




ll=DLL()
ll.create(3)
ll.inatbig(1)
ll.inatbig(3)
ll.inatend(1)
ll.inatloc(1000,0)
ll.inatloc(23,2)
ll.inatloc(60,5)

print("before reversing:")
print([n.value for n in ll])
print("after reversing:")
ll.reverse() 
a=ll.length()   
print(f'lenght of the linkedlist::         {a}') 
print("after deletion") 
ll.delete(0)
ll.delete(6)
ll.delete(2)
