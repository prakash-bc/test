package main

import (
	"fmt"
)

type Tree struct {
	root *Node
}
type Node struct {
	// key   int
	value int
	left  *Node
	right *Node
}

func (t *Tree) insert(val int) *Tree {
	if t.root == nil {
		t.root = &Node{value: val}
	} else {
		t.root.insert(val)

	}
	return t
}

func (t *Node) insert(val int) {
	if val < t.value {
		if t.left == nil {
			t.left = &Node{value: val}
		} else {
			t.left.insert(val)
		}
	} else {
		if t.right == nil {
			t.right = &Node{value: val}
			return
		} else {
			t.right.insert(val)

		}
	}
}

func (t *Node) exists(val int) bool {
	if t == nil {
		return false
	}
	if val == t.value {
		return true
	}
	if val < t.value {
		t.left.exists(val)
	}
	if val > t.value {
		t.right.exists(val)
	}
	return false
}

func printNode(n *Node) {
	if n == nil {
		return

	}
	fmt.Println(n.value)
	printNode(n.left)
	printNode(n.right)
}

func main() {
	t := &Tree{}
	t.insert(10).
		insert(8).
		insert(20).
		insert(9).
		insert(0).
		insert(15).
		insert(25)
	printNode(t.root)
	println(t.root.exists(26))

}
