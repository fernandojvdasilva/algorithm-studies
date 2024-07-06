class RangeModule:

    def __init__(self):
        self.values = set()        	

    def addRange(self, left: int, right: int) -> None:
        for i in range(left, right):
            self.values.add(i)

    def queryRange(self, left: int, right: int) -> bool:
        check = True
        for i in range(left, right):
            if not i in self.values:
                check = False
                break

        return check 

    def removeRange(self, left: int, right: int) -> None:
    	for i in range(left, right):
            if i in self.values:
                self.values.remove(i)

   


# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)