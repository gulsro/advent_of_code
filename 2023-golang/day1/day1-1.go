package main

import (
	"fmt"
	"os"
	"bufio"
	"unicode"
	"strconv"
)

func main(){
	sum := 0
	arr := readLines("text2")
	for _, line := range arr{
		numb := getNumb(line)
		sum += numb
	}
	fmt.Println(sum)
}

func readLines(filePath string) ([]string){
	var lines []string
	file, err := os.Open(filePath)

	if err != nil {
		fmt.Println("Error: ", err)
		os.Exit(1);
	}

	scanner := bufio.NewScanner(file)
	for scanner.Scan(){
		lines = append(lines, scanner.Text())
	}
	return lines
}

func getNumb(line string) (int){
	var found bool
	var first rune
	var last rune
	for _, c := range line{
		if !unicode.IsDigit(c){
			continue
		}
		if (!found){
			first = c
			found = true
		}
		last = c
	}
	f, err := strconv.Atoi(string(first))
	if err != nil {
		os.Exit(1);
	}
	l, err := strconv.Atoi(string(last))
	if err != nil {
		os.Exit(1);
	}
	return 10 * f + l
}
