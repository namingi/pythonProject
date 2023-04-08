from typing import Optional
from typing_extensions import Final
RATE : Final = 300
class Node :
    def __init__(self,data : int, node :Optional["Node"]):
        self.data = data
        self.node = node

node2 = Node(12,None)
node1 = Node(27,node2)
node0 = Node(30,node1)