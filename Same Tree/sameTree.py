#Given by leetCode

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: #means if p and q are empty
            return True
        if not p or not q or p.val != q.val: # here it means if p or q one of them
            return False
        return(self.isSameTree(p.left, q.left)and #here the value of p,q left and right are the same or not 
        self.isSameTree(p.right, q.right))