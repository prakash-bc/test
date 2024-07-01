package main

import "fmt"

type Node struct {
	val  int
	Next *Node
}

func NewNode(val int, Next *Node) *Node {
	return &Node{
		val:  val,
		Next: Next,
	}
}

type LinkList struct {
	head *Node
}

func NewLinkList() LinkList {
	head := NewNode(-1, nil)
	return LinkList{head: head}

}

func (this *LinkList) Append(val int) {
	n := NewNode(val, nil)
	if this.head == nil {
		this.head = n
		return
	}
	curr := this.head
	for curr.Next != nil {
		curr = curr.Next
	}
	curr.Next = n
}

func printList(head *Node) {
	curr := head
	for curr != nil {
		fmt.Printf("%d ", curr.val)
		curr = curr.Next
	}
	fmt.Println()
}

func partition(head *Node, x int) *Node {
	less_head, bigger_head := NewNode(-1, nil), NewNode(-1, nil)
	less_prev, bibigger_prev := less_head, bigger_head
	for head != nil {
		if head.val < x {
			less_prev.Next = head
			less_prev = less_prev.Next
		} else {
			bibigger_prev.Next = head
			bibigger_prev = bibigger_prev.Next
		}
		head = head.Next
	}
	less_prev.Next, bibigger_prev.Next = nil, nil
	less_prev.Next = bigger_head.Next
	return less_head.Next

}

// func mergeTwoLists(list1 *Node, list2 *Node) *Node {

// 	result := &Node{}
// 	current := result

// 	for list1 != nil && list2 != nil {
// 		if list1.val < list2.val {
// 			current.Next = list1
// 			list1 = list1.Next
// 		} else {
// 			current.Next = list2
// 			list2 = list2.Next
// 		}
// 		current = current.Next

// 	}
// 	if list1 != nil {
// 		current.Next = list1
// 	}
// 	if list2 != nil {
// 		current.Next = list2
// 	}

// 	return result.Next

// }

// func reorderList(head *Node) {
// 	slow, fast := head, head.Next
// 	for fast != nil && fast.Next != nil {
// 		slow = slow.Next
// 		fast = fast.Next.Next

// 	}
// 	var prev *Node
// 	curr := slow.Next //4
// 	for curr != nil {
// 		next := curr.Next // 5
// 		curr.Next = prev
// 		prev = curr
// 		curr = next
// 	}
// 	slow.Next = nil
// 	temp1, second := head, prev
// 	for second != nil {
// 		tmp1, tmp2 := first.Next, second.Next
// 		first.Next = second
// 		second.Next = tmp1
// 		first, second = tmp1, tmp2
// 	}
// 	printList(head)

// }

// func removeNthFromEnd(head *Node, n int) *Node {

// 	if head == nil {
// 		return head
// 	}
// 	slow, fast := head, head
// 	for n > 0 {
// 		fast = fast.Next
// 		n -= 1

// 	}
// 	for fast.Next != nil {
// 		fast = fast.Next
// 		slow = slow.Next
// 	}
// 	slow.Next = slow.Next.Next
// 	fmt.Println(slow)
// 	printList(head)
// 	return head
// }

func addTwoNumbers(l1 *Node, l2 *Node) *Node {
	dummy := &Node{}
	l3 := dummy
	carry := 0
	for l1 != nil || l2 != nil {
		var sum int
		if l1 != nil {
			sum += l1.val
			l1 = l1.Next
		}
		if l2 != nil {
			sum += l2.val
			l2 = l2.Next
		}
		val := (sum + carry) % 10
		carry = (sum + carry) / 10
		fmt.Println(sum, carry, val, l3)
		// l3.val = val
		// l3 = l3.Next
		l3.Next = &Node{val: val, Next: nil}
		l3 = l3.Next

	}
	if carry > 0 {
		l3.Next = &Node{val: carry, Next: nil}
		l3 = l3.Next
	}
	printList(dummy.Next)
	return dummy

}
func main() {
	// list := &LinkList{}
	// list.Append(1)
	// list.Append(4)
	// list.Append(3)
	// list.Append(2)
	// list.Append(5)
	// list.Append(2)
	// fmt.Println("Initial List: ")
	// printList(list.head)
	// p := partition(list.head, 3)
	// printList(p)

	// list := &LinkList{}
	// list.Append(1)
	// list.Append(2)
	// list.Append(4)

	// list1 := &LinkList{}
	// list1.Append(1)
	// list1.Append(3)
	// list1.Append(4)
	// mergeTwoLists(list.head, list1.head)
	// printList(p)

	list1 := &LinkList{}
	list1.Append(1)
	// list1.Append(2)
	// list1.Append(3)
	// list1.Append(4)
	// list1.Append(5)
	// // list1.Append(6)

	// reorderList(list1.head)
	// printList(list1.head)
	removeNthFromEnd(list1.head, 1)

	// list1 := &LinkList{}
	// list1.Append(2)
	// list1.Append(4)
	// list1.Append(3)

	// list2 := &LinkList{}
	// list2.Append(5)
	// list2.Append(6)
	// list2.Append(4)

	// addTwoNumbers(list1.head, list2.head)
	//     Input: head = [1,2,3,4]
	// Output: [1,4,2,3]

}

func removeNthFromEnd(head *Node, n int) *Node {
	dummy := &Node{Next: head}
	slow, fast := dummy, head
	for n > 0 {
		fast = fast.Next
		n -= 1

	}
	if fast == nil {
		printList(slow.Next.Next)
		return slow.Next
	}

	for fast.Next != nil {
		slow = slow.Next
		fast = fast.Next

	}
	fmt.Println(slow, "DDDD")
	slow.Next = slow.Next.Next
	printList(dummy.Next)
	return head
}
