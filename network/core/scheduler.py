import random


class BaseScheduler:
    def __init__(self):
        self.steps, self.time, self.agents = 0, 0, []

    def add(self, agent):
        self.agents.append(agent)

    def add_all(self, agents):
        [self.add(x) for x in agents]

    def remove(self, agent):
        while agent in self.agents:
            self.agents.remove(agent)

    def step(self):
        [agent.step() for agent in self.agents]
        self.steps += 1
        self.time += 1


class RandomActivation(BaseScheduler):
    def step(self):
        random.shuffle(self.agents)
        [agent.step() for agent in self.agents]
        self.steps += 1
        self.time += 1


class SimultaneousActivation(BaseScheduler):
    def step(self):
        [agent.step() for agent in self.agents]
        [agent.advance() for agent in self.agents]
        self.steps += 1
        self.time += 1


class StagedActivation(BaseScheduler):
    def __init__(self, steps):
        super().__init__()
        self.stage_list = steps + ['no_move']

    def step(self):
        [getattr(agent, stage)() for stage in self.stage_list for agent in self.agents]
        self.steps += 1
