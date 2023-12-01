package main

import (
	"fmt"
	"os"
	"bufio"
	"unicode"
	"strconv"
	"strings"
)

var digitMap = map[string]int {
		"one": 1, "two": 2, "three": 3,
		"four": 4, "five": 5, "six": 6,
		"seven": 7, "eight": 8, "nine": 9,
	}

var keyOrder = []string{"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"}
var trickyOnes = []string{"twone", "sevenine", "oneight", "eighthree", "eightwo"}


func main(){
	var found bool
	var sum int
	var number int
	arr := readLines("text2")

	for _, lineRaw := range arr {
		found = false
		for _, key := range trickyOnes {
			if strings.Contains(lineRaw, key) == true {

				if strings.Compare(key, lineRaw) == 0 {
					number = getTrickyNumbs(key)
					fmt.Println(number)
					found = true
					break
				}
				number = getTrickyNumbs(key)
				lineRaw := strings.Replace(lineRaw, key, strconv.Itoa(number), -1)
				converted := replaceFirstToDigit(lineRaw)
				first := getFirstDigit(converted)
				converted = replaceLastOneToDigit(converted)
				last := getLastDigit(converted)
				number = joinDigits(first, last)
				fmt.Println(number)
				found = true
			}
		}
		if !found {
			converted := replaceFirstToDigit(lineRaw)
			first := getFirstDigit(converted)
			converted = replaceLastOneToDigit(converted)
			last := getLastDigit(converted)
			number = joinDigits(first, last)
			fmt.Println(number)
		}
		sum += number
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

func replaceFirstToDigit(line string) string {
	for _, key := range keyOrder {
		if strings.Contains(line, key) {
			line = strings.ReplaceAll(line, key, fmt.Sprintf("%d", digitMap[key]))
		}
	}
	return line
}


func replaceLastOneToDigit(line string) string {
	for _, key := range keyOrder {
		lastIndex := strings.LastIndex(line, key)
		if lastIndex != -1 {
			line = strings.ReplaceAll(line, key, fmt.Sprintf("%d", digitMap[key]))
			break
		}
	}
	return line
}

func getFirstDigit(line string) (int){
	var found bool
	var first rune
	for _, c := range line{
		if unicode.IsDigit(c){
			if !found {
				first = c
				found = true
			}
		}
	}
	f, err := strconv.Atoi(string(first))
	if err != nil {
		os.Exit(1);
	}
	return f
}

func getLastDigit(line string) (int){
	var found bool
	var last rune
	for _, c := range line{
		if unicode.IsDigit(c){
			if !found {
				found = true
			}
			last = c
		}
	}
	l, err := strconv.Atoi(string(last))
	if err != nil {
		os.Exit(1);
	}
	return l
}

func joinDigits(firstDigit int, lastDigit int)(int){
	return 10 * firstDigit + lastDigit
}

func getTrickyNumbs(key string)(int){
	switch key {
	case "twone":
		return 21
	case "oneight":
		return 18
	case "sevenine":
		return 79
	case "eighthree":
		return 83
	case "eightwo":
		return 82
	}
	return 0
}
