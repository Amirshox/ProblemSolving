package main

func seatsInTheater(nCols int, nRows int, col int, row int) int {
	return (nCols - col) * (nRows - row)
}
