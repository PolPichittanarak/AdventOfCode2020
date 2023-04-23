#x = "4 - 5 m: mmmmmmpth"
#x = "14 - 15 s: gsrsssssbsssstkssmbsss"

def PasswordCheck(line):
	passworddata = line.partition(":") 
	passwordrange = passworddata[0].replace(" ", "")
	for character in passwordrange:
		if character.isalpha():
			TargetCharacter = character
			break
	passwordrangenumonly = passwordrange.replace(TargetCharacter, "")
	passwordnum = passwordrangenumonly.partition("-")

	CharacterMin = int(passwordnum[0])
	CharacterMax = int(passwordnum[2])
	CharacterPos1 = CharacterMin - 1
	CharacterPos2 = CharacterMax - 1

	password = passworddata[2].strip()
	if (password[CharacterPos1] == TargetCharacter and password[CharacterPos2] == TargetCharacter) or (password[CharacterPos1] != TargetCharacter and password[CharacterPos2] != TargetCharacter):
		return False
	elif (password[CharacterPos1] == TargetCharacter and password[CharacterPos2] != TargetCharacter) or (password[CharacterPos1] != TargetCharacter and password[CharacterPos2] == TargetCharacter):
		return True
	
	#CharacterCount = 0
	#for letter in password:
		#if letter == TargetCharacter:
			#CharacterCount += 1

	#if CharacterCount in range(CharacterMin, CharacterMax + 1):
		#return True
	#else: 
		#return False

file = open("Passworddata", "r")
content = file.readlines()
count = 0
validtrue = 0
for line in content:
	print(line)
	Valid = PasswordCheck(line)
	print(Valid)
	if Valid:
		validtrue += 1
	count += 1
print(count)
print(validtrue)








