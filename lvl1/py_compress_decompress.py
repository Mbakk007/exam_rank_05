def compress(s: str) -> str:
	result = ""
	count = 0
	before = ""
	for letter in s:
		if before == letter or before == "":
			count += 1
		else:
			result += before
			if count > 1:
				result += str(count)
			count = 1
		before = letter
	if before != "":
		result += before
		if count > 1:
			result += str(count)
	return result

def decompress(s: str) -> str:
	result = ""
	temp = ""
	i = 0
	while i < len(s):
		temp = s[i]
		result += temp
		i += 1
		start = i
		while i < len(s) and s[i].isdigit():
			i += 1
		if i > start:
			count = int(s[start:i])
			while count > 1:
				result += temp
				count -= 1
	return result




if __name__ == "__main__":
	print(compress("hhhhheelllllloooo"))
	print(decompress("h5e2l6o4"))