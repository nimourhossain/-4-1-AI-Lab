import random  

class GridWorld:
    def __init__(self, size=5):
        self.size = size
        self.agent_pos = [0, 0]
        self.goal_pos = [random.randint(0, size - 1), random.randint(0, size - 1)]

    def move_agent(self, direction):
        if direction == 'right' and self.agent_pos[1] < self.size - 1:
            self.agent_pos[1] += 1
        elif direction == 'left' and self.agent_pos[1] > 0:
            self.agent_pos[1] -= 1
        elif direction == 'up' and self.agent_pos[0] > 0:
            self.agent_pos[0] -= 1
        elif direction == 'down' and self.agent_pos[0] < self.size - 1:
            self.agent_pos[0] += 1

    def is_goal_reached(self):
        return self.agent_pos == self.goal_pos

class SimpleAgent:
    def __init__(self, env):
        self.env = env

    def act(self):
        while not self.env.is_goal_reached():
            ax, ay = self.env.agent_pos
            gx, gy = self.env.goal_pos

            if gx > ax:
                self.env.move_agent('down')
            elif gx < ax:
                self.env.move_agent('up')
            elif gy > ay:
                self.env.move_agent('right')
            elif gy < ay:
                self.env.move_agent('left')

            print(f"Agent moved to: {self.env.agent_pos}")

        print("Goal reached!")

# Run it
env = GridWorld()
agent = SimpleAgent(env)

print(f"Agent starting at {env.agent_pos}, Goal at {env.goal_pos}")
agent.act()
