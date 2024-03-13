class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        self.result = 0
        self.deepest = 1
        self.dfs(root, 1)
        return self.result
    def dfs(self, root, curr_depth):
        if root == None:
            return
        self.dfs(root.left, curr_depth + 1)
        self.dfs(root.right, curr_depth + 1)
        if curr_depth == self.deepest:
            self.result += root.val
        elif curr_depth > self.deepest:
            self.result = root.val
            self.deepest = curr_depth