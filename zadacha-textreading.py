# file = open("python.txt", "r")
# while True:
# 	content=file.readline()
# 	if not content:
# 		break
# 	print(content)
# file.close()

# file = open("large_file.csv", "r")
# content=file.readlines()
# print(content)
# file.close()

# file = open("test.txt", "w")
# sample_list = ["one", "two", "three"]
# for item in sample_list:
#     file.write(item)
#     file.write('\n')
# file.close()

# file = open("test.txt", "w")
# sample_list = ["one", "two", "three"]
# file.writelines(sample_list)
# file.close()
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
