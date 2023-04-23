#BFFFBBFRLR
#FBFFFBBLRL
def SeatingRowSlicing(SeatingRow):
	#SeatingRow = BFFFBBF
	PossibleRow = []
	for Row in range(0, 128):
		PossibleRow.append(Row)
	for bit in range(len(SeatingRow)):
		HalvedTotalRow = len(PossibleRow) // 2
		if SeatingRow[bit] == "B":
			PossibleRow = PossibleRow[HalvedTotalRow:]
		elif SeatingRow[bit] == "F":
			PossibleRow = PossibleRow[:HalvedTotalRow]
	Row = int(PossibleRow[0])
	return Row
	
def SeatingColumnSlicing(SeatingColumn):
	TotalColumn = []
	for Column in range(0, 8):
		TotalColumn.append(Column)
	for bit in range(len(SeatingColumn)):
		HalvedTotalColumn = len(TotalColumn) // 2
		if SeatingColumn[bit] == "R":
			TotalColumn = TotalColumn[HalvedTotalColumn:]
		elif SeatingColumn[bit] == "L":
			TotalColumn = TotalColumn[:HalvedTotalColumn]
	Column = int(TotalColumn[0])
	return Column

BPCollection = open("BinaryBoardingPass", "r")
BoardingPassData = BPCollection.readlines()
HighestSeatID = 0

for BoardingPass in BoardingPassData:
	SeatingRow = SeatingRowSlicing(BoardingPass[:7])
	SeatingColumn = SeatingColumnSlicing(BoardingPass[7:])
	BoardingPassID = SeatingRow * 8 + SeatingColumn
	if BoardingPassID > HighestSeatID:
		HighestSeatID = BoardingPassID
print(HighestSeatID)
