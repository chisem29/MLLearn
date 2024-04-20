package main

import (
	"fmt"
	"os"
	"sync"
	"sync/atomic"
	"time"
)

type Point struct {
	x int
	y int
}

type exteremes struct {
	top    int
	bottom int
	left   int
	right  int
}

type Shape struct {
	points map[Point]bool
	e      exteremes
}

func (shape *Shape) contains(x, y int) bool {
	_, ok := shape.points[Point{x, y}]
	return ok
}

func (shape *Shape) exteremes() exteremes {
	return shape.e
}

func (shape *Shape) isRect() bool {
	e := shape.exteremes()
	for y := e.top; y <= e.bottom; y++ {
		for x := e.left; x <= e.right; x++ {
			if !shape.contains(x, y) {
				return false
			}
		}
	}
	return true
}

func addPoint(shape *Shape, field [][]byte, x int, y int) {
	if x < 0 {
		return
	}
	if x >= len(field[0]) {
		return
	}
	if y < 0 {
		return
	}
	if y >= len(field) {
		return
	}
	if field[y][x] != 35 {
		return
	}

	shape.points[Point{x, y}] = true
	e := &shape.e
	if x > e.right {
		e.right = x
	}
	if x < e.left {
		e.left = x
	}
	if y > e.bottom {
		e.bottom = y
	}
	if y < e.top {
		e.top = y
	}
	field[y][x] = 0
	addPoint(shape, field, x-1, y)
	addPoint(shape, field, x, y-1)
	addPoint(shape, field, x+1, y)
	addPoint(shape, field, x, y+1)
}

func getShape(field [][]byte, x int, y int) Shape {
	shape := Shape{make(map[Point]bool, 0), exteremes{100000, -1, 1000000, -1}}
	addPoint(&shape, field, x, y)
	return shape
}

func getShapes(field [][]byte) []Shape {
	shapes := make([]Shape, 0)
	for y, row := range field {
		for x, cell := range row {
			if cell == 35 {
				shapes = append(shapes, getShape(field, x, y))
			}
		}
	}
	return shapes
}

func main() {
	var n int
	var m int
	start := time.Now()
	fmt.Scanf("%d %d\n", &n, &m)
	field := make([][]byte, n)
	for i := 0; i < n; i++ {
		fmt.Scanln(&field[i])
	}
	shapes := getShapes(field)
	var count int64 = 0
	var wg sync.WaitGroup
	for _, sh := range shapes {
		wg.Add(1)
		go func(sh Shape) {
			defer wg.Done()
			if sh.isRect() {
				atomic.AddInt64(&count, 1)
			}
		}(sh)
	}
	wg.Wait()
	fmt.Println(count)
	end := time.Now()
	fmt.Fprintf(os.Stderr, "%v\n", end.Sub(start))
}
