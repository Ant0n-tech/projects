output_list = []
file = open("people.csv", mode = "r",encoding = "utf-8")
while True:
	line = file.readline()
	if not line:
		break
	token_list = line.split(',')
	age = int(token_list[2])
	city = token_list[3]
	if age > 38 and city.lower() == 'Железаре':
		break

file.close()


# file = open("duplicate_python.txt", "w")
# file.writelines(content)
# file.close()
