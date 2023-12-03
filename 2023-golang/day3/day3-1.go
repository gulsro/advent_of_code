package main

import (
	"fmt"
	"os"
	"strings"
	"strconv"
	"unicode"
	)

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
	symbols := "*$+@-/%&=#"
	for i := row - 1; i <= row + 1; i++{
		for j := col - 1; j <= col + lenS; j++ {
			if i >= 0 && i < len(engineSchema) && j >=0 && j < len(engineSchema[i]){
				if strings.ContainsRune(symbols, rune(engineSchema[i][j])){
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


