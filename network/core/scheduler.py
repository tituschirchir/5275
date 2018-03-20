import random


class BaseScheduler:
    def __init__(self, model):
        self.model = model
        self.steps = 0
        self.time = 0
        self.agents = []

    def add(self, agent):
        self.agents.append(agent)

    def add_all(self, agents):
        for x in agents:
            self.add(x)

    def remove(self, agent):
        while agent in self.agents:
            self.agents.remove(agent)

    def step(self):
        for agent in self.agents[:]:
            agent.step()
        self.steps += 1
        self.time += 1

    def get_agent_count(self):
        return len(self.agents)


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
    def __init__(self, model):
        super().__init__(model)
        self.stage_list = ['no_move'] + model.steps

    def step(self):
        [getattr(agent, stage)() for stage in self.stage_list for agent in self.agents]
        self.steps += 1
