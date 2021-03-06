# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution(object):
    def depthSum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        if len(nestedList) == 0:
            return 0

        stack = []
        sumValue = 0

        for n in nestedList:
            stack.append((n, 1))

        while stack:
            curr = stack.pop()
            nextElem = curr[0]
            depth = curr[1]
            if nextElem.isInteger():
                sumValue += nextElem.getInteger() * depth
            else:
                for i in nextElem.getList():
                    stack.append((i, depth + 1))

        return sumValue
