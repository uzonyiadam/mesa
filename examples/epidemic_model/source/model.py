from examples.epidemic_model.source.agent import EpidemicAgent
from mesa import Model
from mesa.datacollection import DataCollector
from mesa.space import MultiGrid
from mesa.time import RandomActivation


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


def states(model):
    s, i, r = 0, 0, 0
    for agent in model.schedule.agents:
        if agent.state == 0:
            s += 1
        elif agent.state == 1:
            i += 1
        else:
            r += 1
    return [s, i, r]


def susc(model):
    return states(model)[0]


def inf(model):
    return states(model)[1]


def rec(model):
    return states(model)[2]
