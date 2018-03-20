import random

import structures.debt_allocator as sa
from network.core.scheduler import StagedActivation
from network.core.skeleton import Graph


class FinNetwork(Graph):
    def __init__(self, name, init_agents, net_type, p, k, m, steps):
        self.steps = steps
        super().__init__(name, init_agents, net_type, p, k, m)
        sa.allocate(self.schedule.agents)

    def apply_shock(self, pos):
        unlucky = self.get_agent(pos)
        if unlucky:
            shock = unlucky.capital.value * random.random()
            unlucky.apply_initial_shock(shock)

    def step(self):
        self.schedule.step()

    def get_scheduler(self):
        return StagedActivation(self)

    def initialize_model(self):
        for x in self.schedule.agents:
            x.model = self
