package main

import (
	"container/heap"
	"fmt"
)

type Point struct {
	dist int
	x    int
	y    int
}

type PointHeap []*Point

func (p PointHeap) Len() int {
	return len(p)
}
func (p PointHeap) Swap(i, j int) {
	p[i], p[j] = p[j], p[i]
}

func (p PointHeap) Less(i, j int) bool {
	return p[i].dist < p[j].dist
}

func (p *PointHeap) Push(i any) {
	*p = append(*p, i.(*Point))
}

func (p *PointHeap) Pop() any {
	old := *p
	l := len(old)
	x := old[l-1]
	*p = old[0 : l-1]
	return x
}

const X = 0
const Y = 1

func kClosest(points [][]int, k int) [][]int {
	// sort.Sort()
	// heap.Init()
	_pts := make([]*Point, 0, len(points))
	for _, point := range points {
		dist := (pow(point[0], 2) + pow(point[1], 2))
		_pts = append(_pts, &Point{dist: dist, x: point[X], y: point[Y]})
	}
	pt := PointHeap(_pts)
	fmt.Println(pt)
	for _, x := range pt {
		fmt.Println(x, "1111")
	}

	res := make([][]int, 0)
	heap.Init(&pt)
	for _, x := range pt {
		fmt.Println(x, "22")
	}

	for _ = range k + 1 {
		x := heap.Pop(&pt).(*Point)
		res = append(res, []int{x.x, x.y})
	}
	fmt.Println(res, "DDDDDDDDDDDDDDD")
	return res
}
func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func pow(x, n int) int {
	if n == 0 {
		return 1
	} else if n == 1 {
		return x
	} else {
		return pow(x, n/2) * pow(x, (n+1)/2)

	}
}
func main() {
	kClosest([][]int{{1, 3}, {-2, 2}}, 1)
}
