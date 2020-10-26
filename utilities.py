class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def head(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)


def traverse(graph):

    current_path = Stack()

    moves = []

    visited = set()

    current_path.push(0)

    while len(visited) < len(graph):
        room_id = current_path.head()
        visited.add(room_id)

        current_room = graph[room_id]

        adjacent_rooms = current_room[1]

        undiscovered = []

        for direction, adjacent_id in adjacent_rooms.items():
            if adjacent_id not in visited:
                undiscovered.append(adjacent_id)

        if len(undiscovered) > 0:
            next_room = undiscovered[0]
            current_path.push(next_room)
        else:
            current_path.pop()
            next_room = current_path.head()

        for direction, adjacent_id in adjacent_rooms.items():
            if adjacent_id == next_room:
                moves.append(direction)
    return moves