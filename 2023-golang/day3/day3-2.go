
package main

import (
	"fmt"
	"os"
	"strings"
	"strconv"
	"unicode"
	)

type partNumb struct {
	value int
	len int
	row	int
	col int
}

func main(){
	numList := readLines("text")
	fmt.Println(extactNumbers(numList))
}

func readLines(filePath string) ([]string){
	input, err := os.ReadFile(filePath)
		if err != nil {
			fmt.Println("Error reading file:", err)
			os.Exit(1)
		}
	content := string(input)
	return strings.Split(content, "\n")
}

func extactNumbers(engineSchema []string)(int) {
	var str strings.Builder
	var sum int
	for i, line := range engineSchema{
		for j:=0; j<len(line); j++{

			if unicode.IsDigit(rune(line[j])) {
				for k := j; k < len(line) && unicode.IsDigit(rune(line[k])); k++ {
					str.WriteByte(line[k])
				}
				strNum := str.String()
				if strNum != "" && isAdjecent(engineSchema, i, j, len(strNum)) {
					partNum := handleStrDigit(strNum)
					sum += partNum
				}
				j += len(strNum)
				str.Reset()
			}
		}
	}
	return sum
}

func isAdjecent(engineSchema []string, row int, col int, lenS int) (bool) {
	symbol := '*'
	for i := row - 1; i <= row + 1; i++{
		for j := col - 1; j <= col + lenS; j++ {
			if i >= 0 && i < len(engineSchema) && j >=0 && j < len(engineSchema[i]){
				if symbol == engineSchema[i][j] {
					return true
				}
			}
		}
	}
	return false
}


func handleStrDigit(strNum string)(int){
	num, err := strconv.Atoi(strNum)
	if (err != nil){
		os.Exit(1)
	}
	return num
}

func makeStruct(strNum string, r int, c int) (partNumb) {
	var new partNumb
	return {value: handleStrDigit(strNum), len: len(strNum), row: r, col: c}
}


{ID: "1", Item: "Clean Room", Completed: false},

var todos = []todo {
	{ID: "1", Item: "Clean Room", Completed: false},
	{ID: "2", Item: "Read Book", Completed: false},
	{ID: "3", Item: "Record Video", Completed: false},
}
