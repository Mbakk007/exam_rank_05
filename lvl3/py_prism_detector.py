def prism_detector(grid: list[str], pattern: str):
	if not grid or not pattern:
		return []

	directions = (
		(1, 0, "H"),
		(-1, 0, "H-"),
		(0, 1, "V"),
		(0, -1, "V-"),
		(1, 1, "D1"),
		(-1, -1, "D1-"),
		(-1, 1, "D2"),
		(1, -1, "D2-"),
	)
	matches = []

	for y, row in enumerate(grid):
		for x in range(len(row)):
			for dx, dy, direction in directions:
				found = True
				for index in range(len(pattern)):
					next_x = x + dx * index
					next_y = y + dy * index
					if (
						next_y < 0
						or next_y >= len(grid)
						or next_x < 0
						or next_x >= len(grid[next_y])
						or grid[next_y][next_x] != pattern[index]
					):
						found = False
						break
				if found:
					matches.append((x, y, direction))

	return matches