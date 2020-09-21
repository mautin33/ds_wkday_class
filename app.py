#an isogram challenge

def findIsogram():
	user_input = input("Enter a word here: ").lower()

	word = []

	for i in user_input:

		if i in word:
			print("not an isogram")
			break

		else:
			word.append(i)


findIsogram()