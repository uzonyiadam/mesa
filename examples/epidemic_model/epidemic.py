import numpy as np

from examples.epidemic_model.utils import inf, rec, susc
from mesa import Agent, Model
from mesa.datacollection import DataCollector
from mesa.space import MultiGrid
from mesa.time import RandomActivation


class EpidemicAgent(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.state = 0

    def step(self):
        self.move()
        self.epi()

    def move(self):
        possible_steps = self.model.grid.get_neighborhood(self.pos, moore=True, include_center=False, radius=5)
        new_position = self.random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)

    def epi(self):
        agents_in_the_same_cell = self.model.grid.get_cell_list_contents([self.pos])
        # Infection
        if len(agents_in_the_same_cell) > 1:
            other_agent = self.random.choice(agents_in_the_same_cell)
            self.infect(other_agent)
        # Recovery
        self.recover()

    def recover(self):
        recovery_prob = 0.2
        if self.state == 1 and np.random.rand() < recovery_prob:
            self.state = 2

    def infect(self, other_agent):
        infection_prob = 0.75
        if self.state == 1 and other_agent.state == 0:
            if np.random.rand() < infection_prob:
                other_agent.state = 1
        elif other_agent.state == 1 and self.state == 0:
            if np.random.rand() < infection_prob:
                self.state = 1


class EpidemicModel(Model):
    def __init__(self, num_agents, width, height):
        self.num_agents = num_agents
        self.grid = MultiGrid(width, height, True)
        self.schedule = RandomActivation(self)

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

        self.data_collection = DataCollector(
            model_reporters={"Susceptibles": susc, "Infecteds": inf, "Recovereds": rec},
            agent_reporters={"State": "state"}
        )

    def step(self):
        self.data_collection.collect(self)
        self.schedule.step()
