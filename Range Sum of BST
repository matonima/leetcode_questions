
""""@author: toni"""

import math
class Node:
    def __init__(self,X):
        self.root=X
        self.parent=None
        self.leftchild=None
        self.rightchild=None

        
class binary_search_tree(): 
    def __init__(self,X1,k1,k2):
        self.root=None
            
    def treeassign(self,X1):
        if self.root==None:
            self.root=Node(X1)
        elif self.root>X1 and self.root.leftchild==None:
            self.root.leftchild=Node(X1)
            self.root.leftchild.parent=self.root
        elif self.root<X1 and self.root.rightchild==None:
            self.root.rightchild=Node(X1)
            self.root.rightchild.parent=self.root
        return (self)

    def checkval(self,k1,k2):#checking value of node between limit 1 and 2 (k1,k2)
        x=self
        if x==k1 or x==k2:#if val is = limit
            y=1
        elif x<k2 and x>k1:
            y=1
        else:
            y=0
        return(y)
def treecheck(myinput,l1,l2):
    w=[]
    w1=[]
    n=len(myinput)    
    for i in range(n):        
        x=binary_search_tree(myinput[0],l1,l2)
        x1=((binary_search_tree.treeassign(x, myinput[i])))       
        x2=binary_search_tree.checkval(myinput[i],l1,l2)
        if x2>0:
            w=(x1.root.root) #this gives the value of current node
            w1.append(w)
            print(w)     
    y=sum(w1)
    return(y)
#drivecode
myinput1 = [4,5,6,7,8,9,10,20,14,35,67,24]
limit1=1
limit2=15
y=(treecheck(myinput1,limit1,limit2))
print(y) #prints sum of all the numbers in that are within limit
