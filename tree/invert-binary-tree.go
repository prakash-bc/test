/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func invertTree(root *TreeNode) *TreeNode {
	if root == nil {
		return root
	}
	root.Left, root.Right = root.Right, root.Left
	invertTree(root.Left)
	invertTree(root.Right)
	return root

}

// class Solution(object):
//     def invertTree(self, root):
//         """
//         :type root: TreeNode
//         :rtype: TreeNode
//         """
//         if root is None:
//             return root
//         root.left, root.right = root.right, root.left
//         self.invertTree(root.left)
//         self.invertTree(root.right)
//         return root

        