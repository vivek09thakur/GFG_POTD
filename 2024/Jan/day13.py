class Solution:
    def insertionSort(self, head):
        #code here
        if not head or not head.next:
            return head
            
        sorted_head=None
        while head:
            curr=head
            head=head.next
            curr.next=None
            
            if not sorted_head or curr.data<sorted_head.data:
                curr.next=sorted_head
                sorted_head=curr
            else:
                temp = sorted_head
                while temp.next and temp.next.data < curr.data:
                    temp = temp.next
                curr.next = temp.next
                temp.next = curr
        return sorted_head
