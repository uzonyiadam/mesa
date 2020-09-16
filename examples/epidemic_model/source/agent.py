import numpy as np

from mesa import Agent


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