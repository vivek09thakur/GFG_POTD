class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Solution:
    def sort(self, h1):
        #return head
        if h1.next == None:
            return h1
        
        else:
            # break linked list in two parts
            head1 = h1
            head2 = h1.next
            
            # fill them
            ptr1 = h1
            ptr2 = head2
            temp1 = head1
            temp2 = head2
            while(temp1 != None and temp2!= None):
                temp1 = temp2.next
                if temp1 == None:
                    break
                
                temp2 = temp1.next
                ptr1.next = temp1
                ptr2.next = temp2
                
                ptr1 = temp1
                ptr2 = temp2
                
            
            ptr1.next = None
            if ptr2:
                ptr2.next = None
            
            # now reverse the head 2 linked list
            t1 = None
            t2 = head2
            t3 = head2.next
            while(t3!= None):
                t2.next = t1
                t1 = t2
                t2 = t3
                t3 = t3.next
            
            t2.next = t1
            head2 = t2
            
            ptr1.next = head2
            return head1
        return None
