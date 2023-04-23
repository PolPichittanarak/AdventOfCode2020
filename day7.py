baggages_list = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
big green bags contain 2 light red bags.
black dotted bags contain 3 big green bags"""
baggages_list_split = baggages_list.split(".")
#print(baggages_list_split)
#print()
bagtoidentify = "shiny gold bag" 
bagfound = 0
def bagsortextension(bagtoidentify1, baggages_list_split):
	print()
	print()
	print()
	print("bagtoidentify1: {}".format(bagtoidentify1))
	print()
	BagToIdenUp = [bagtoidentify1, bagtoidentify1 + "s"]
	bagfound = 0
	bagcontained1 = []
	for bag in baggages_list_split:
		if bag == "":
			break
		else:
			bagelement = bag.split("contain")
			mainbag = bagelement[0].strip()
			bagcontainment = bagelement[1].strip()
			#print("mainbag: {}".format(mainbag))
			#print("mainbag split: {}".format(mainbag.split()))
			#print("bagcontainment: {}".format(bagcontainment))
			#print("bagcontainment split: {}".format(bagcontainment.split(",")))
			for i, bagcontained in enumerate(bagcontainment.split(",")):
				bagcontained = bagcontained[2:].strip()
				#print("bag", i+1 , ": {}".format(bagcontained))
				if bagcontained in BagToIdenUp:
					bagcontained1.append(mainbag)
					bagfound += 1
					print()
					print("bagfound: {}".format(bagfound))
					print()
	bagstoreturn = []
	bagstoreturn.append(bagfound)
	bagstoreturn.append(bagcontained1)
	print("BAGSTORETURN: {}".format(bagstoreturn))
	return bagstoreturn


def bagsort(bagtoidentify, baggages_list_split):
	print("bagtoidentify : {}".format(bagtoidentify))
	BagToIdenUp = [bagtoidentify, bagtoidentify + "s"]
	bagfound = 0
	bagcontaining = []
	bagtoreturn = []
	for i, bag in enumerate(baggages_list_split):
		if bag == "":
			break
		else:
			print("bag number", i+1, ":")
			bagelement = bag.split("contain")
			mainbag = bagelement[0].strip()
			bagcontainment = bagelement[1].strip()
			#print("mainbag: {}".format(mainbag))
			#print("mainbag split: {}".format(mainbag.split()))
			#print("bagcontainment: {}".format(bagcontainment))
			#print("bagcontainment split: {}".format(bagcontainment.split(",")))
			for i, bagcontained in enumerate(bagcontainment.split(",")):
				bagcontained = bagcontained[2:].strip()
				#print("bag", i+1 , ": {}".format(bagcontained))
				if bagcontained in BagToIdenUp:
					bagfound += 1
					bagcontaining.append(mainbag)
					#print("bagcontaining: {}".format(bagcontaining))
			print("bag found : {}".format(bagfound))
			print("bagcontaining : {}".format(bagcontaining))
			print()
	bagtoreturn.append(bagfound)
	bagtoreturn.append(bagcontaining)
	print("bagtoreturn: {}".format(bagtoreturn))
	print()
	return bagtoreturn

x = bagsort("shiny gold bag", baggages_list_split)
print("x : {}".format(x))
shinygoldbagraw = x[0]
bagscontaininggold = x[1]
print("shinygoldbagraw: {}".format(shinygoldbagraw))
print("bagscontaininggold: {}".format(bagscontaininggold))
baggagedup = []
for baggage in bagscontaininggold:
	baggage = baggage[:-1:]
	y = bagsort(str(baggage), baggages_list_split)
	print("y : {}".format(y))
	print()
	baggagedup.append(y)
#print(baggagedup)
print("baggagedup: {}".format(baggagedup))
print()
for bag1 in baggagedup:
	del bag1[0]
#print("baggagedup: {}".format(baggagedup))
totalbaggages = []
for bag1 in baggagedup:
	for bag2 in bag1:
		for bag3 in bag2:
			totalbaggages.append(bag3)
newtotalbaggages = list(set(totalbaggages))
allbags = []
for baggage in newtotalbaggages:
	allbags.append(baggage)
for baggage1 in bagscontaininggold:
	allbags.append(baggage1)
print(allbags)
duplicate_allbags = allbags
print("allbag {}".format(allbags))
count = 0
while duplicate_allbags != []:
	for baggageloop in duplicate_allbags:
		baggageloop1 = baggageloop[:-1:]
		z = bagsort(baggageloop1, baggages_list_split)
		print("z: {}".format(z))
		duplicate_allbags.remove(baggageloop)
		print("new dup list: {}".format(duplicate_allbags))
		count += z[0]
		print(z[0])
		for bagidentified in z[1]:
			print(bagidentified)
			if bagidentified not in duplicate_allbags:
				duplicate_allbags.append(bagidentified)
		print("count: {}".format(count))
print("final count = {}".format(count))
print("shinygoldbagraw: {}".format(shinygoldbagraw))

