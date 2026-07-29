class ListNode:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node
class LinkedList:
    
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        cnt=0
        curr = self.head.next
        while(curr):
            if(cnt == index):
                return curr.val
            cnt+=1
            curr = curr.next
        return -1

    def insertHead(self, val: int) -> None:
        newNode =ListNode(val)
        newNode.next = self.head.next
        self.head.next = newNode
        if not newNode.next:
            self.tail = newNode

    def insertTail(self, val: int) -> None:
        self.tail.next = ListNode(val)
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        curr = self.head
        cnt=0
        while(cnt != index and curr):
            cnt +=1
            curr = curr.next
        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True
        return False

    def getValues(self) -> List[int]:
       list = []
       curr = self.head.next
       while(curr):
        list.append(curr.val)
        curr = curr.next
       return list

