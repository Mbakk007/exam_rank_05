from typing import Any

def py_room_scheduler(meetings: list[list[int]]) -> dict[str, Any]:
	if not meetings:
		return {"total_rooms": 0, "schedule": []}
	sorted_meetings = sorted(meetings, key=lambda x: x[0])
	schedule: list[list[list[int]]] = []

	for meeting in sorted_meetings:
		start_time = meeting[0]
		assigned = False

		for room in schedule:
			if room[-1][1] <= start_time:
				room.append(meeting)
				assigned = True
				break

		if not assigned:
			schedule.append([meeting])

	return {"total_rooms": len(schedule), "schedule": schedule}