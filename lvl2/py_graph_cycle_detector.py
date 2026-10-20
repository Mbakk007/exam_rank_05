def py_graph_cycle_detector(graph: dict[int, list[int]]) -> bool:
	visited: set[int] = set()
	visiting: set[int] = set()

	def visit(node: int) -> bool:
		if node in visiting:
			return True
		if node in visited:
			return False

		visiting.add(node)
		for neighbor in graph.get(node, []):
			if visit(neighbor):
				return True
		visiting.remove(node)
		visited.add(node)
		return False

	for node in graph:
		if visit(node):
			return True

	return False