package main

import (
	"fmt"
	"os"
	"strings"
	"slices"
//	"unicode"
)

func main(){
	var point int
	var sum int
	lines := readLines("text")
	for _, line := range lines {
		hand, winner := splitHand(line)
		point = checkWinners(hand, winner)
		sum += point
	}
	fmt.Println(sum)
}

func readLines(filePath string) ([]string){
	var lines []string

	input, err := os.ReadFile(filePath)
		if err != nil {
			fmt.Println("Error reading file:", err)
			os.Exit(1)
		}
	content := string(input)
	cards := strings.Split(content, "\n")
	for _, line := range cards{
		newLine := strings.Split(line, ":")
		trimmed := newLine[len(newLine) - 1]
		lines = append(lines, trimmed)
	}
	return lines
}

func splitHand(line string)([]string, []string){
	piped := strings.Split(line, "|")
	hand := strings.Fields(piped[0])
	winner := strings.Fields(piped[len(piped) - 1])
	return hand, winner
}

func checkWinners(hand []string, winner []string) int {
	var found int
	for _, num := range hand {
		if slices.Contains(winner, num) {
			found += 1
		}
	}
	return calculatePoints(found)
}

func calculatePoints(len int) int {
	var total = 1
	var i int
	if len == 0 {
		return 0
	}
	for i < len-1 {
		total *= 2
		i += 1
	}
	return total
}