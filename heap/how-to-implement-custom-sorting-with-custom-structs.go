// // https://medium.com/@briankworld/how-to-implement-custom-sorting-with-custom-structs-in-go-322e9c1d26b8#:~:text=In%20Go%2C%20the%20standard%20library's,Less()%2C%20and%20Swap().

// // Define a custom struct type called Person
package main

import "fmt"

// import (
// 	"fmt"
// 	"sort"
// )

// type Person struct {
// 	Name string
// 	Age  int
// }
// type People []Person

// // Len
// // Less
// // Swap

// func (p People) Len() int {
// 	return len(p)
// }
// func (p People) Less(i, j int) bool {
// 	return p[i].Age < p[j].Age
// }

// func (p People) Swap(i, j int) {
// 	p[i], p[j] = p[j], p[i]
// }
// func createPointer() *int {
// 	var x int
// 	return &x // returning a pointer to a local variable
// }

// func (p *Person) IncrementAge() {
// 	p.Age++
// }

// func main() {
// 	p := createPointer()
// 	fmt.Println(*p) // Undefined behavior
// 	// Initialize a slice of Person structs
// 	people := People{
// 		{Name: "Alice", Age: 25},
// 		{Name: "Bob", Age: 30},
// 		{Name: "Charlie", Age: 20},
// 	}
// 	fmt.Println((people))

// 	// Sort the slice of Person structs by age using the sort package
// 	sort.Sort(people)
// 	fmt.Println((people))
// 	person := Person{"Alice", 30}
// 	ptr := &person

// 	ptr.IncrementAge()
// 	fmt.Println(person)

// 	person.IncrementAge()
// 	fmt.Println(person)

// }

type Person struct {
	Name string
	Age  int
}

func (p Person) IncrementAge() {
	p.Age++
}

func (p *Person) IncrementAge2() {
	p.Age++
}
func main() {
	person := Person{"Alice", 30}
	ptr := &person

	fmt.Printf("Address of person: %p\n", &person)
	fmt.Printf("Address of ptr: %p\n", ptr)

	ptr.IncrementAge()
	fmt.Println("Age after calling IncrementAge on ptr:", ptr.Age)

	person.IncrementAge()
	fmt.Println("Age after calling IncrementAge on person:", person.Age)

	ptr.IncrementAge2()
	fmt.Println("Age after calling IncrementAge2 on ptr:", ptr.Age)

	person.IncrementAge2()
	fmt.Println("Age after calling IncrementAge2 on person:", person.Age)
}
