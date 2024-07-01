package main

import (
	"container/heap"
	"fmt"
)

type IntHeap []int

func (h IntHeap) Len() int            { return len(h) }
func (h IntHeap) Less(i, j int) bool  { return h[i] < h[j] }
func (h IntHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *IntHeap) Push(x interface{}) { *h = append(*h, x.(int)) }
func (h *IntHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

func main() {
	// [2,7,4,1,8,1]
	// nums := &intHeap{3, 1, 4, 5, 1, 1, 2, 6}
	nums := &IntHeap{2, 7, 4, 1, 8, 1}

	// fmt.Println(nums)
	heap.Init(nums)

	fmt.Println(nums)
	_stones := []int{2, 7, 4, 1, 8, 1}
	for s := 0; s < len(_stones); s++ {
		_stones[s] *= -1
	}
	fmt.Println(_stones)

	stones := IntHeap(_stones)
	heap.Init(&stones)
	fmt.Println(_stones)

	// stones := []int{3, 1, 4, 5, 1, 1, 2, 6}
	// h := &intHeap{stones}
	// heap.Init(h)
	// for _, val := range stones {
	// 	heap.Push(h, val)
	// }
	// fmt.Println(h)
	// for nums.Len() >= 2 {
	// 	x := nums.Pop().(int)
	// 	y := nums.Pop().(int)
	// 	if x != y {
	// 		heap.Push(nums, x-y)
	// 	}
	// }
	// fmt.Println(nums)
}
