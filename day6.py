def QuestionCount(GroupForm):
	SingleForm = GroupForm.split()
	QuestionAnswered = []
	QuestionAllAgreed = []
	AllQuestions = []
	PersonCount = 0
	AnswerAppCount = 0
	for SinglePerAnswer in SingleForm:
		PersonCount += 1
		for letter in SinglePerAnswer:
			AllQuestions.append(letter)
			if letter not in QuestionAnswered:
				QuestionAnswered.append(letter)
			print("letter variable: {}".format(letter))
	JoinedAllQuestions = "".join(AllQuestions)
	for letter in QuestionAnswered:
		LetterCount = JoinedAllQuestions.count(letter)
		if LetterCount == PersonCount:
			QuestionAllAgreed.append(letter)
	TotalQuantity = len(QuestionAnswered)
	print("AllQuestions variable: {}".format(AllQuestions))
	print("QuestionAllAgreed: {}".format(QuestionAllAgreed))
	print("QuestionAnswered variable: {}".format(QuestionAnswered))
	print("TotalQuantity variable: {}".format(TotalQuantity))
	return len(QuestionAllAgreed)



FormsCollection = open("CustomsDeclarationForms", "r")
FormsAnswers = FormsCollection.readlines()
FormsListCol = []
GroupAnswer = ""
TotalYes = 0
for passenger in FormsAnswers:
	if passenger != "\n":
		GroupAnswer += passenger.replace("\n", " ")
	elif passenger == "\n":
		FormsListCol.append(GroupAnswer.strip())
		GroupAnswer = ""
for form in FormsListCol:
	TotalYes += QuestionCount(form)
	print("len(QuestionAllAgreed) variable: {}".format(TotalYes))
	print()


