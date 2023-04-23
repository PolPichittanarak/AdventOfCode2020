data = open("Passport_Data_4", "r")
datacontent = data.readlines()
passport_groups = []
passport1 = ""

for line in datacontent:
	if line != "\n":
		passport1 += line.replace("\n", " ")
	elif line == "\n":
		passport_groups.append(passport1.strip())
		passport1 = ""
		
def eclcheck(ecl):
	#amb blu brn gry grn hzl oth
	validecl = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
	if ecl in validecl:
		return True
	else:
		return False

def hgtcheck(hgt):
	if hgt[-2:] == "cm":
		heightcm = int(hgt[:-2])
		if heightcm in range(150, 194):
			return True
	elif hgt[-2:] == "in":
		heightin = int(hgt[:-2])
		if heightin in range(59, 77):
			return True
	return False

def iyrcheck(iyr):
	if len(iyr) != 4:
		return False
	issueyear = int(iyr)
	if issueyear in range(2010,2021):
		return True
	else:
		return False

def eyrcheck(eyr):
	if len(eyr) != 4:
		return False
	expiryyear = int(eyr)
	if expiryyear in range(2020, 2031):
		return True
	else:
		return False

def pidcheck(pid):
	if len(pid) != 9:
		return False
	else:
		return True
def byrcheck(byr):
	if len(byr) != 4:
		return False
	birthyear = int(byr)
	if birthyear in range(1920, 2003):
		return True
	else:
		return False
def hclcheck(hcl):
	validcharacter = ["0", '1', "2", "3", "4", "5", "6", "7", "8", '9', "a", "b", "c", "d", "e", "f", "#"]
	if len(hcl) == 7:
		if hcl[0] == "#":
			for character in hcl:
				if character in validcharacter:
					continue
				else:
					return False
			return True
		else:
			return False
	else:
		return False

def validdatacheck(passportdata):
	passportdetails = []
	for i, passport_field in enumerate(passportdata):
		passportdetails.append(passport_field.split(":"))
	for passportelement in passportdetails:
		if passportelement[0] == "ecl":
			eclvalid = eclcheck(passportelement[1])
			print("ecl valid checkpoint : {}".format(eclvalid))
			if not eclvalid:
				return False
		elif passportelement[0] == "hgt":
			hgtvalid = hgtcheck(passportelement[1])
			print("hgt valid checkpoint : {}".format(hgtvalid))
			if not hgtvalid:
				return False
		elif passportelement[0] == "iyr":
			iyrvalid = iyrcheck(passportelement[1])
			print("iyr valid checkpoint : {}".format(iyrvalid))
			if not iyrvalid:
				return False
		elif passportelement[0] == "eyr":
			eyrvalid = eyrcheck(passportelement[1])
			print("eyr valid checkpoint : {}".format(eyrvalid))
			if not eyrvalid:
				return False
		elif passportelement[0] == "pid":
			pidvalid = pidcheck(passportelement[1])
			print("pid valid checkpoint : {}".format(pidvalid))
			if not pidvalid:
				return False
		elif passportelement[0] == "byr":
			byrvalid = byrcheck(passportelement[1])
			print("byr valid checkpoint : {}".format(byrvalid))
			if not byrvalid:
				return False
		elif passportelement[0] == "hcl":
			hclvalid = hclcheck(passportelement[1])
			print("hcl valid checkpoint : {}".format(hclvalid))
			if not hclvalid:
				return False
	print("valid")
	return True

def passport_check(passportdata):
	fieldsrequired = ["ecl", "iyr", "hgt", "eyr", "pid", "byr", "hcl"]
	fields_containing = []
	for i, passport_field in enumerate(passportdata):
		#print(passport_field.split(":"))
		field = passport_field[:3]
		fields_containing.append(field)
	print("This passport contains {} fields".format(i+1))
	#print(fields_containing)
	
	for field in fieldsrequired:
		if field in fields_containing:
			continue
		else:
			return False
	return True

completepassport = 0
completevalidpassport = 0
valid_passport = 0
for passport in passport_groups:
	passportdata = passport.split(" ")
	valid = passport_check(passportdata)
	if valid:
		completepassport += 1
		validdatacheck1 = validdatacheck(passportdata)
		print("Valid data check 1 check point: {}".format(validdatacheck1))
		if validdatacheck1:
			completevalidpassport += 1
			valid_passport += 1
	print()
	print()
print(valid_passport)
print(completepassport)
print(completevalidpassport)
