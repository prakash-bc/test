package main

func isBalanced(root *TreeNode) bool {
	isbal, _ := dfs(root)
	return isbal

}
func dfs(node *TreeNode) (bool, int) {
	if node == nil {
		return true, 0
	}
	leftB, leftH := dfs(node.Left)
	rightB, rightH := dfs(node.Right)

	h := 1 + max(leftH, rightH)
	isbal := leftB && rightB && abs(leftH-rightH) <= 1
	return isbal, h
}

func max(a, b int) int {
	if a < b {
		return b
	}
	return a
}

func abs(a int) int {
	if a < 0 {
		return -a
	}
	return a
}

// class Solution(object):
//     def isBalanced(self, root):
//         """
//         :type root: TreeNode
//         :rtype: bool
//         """
//         def dfs(node):
//             if node is None:
//                 return [True, 0]
//             left = dfs(node.left)
//             right = dfs(node.right)

//             h = 1+max(left[1], right[1])
//             isbal = left[0] and right[0] and abs(left[1]-right[1])<=1
//             return [isbal, h]
//         return dfs(root)[0]
