def island_matrix_counter(matrix: list[list[str]]) -> int:
	if not matrix:
		return 0

	visited: set[tuple[int, int]] = set()
	island_count = 0

	for row_index, row in enumerate(matrix):
		for column_index, cell in enumerate(row):
			position = (row_index, column_index)
			if cell != "1" or position in visited:
				continue

			island_count += 1
			stack = [position]
			visited.add(position)

			while stack:
				current_row, current_column = stack.pop()
				neighbors = (
					(current_row - 1, current_column),
					(current_row + 1, current_column),
					(current_row, current_column - 1),
					(current_row, current_column + 1),
				)

				for neighbor_row, neighbor_column in neighbors:
					if neighbor_row < 0 or neighbor_row >= len(matrix):
						continue
					if neighbor_column < 0 or neighbor_column >= len(matrix[neighbor_row]):
						continue

					neighbor_position = (neighbor_row, neighbor_column)
					if (
						matrix[neighbor_row][neighbor_column] == "1"
						and neighbor_position not in visited
					):
						visited.add(neighbor_position)
						stack.append(neighbor_position)

	return island_count
