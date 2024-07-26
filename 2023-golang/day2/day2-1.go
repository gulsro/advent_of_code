package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

type count struct {
	redCount int
	greenCount int
	blueCount int
}

func main() {
	input := readLines("text")
	colourCount := count{redCount: 12, greenCount: 13, blueCount: 14}
	possibleGames := findPossibleGames(input, 12, 13, 14)
	fmt.Println("Sum of possible game IDs:", possibleGames)
}

func readLines(filePath string) []string {
	var lines string
	file, err := os.ReadFile(filePath)

	if err != nil {
		fmt.Println("Error: ", err)
		os.Exit(1)
	}
	content := string(file)
	lines := strings.Split(content, "\n")
	return lines
}

func findPossibleGames(lines []string, colourCount count) (int) {
	var sumPossibleGames int

	for _, game := range lines {
		if strings.TrimSpace(game) == "" {
			continue
		}

		var gameId int
		var sets string
		fmt.Sscanf(game, "Game %d:%s", &gameId, &sets)

		if possibleGame(sets, redCount, greenCount, blueCount) {
			sum += gameId
		}
	}
	return sum
}

func possibleGame(sets string, colourCount count) bool {
	gameMap := map[string]int{
			"red": colourCount.redCount,
			"green": colourCount.greenCount,
			"blue": colourCount.blueCount
			}

	setList := strings.Split(sets, ";")
	for _, subset := range setList {
		setCubes := strings.Fields(subset)
		for _, cube := range setCubes[1:] {
			color := strings.ToLower(cube)
			gameMap[color]--

			if gameMap[color] < 0 {
				return false
			}
		}
	}
	return true
}

// package main

// import (
// 	"fmt"
// 	"strings"
// )

// func main() {
// 	input := readLines("text")
// 	possibleGames := findPossibleGames(input, 12, 13, 14)
// 	fmt.Println("Sum of possible game IDs:", possibleGames)
// }

// func readLines(filePath string) (string){
// 	var lines []string
// 	file, err := os.Open(filePath)

// 	if err != nil {
// 		fmt.Println("Error: ", err)
// 		os.Exit(1);
// 	}

// 	scanner := bufio.NewScanner(file)
// 	for scanner.Scan() {
// 		game := scanner.Text()

// 		if strings.TrimSpace(game) == "" {
// 			continue
// 		}

// 	return game
// }

// func findPossibleGames(input string, redCount string, greenCount string, blueCount int) (int) {
// 	var sumPossibleGames int

// 	games := strings.Split(input, "\n")

// 	for _, game := range games {
// 		if strings.TrimSpace(game) == "" {
// 			continue
// 		}

// 		// Parse game ID and subsets
// 		var gameID int
// 		var subsets []string
// 		fmt.Sscanf(game, "Game %d:%s", &gameID, &subsets)

// 		// Simulate cube distribution for the game
// 		if isPossibleGame(subsets, redCount, greenCount, blueCount) {
// 			sumPossibleGames += gameID
// 		}
// 	}
// 	return sumPossibleGames
// }

// func isPossibleGame(subsets string, redCount string, greenCount string, blueCount int) (bool) {
// 	cubeCounts := map[string]int{"red": redCount, "green": greenCount, "blue": blueCount}

// 	subsetList := strings.Split(subsets, ";")
// 	for _, subset := range subsetList {
// 		cubes := strings.Fields(subset)
// 		for _, cube := range cubes[1:] {
// 			color := strings.ToLower(cube)
// 			cubeCounts[color]--

// 			if cubeCounts[color] < 0 {
// 				return false
// 			}
// 		}
// 	}
// 	return true
// }


// 0: 20 green, 3 red, 2 blue;||| 9 red, 16 blue, 18 green; 6 blue, 19 red, 10 green;
// 			||| 12 red, 19 green, 11 blue

// func mapInMap(gameMap map[int]string) (map[int]map) {
// 	for i, game := range gameMap {
// 		make(map[string]int)
// 	}
// }

// func totalCubeChecker(game map[int]string)(bool)
// {
// 	var total int
// 	for _, round := range game {
// 		for i := 0; len(round); i++{
// 			if round[i] != ';'
// 			&& unicode.IsDigit(round[i]){
// 				total += int(round[i])
// 			}
// 		if total > 39
// 			return false
// 		}
// 	}

// }
