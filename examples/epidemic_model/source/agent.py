from mesa.agent import Agent


class EpidemicAgent(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id=unique_id, model=model)
        # 0: susceptible, 1: infected, 2: recovered
        self.state = 0

    def step(self):
        self.move()
        self.epi()

    def move(self):
        possible_places = self.model.grid.get_neighborhood(pos=self.pos,
                                                           moore=True,
                                                           include_center=False,
                                                           radius=5)
        new_position = self.model.random.choice(possible_places)
        self.model.grid.move_agent(agent=self, pos=new_position)

    def epi(self):
        agents_in_the_same_cell = self.model.grid.get_cell_list_contents([self.pos])
        # Infection
        if len(agents_in_the_same_cell) > 1:
            other_agent = self.model.random.choice(agents_in_the_same_cell)
            self.infect(other_agent)
        # Recovery
        self.recover()

    def infect(self, other_agent):
        infection_prob = 0.7
        if self.state == 0 and other_agent.state == 1:
            if self.model.random.random() < infection_prob:
                self.state = 1
        elif self.state == 1 and other_agent.state == 0:
            if self.model.random.random() < infection_prob:
                other_agent.state = 1

    def recover(self):
        recovery_prob = 0.2
        if self.state == 1 and self.model.random.random() < recovery_prob:
            self.state = 2


def susc(model):
    s = 0
    for agent in model.schedule.agents:
        if agent.state == 0:
            s += 1  # s = s + 1
    return s


def inf(model):
    i = 0
    for agent in model.schedule.agents:
        if agent.state == 1:
            i += 1
    return i


def rec(model):
    r = 0
    for agent in model.schedule.agents:
        if agent.state == 2:
            r += 1
    return r
