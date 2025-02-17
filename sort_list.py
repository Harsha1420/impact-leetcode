class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def sortList(head):
    if not head or not head.next:
        return head 

    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    mid = slow.next
    slow.next = None
    left = sortList(head)
    right = sortList(mid)
    return merge(left, right)

def merge(l1, l2):
    dummy = ListNode()
    tail = dummy

    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    tail.next = l1 if l1 else l2 

    return dummy.next

# Example Usage:
def printList(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

head = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))
sorted_head = sortList(head)
printList(sorted_head) 