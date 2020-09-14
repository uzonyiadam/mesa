import numpy as np

from mesa import Agent, Model
from mesa.space import MultiGrid
from mesa.time import RandomActivation


class EpidemicAgent(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.state = 0

    def step(self):
        other_agent = self.random.choice(self.model.schedule.agents)
        if self.state == 1:
            # Infection
            if np.random.rand() < 0.2:
                other_agent.state = 1

            # Recovery
            if np.random.rand() < 0.3:
                self.state = 2

        elif other_agent.state == 1:
            if np.random.rand() < 0.2:
                self.state = 1


class EpidemicModel(Model):
    def __init__(self, num_agents, width, height):
        self.num_agents = num_agents
        self.grid = MultiGrid(width, height, True)
        self.schedule = RandomActivation(self)
        self.time_series = []

        # Create agents
        for i in range(self.num_agents):
            a = EpidemicAgent(i, self)
            self.schedule.add(a)

            # Add agent to a random grid cell
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(a, (x, y))

        # Pick one infected
        agent = self.random.choice(self.schedule.agents)
        agent.state = 1

    def step(self):
        self.schedule.step()
        susc, inf, rec = 0, 0, 0
        for agent in self.schedule.agents:
            if agent.state == 0:
                susc += 1
            elif agent.state == 1:
                inf += 1
            else:
                rec += 1
        self.time_series.append([susc, inf, rec])
