import random

class ReflexAgent:
    def __init__(self,room_size=(10,10)):
        self.room_size = room_size
        self.grid = [[random.choice([0,1]) for _ in range(room_size[1])] for _ in range(room_size[0])]
        print(self.grid)
        self.current_position = (random.randint(0,room_size[0]-1),random.randint(0,room_size[1]-1))
        print(f"Agent's Position is: {self.current_position}")
    def display_room(self):
        for row in self.grid:
            for cell in row:
                print(str(cell), end=" ")
            print("\n")
    #
    def perceive(self):
        x, y = self.current_position
        return self.grid[x][y]
    #
    def act(self):
        x, y = self.current_position
        if self.perceive() == 1:
            print(f"cell ({x}, {y}) is Dirty. Cleaning.....")
            self.grid[x][y] = 0
            print(f"Cell ({x}, {y}) is now clean.")
        else:
            print(f"Cell ({x}, {y}) is already Clean. ")

    def optimized_move(self):
        if not hasattr(self,'visited'):
            self.visited = set()
        self.visited.add(self.current_position)
        print(f"visited cells: {self.visited}")

        x,y = self.current_position
        room_height, room_width = self.room_size

        possible_moves = [
            (x,y+1),
            (x+1,y),
            (x,y-1),
            (x-1,y)
        ]

        for dx, dy in [(0,1),(1,0),(0,-1),(-1,0)]:
            new_x, new_y = x+dx, y+dy
            if(0<= new_x < room_height and
                0<= new_y < room_width and
                (new_x, new_y) not in self.visited and
                self.grid[new_x][new_y] == 1):
                self.current_position = (new_x, new_y)
                return
        for new_x, new_y in possible_moves:
            if(0<= new_x < room_height and
                0<= new_y < room_width and
                (new_x, new_y) not in self.visited):
                self.current_position = (new_x, new_y)
                return
        if not self.is_room_clean():
            for i in range(room_height):
                for j in range(room_width):
                    if self.grid[i][j] ==  1:
                        self.current_position = (i,j)
                        return
        else:
            self.current_position = None

    def is_room_clean(self):
        return all(cell == 0 for row in self.grid for cell in row)

    def run(self):
        print("Initial Room Status: ")
        self.display_room()

        steps = 0
        while not self.is_room_clean():
            print(f"\nStep {steps + 1}: ")
            self.act()
            self.optimized_move()
            steps += 1
            if self.current_position is None:
                self.current_position = (0, 0)
        print("\nFinal Room Status: ")
        self.display_room()
        print(f"Room cleaned in {steps} steps.")
agent = ReflexAgent()
agent.run()
