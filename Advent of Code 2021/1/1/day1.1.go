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

func stackShiftLeft(arr []int, newItem int) []int {
	for i := 0; i < len(arr); i++ {
		if i == (len(arr) - 1) {
			arr[i] = newItem
		} else {
			arr[i] = arr[i+1]
		}
	}
	return arr
}

func findArraySum(arr []int) int {
	result := 0
	for i := 0; i < len(arr); i++ {
		result += arr[i]
	}
	return result
}

func main() {
	f, err := os.Open("input")

	check(err)

	defer f.Close()

	scanner := bufio.NewScanner(f)
	scanner.Split(bufio.ScanWords)
	var groupSize = 3
	var group = make([]int, groupSize)
	var lastSweep int
	var increasing = 0
	var decreasing = 0
	var nochange = 0
	for scanner.Scan() {
		// convert string to int
		thisValue, err := strconv.Atoi(scanner.Text())
		check(err)

		group := stackShiftLeft(group, thisValue)
		thisSweep := findArraySum(group)

		// Skip loops where we have not yet filled the buffer
		var zeroEncounter = false
		for i := 0; i < len(group); i++ {
			if group[i] == 0 {
				fmt.Println("breaking because full set not yet availible")
				zeroEncounter = true
				break
			}
		}
		if zeroEncounter {
			continue
		}

		// if this is the ifrst iteration, don't increment anything
		if lastSweep == 0 {
			lastSweep = thisSweep
			continue
		}

		if thisSweep > lastSweep {
			increasing++
		} else if thisSweep < lastSweep {
			decreasing++
		} else if thisSweep == lastSweep {
			nochange++
		}

		// store computed set for reference
		lastSweep = thisSweep
	}

	fmt.Println("Number of increases:", increasing)
	fmt.Println("Number of decreases:", decreasing)
	fmt.Println("Number of noChange:", nochange)

}
