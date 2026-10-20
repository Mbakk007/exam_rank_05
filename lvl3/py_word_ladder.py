def word_ladder(start: str, end: str, sentence: list[str]) -> int:
	if start == end:
		return 1
	if len(start) != len(end) or end not in sentence:
		return 0

	words = set(sentence)
	visited = {start}
	queue = [(start, 1)]
	index = 0

	while index < len(queue):
		current, length = queue[index]
		index += 1

		for word in words:
			if word in visited or len(word) != len(current):
				continue

			differences = 0
			for position in range(len(current)):
				if current[position] != word[position]:
					differences += 1
					if differences > 1:
						break

			if differences == 1:
				if word == end:
					return length + 1
				visited.add(word)
				queue.append((word, length + 1))

	return 0