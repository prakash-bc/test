package main

import (
	"fmt"
	"sort"
)

func carFleet(target int, position []int, speed []int) int {
	var cars [][2]int = make([][2]int, len(position))
	for i := range cars {
		cars[i] = [2]int{
			position[i],
			speed[i],
		}
	}
	sort.Slice(cars, func(i, j int) bool { return cars[i][0] > cars[j][0] })
	fmt.Println(cars)

	var time []float64 = make([]float64, 0, len(cars))

	for _, car := range cars {
		p, s := car[0], car[1]
		ct := float64(target-p) / float64(s)
		fmt.Println(p, s, ct)
		if len(time) == 0 || ct > time[len(time)-1] {
			time = append(time, ct)
		}
	}
	fmt.Println(time)
	return len(time)
}

func main() {
	target := 12
	position := []int{10, 8, 0, 5, 3}
	speed := []int{2, 4, 1, 1, 3}
	carFleet(target, position, speed)
}
