class node:
    def __init__(self,value):
        self.value=value
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None
        self.tail=None
        self.len=0
    def __str__(self):
        temp=self.head
        result=''
        while temp is not None:
            result+=str(temp.value)
            temp=temp.next
            if temp is not None:
                result+=' -> '    
        return result
    def append(self,value):
        newnode=node(value)
        if self.head is None:
            self.head=newnode
            self.tail=newnode
        else:
            self.tail.next=newnode
            self.tail=newnode
        self.len+=1
    def prepend(self,value):
        newnode=node(value)
        if self.head is None:
            self.head=newnode
            self.tail=newnode
        else:
            newnode.next=self.head
            self.head=newnode
        self.len+=1
    def insert(self,value,index):
        newnode=node(value)
        if len==0:
            self.head=value
            self.tail=value
        elif index==0:
            newnode.next=self.head
            self.head=newnode
        
        else:
            tempnode=self.head
            for _ in range(index-1):
                tempnode=tempnode.next
            newnode.next=tempnode.next
            tempnode.next=newnode
        self.len+=1



start=Linkedlist()
while(1):
    print('\t\t\t\t\tWELCOME TO LINKED LIST')
    print(' 1.append \n 2.insert \n 3.prepend \n 4.length ')
    c=int(input("enter you choice:"))

    if c==1:
        n=int(input('enter a number to append:'))
        start.append(n)
        print(start)
    elif c==2:
        n=int(input('enter a number to insert:'))
        i=int(input('enter postion to insert:'))
        start.insert(n,i)
        print(start) 
    elif c==3:
        n=int(input('enter a number to prepend:'))
        start.prepend(n)
        print(start)
    elif c==4:
        print(start.len)
    else:
        print('PROGRAM EXITS')
        break       
