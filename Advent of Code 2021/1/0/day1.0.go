package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func main() {
	f, err := os.Open("input")

	check(err)

	defer f.Close()

	scanner := bufio.NewScanner(f)
	scanner.Split(bufio.ScanWords)
	var lastValue = 0
	var increasing = 0
	var decreasing = 0
	for scanner.Scan() {
		thisValue, err := strconv.Atoi(scanner.Text())
		check(err)
		// Initialize lastValue
		if lastValue == 0 {
			lastValue = thisValue
		}
		if thisValue > lastValue {
			increasing++
		}

		lastValue = thisValue
	}

	fmt.Println("Number of increases:", increasing)
	fmt.Println("Number of decreases:", decreasing)
}
