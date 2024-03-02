
class LinkedList :
    def __init__(self, val, next=None) -> None:
        self.val = val
        self.next = next

ll = LinkedList(1, LinkedList(2, LinkedList(3)))

def show(ll : LinkedList, to) -> list :
    if ll :
        to.append(ll.val)
        if ll.next :
            show(ll.next, to)
        return to
    return []

def toLinked(dl : list) :
    if len(dl) :
        return LinkedList(dl[0], toLinked(dl[1:]))

print(show(toLinked(show(ll, [])), [])) # работать
