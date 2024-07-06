class RangeNode:
    def __init__(self, left: int, right: int):
        self.left = left
        self.right = right
        self.next = None
        self.prev = None
        self.to_remove = False


    def add(self, root, node, overlaps: bool=False):
	
        # check if I should place the new node before the current one
        if node.right <= self.left and not overlaps:
            if self.prev is None:
                root = node
                self.prev = node
                node.next = self
            else:
                if self.prev.right <= node.left:
                    self.prev.next = node
                    node.next = self
                    self.prev = node
                else:
                    self.prev.add(root, node, False)

		# Overlapping with the current left
        elif node.left < self.right:
            if node.left < self.left:
                self.left = node.left
		
            # Check if it also overlaps with the previous one
            if not self.prev is None:
                self.prev.add(root, node, True)

            if node.right > self.right:
                self.right = node.right
                if not self.next is None:
                    self.next.add(root, node, True)

	
		
		# check if I should place the new node after the current one 
        elif node.left >= self.right  and not overlaps:
            if self.next is None:
                self.next = node
                node.prev = self
            else:
                if self.next.left >= node.right: 
                    self.next.prev = node
                    node.prev = self
                    self.next = node

                self.next.add(root, node, False)
			

		# Overlapping with the current right
        elif node.right > self.left:
            if node.left < self.left:
                self.left = node.left
		        # Check if it also overlaps with the previous one
                if not self.prev is None:
                    self.prev.add(root, node, True)

            if node.right > self.right:
                self.right = node.right
                if not self.next is None:
                    self.next.add(root, node, True)

    def query(self, node) -> bool:
        if node.left >= self.left and node.right <= self.right:
            return True
        elif node.right <= self.right and node.right > self.left:
            if self.prev is None:
                return False
            else:
                return self.prev.query(RangeNode(node.left, self.left))
        elif node.left >= self.left and node.left < self.right:
            if self.next is None:
                return False
            else:
                return self.next.query(RangeNode(self.right-1, node.right))
		
        elif node.right <= self.left:
            if self.prev is None:
                return False
            else:
                return self.prev.query(node)
        elif node.left > self.right:
            if self.next is None:
                return False
            else:
                return self.next.query(node)

    def remove(self, root, node):
        # Exact node
        if node.left == self.left and node.right == self.right:
            self.prev.next = self.next
            self.next.prev = self.prev
	
        # Touching the left
        elif node.left == self.left and node.right <= self.right:
            self.left = node.right
		
        # Touching the right
        elif node.right == self.right and node.left >= self.left:
            self.right = node.left
		

        # in the middle
        elif node.left > self.left and node.right < self.right:
            node1 = RangeNode(self.left, node.left)
            node2 = RangeNode(node.right, self.right)
            node1.prev = self.prev
            node1.next = node2
            node2.prev = node1
            node2.next = self.next

            if self.prev is None:
                root = node1
            else:
                self.prev.next = node1

            if not self.next is None:
                self.next.prev = node2
				
		
        elif node.right <= self.right and node.right > self.left:
            self.left = node.right

            if not self.prev is None:
                self.prev.remove(root, RangeNode(node.left, self.left))

        elif node.left >= self.left and node.left < self.right:
            self.right = node.left
            if not self.next is None:
                self.next.remove(root, RangeNode(self.right-1, node.right))
		
        elif node.right <= self.left:
            if not self.prev is None:
                self.prev.remove(root, node)
        
        elif node.left > self.right:
            if not self.next is None:
                self.next.remove(root, node)
		


class RangeModule:

    def __init__(self):
        self.ranges = None        
	

    def addRange(self, left: int, right: int) -> None:
        if self.ranges is None:
            self.ranges = RangeNode(left, right)
        else:
            self.ranges.add(self.ranges, RangeNode(left, right), False)

    def queryRange(self, left: int, right: int) -> bool:
        if self.ranges is None:
            return False
        else:
            return self.ranges.query(RangeNode(left, right))
        	

    def removeRange(self, left: int, right: int) -> None:
        if not self.ranges is None:
            self.ranges.remove(self.ranges, RangeNode(left, right))


# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)
