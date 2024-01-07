class Solution:
    def mergeResult(self, h1, h2):
        #return head of merged list
        dummy = Node(0)
        while h1 and h2:
            if h1.data < h2.data:
                n = h1
                h1 = h1.next
            else:
                n = h2
                h2 = h2.next
            n.next = dummy.next
            dummy.next = n
        h = h1 or h2
        while h:
            n = h
            h = h.next
            n.next = dummy.next
            dummy.next = n
        return dummy.next
