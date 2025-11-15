from collections import deque

class MapEnvironment:
    def __init__(self):
        self.graph = {
            'A': {'B': 2, 'C': 4},
            'B': {'A': 2, 'D': 3, 'E': 5},
            'C': {'A': 4, 'F': 6},
            'D': {'B': 3},
            'E': {'B': 5, 'F': 1},
            'F': {'C': 6, 'E': 1, 'G': 2},
            'G': {'F': 2}
        }

    def get_neighbors(self, city):
        return self.graph.get(city, {})
    def get_cost(self, from_city, to_city):
        return self.graph[from_city].get(to_city,  float('inf'))

class RouteFindingAgent:
    def __init__(self, environment):
        self.env = environment
    def bfs (self, start, goal):
        queue = deque()
        queue.append((start, [start]))
        visited = set()

        while queue:
            current, path = queue.popleft()

            if current == goal:
                return path
            if current in visited:
                continue
            visited.add(current)

            for neighbor in self.env.get_neighbors(current):
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))

        return None

    def calculate_cost(self, path):
        if not path or len(path) < 2:
            return 0
        total_cost = 0
        for i in range(len(path) - 1):
            from_city = path[i]
            to_city = path[i+1]
            cost = self.env.get_cost(from_city, to_city) 
            total_cost += cost
        return total_cost               

env = MapEnvironment()
agent = RouteFindingAgent(env)

start_city = 'A'
goal_city = 'G'
path = agent.bfs(start_city, goal_city)
cost = agent.calculate_cost(path)
print(f"Path from {start_city} to {goal_city}: {path}")
print(f"Total path cost: {cost}")