package main

import "math"

// class Solution(object):
//     def isValidBST(self, root):
//         """
//         :type root: TreeNode
//         :rtype: bool
//         """
//         def helper(node, leftVal, rightVal):
//             if not node:
//                 return True
//             if not (leftVal< node.val<rightVal):
//                 return False
//             return helper(node.left, leftVal, node.val) and helper(node.right, node.val, rightVal)
//         return helper(root, -sys.maxsize,  sys.maxsize)

func isValidBST(root *TreeNode) bool {
	return valid(root, math.MinInt, math.MaxInt)

}
func valid(node *TreeNode, leftVal, rightVal int) bool {
	if node == nil {
		return true
	}
	if !((leftVal < node.Val) && (node.Val < rightVal)) {
		return false
	}
	return valid(node.Left, leftVal, node.Val) && valid(node.Right, node.Val, rightVal)

}
