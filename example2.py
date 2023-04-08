from typing import Optional, Generic, TypeVar,Tuple,Dict,List

T = TypeVar("T")

class Node(Generic[T]) :
    def __init__(self,data : T,next : Optional["Node"]=None):
        self.data = data
        self.next = next

class LinkedList(Generic[T]) :
    def __init__(self):
        self.head : Optional[Node[T]] = Node(None)
        self.count : int = 0
    def add(self,node : Node[T]) :
        if self.head.data == None :
            self.head = node
            self.count += 1
        else :
            cur = self.head
            while cur.next != None :
                cur = cur.next
                self.count += 1
            cur.next = node

    def insert(self,idx : int,node : Node[T] ):
        prev = None
        cur = self.head
        for i in range(self.count) :
            cur = self.head
            if idx == 0 and i == 0 :
                self.head = node
                cur = cur.next
                self.count += 1
                break
            elif idx == i :
                prev.next = node
                node.next = cur
                self.count += 1
                break
            else :
                prev = cur
                cur = cur.next

    def toArray(self) -> list:
        array = []
        cur = self.head
        for i in range(self.count) :
            array.append(cur)
            cur = cur.next
        return array

    def isEmpty(self) -> bool:
        if self.head.data == None :
            return True
        else :
            return False

    def getFrequencyOf(self,Entry : T )->int:
        frequency:int = 0
        cur = self.head
        for i in range(self.count) :
            if cur.data == Entry :
                frequency += 1
            cur = cur.next
        return frequency

    def contains(self,Entry : T)->bool:
        found : bool = False
        cur = self.head
        for i in range(self.count) :
            if cur.data == Entry :
                found = True
                break
            else :
                cur = cur.next
        return found

    def pop(self) -> T :
        result : T = None
        if self.head.data !=None :
            result = self.head.data
            self.head = self.head.next
            self.count -= 1
        return result

    def remove(self,Entry : T) :
        prev = None
        cur = self.head
        if self.head.data != None :
            for i in range(self.count) :
                if cur.data == Entry and i == 0  :
                    cur = cur.next
                    self.count -=1
                    break
                elif cur.data == Entry and i > 0  :
                    cur = cur.next
                else :
                    prev = cur
                    cur = cur.next

    def clear(self):
        self.head = None







