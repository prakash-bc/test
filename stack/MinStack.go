type MinStack struct {
	Stack []int
	Min   []int
}

func Constructor() MinStack {
	return MinStack{Stack: []int{}, Min: []int{}}

}
func min(x, y int) int {
	if x < y {
		return x
	}
	return y
}
func (this *MinStack) Push(val int) {
	this.Stack = append(this.Stack, val)
	if len(this.Min) != 0 {
		this.Min = append(this.Min, min(val, this.GetMin()))
	} else {
		this.Min = append(this.Min, val)

	}

}

func (this *MinStack) Pop() {
	this.Stack = this.Stack[:len(this.Stack)-1]
	this.Min = this.Min[:len(this.Min)-1]

}

func (this *MinStack) Top() int {
	return this.Stack[len(this.Stack)-1]
}

func (this *MinStack) GetMin() int {
	return this.Min[len(this.Min)-1]
}
