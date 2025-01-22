from collections import deque
class WaterJug:
    def __init__(self, initial_state=(0, 0), goal_state=(2, 0)):
        self.initial_state = initial_state
        self.goal_state = goal_state

    def successors(self, state):
        X, Y = state
        succ = []

        if X < 4:
            succ.append((4, Y))

        if Y < 3:
            succ.append((X, 3))

        if X > 0:
            succ.append((0, Y))

        if Y > 0:
            succ.append((X, 0))

        if X > 0 and Y < 3:
            transfer = min(X, 3 - Y)
            succ.append((X - transfer, Y + transfer))

        if Y > 0 and X < 4:
            transfer = min(Y, 4 - X)
            succ.append((X + transfer, Y - transfer))

        return succ

    def bfs_with_path(self, initial_state, goal_state):
        open_queue = deque([(initial_state, [initial_state])])
        closed_set = set()

        while open_queue:
            current_state, path = open_queue.popleft()
            closed_set.add(current_state)

            if current_state == goal_state:
                return path
            for succ in self.successors(current_state):
                if succ not in closed_set and succ not in [state for state, _ in open_queue]:
                    new_path = path + [succ]
                    open_queue.append((succ, new_path))

        return None

    def run(self):
        result = self.bfs_with_path(self.initial_state, self.goal_state)
        if result is None:
            print("Goal not found")
        else:
            print("Goal found:", result)


sol = WaterJug()
sol.run()


