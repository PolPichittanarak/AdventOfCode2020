def deci_to_bi(decimal):
	x = "000000000000000000000000000000000000"
	y = decimal
	z  = list(x)
	subtract = y
	for i, letter in enumerate(reversed(x)):
		exponent = 35 - i
		binaryexponent = 2 ** exponent
		subtraction = subtract - binaryexponent
		if subtraction >= 0:
			subtract = subtraction
			z[i] = '1'
		else:
			pass
	x = "".join(z)
	return x 

def masking(mask, value):
	result = ""
	for i, letter in enumerate(mask):
		if mask[i] == "X":
			result += value[i]
		else:
			if mask[i] == value[i]:
				result += value[i]
			else:
				result += mask[i]
	return result 
	
def memorycheck(mem_removed, result):
	biaddresses = open("binary_address", "r")
	filecont2 = biaddresses.readlines()
	for line2 in filecont2:
		splitline2 = line2.split(":")
		print("splitline2 : " + str(splitline2))
		if mem_removed == splitline2[0]:
			print("True")
			remove_mem(mem_removed)
	write_updated(mem_removed, result)
	biaddresses.close()
	return

def remove_mem(mem_removed):
	biaddresses = open("binary_address", "r")
	filecont3 = biaddresses.readlines()
	biaddresses.close()
	biaddresses_w = open("binary_address", "w")
	for line in filecont3:
		if line != mem_removed:
			biaddresses_w.write("NEW")
			biaddresses_w.write(line)
	biaddresses.close()

def write_updated(mem_removed, result):
	biaddresses3 = open("binary_address", "a")
	biaddresses3.write("{}:".format(mem_removed) + result)
	biaddresses3.close()

bimask = open("binary_masking", "r")
filecont = bimask.readlines()

for line in filecont:
	if line[:4] == "mask":

		mask = line
		mask_split = mask.split("=")
		mask_mod = mask_split[1].strip().replace('"', "")
		#print(mask_mod)

	else:
		splitline = line.split("=")	
		#print(splitline) #['mem[9227] ', ' 2018\n']

		value = splitline[1].strip().replace("\n", "")
		valueinbi = deci_to_bi(int(value))
		result = masking(mask_mod, valueinbi)

		print("value : {}".format(value))
		print("mask :      {}".format(mask_mod))
		print("valueinbi : {}".format(valueinbi))
		print("result :    {}".format(result))

		mem_removed = splitline[0].replace("mem[", "").replace("]", "").strip()
		print("mem_removed : {}".format(mem_removed))
		print()
		memreplace = memorycheck(mem_removed, result)
		



