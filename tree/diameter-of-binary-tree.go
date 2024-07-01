/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

var maxD int

func diameterOfBinaryTree(root *TreeNode) int {
	maxD = 0
	findh(root)
	return maxD

}
func findh(root *TreeNode) int {
	if root == nil {
		return -1
	}
	leftH := findh(root.Left)
	rightH := findh(root.Right)
	maxD = max(maxD, 2+leftH+rightH)
	return 1 + max(leftH, rightH)

}

func max(x int, y int) int {
	if x > y {
		return x
	}
	return y
}

// class Solution(object):
//     def diameterOfBinaryTree(self, root):
//         res = [0]
//         def dfsheight(root):
//             if not root:
//                 return -1
//             leftH = dfsheight(root.left)
//             rightH = dfsheight(root.right)

//             res[0] = max(res[0], 2+leftH+rightH)

//             return 1+max(leftH,rightH)
//         dfsheight(root)
//         return res[0]

            
        