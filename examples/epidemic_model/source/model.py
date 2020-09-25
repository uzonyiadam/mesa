from mesa.datacollection import DataCollector
from mesa.model import Model
from mesa.space import MultiGrid
from mesa.time import RandomActivation
from examples.epidemic_model.source.agent import EpidemicAgent, susc, rec, inf


class EpidemicModel(Model):
    def __init__(self, num_agent, width, height):
        super().__init__()
        self.num_agent = num_agent
        self.grid = MultiGrid(width=width, height=height, torus=True)
        self.schedule = RandomActivation(self)

        # Create agents
        for u_id in range(0, num_agent):
            a = EpidemicAgent(unique_id=u_id, model=self)
            self.schedule.add(a)

            # Place the agents in the grid
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(agent=a, pos=(x, y))

        # Pick one agent and infect him/her
        agent = self.random.choice(self.schedule.agents)
        agent.state = 1

        self.data_collector = DataCollector(
            model_reporters={"Susceptibles": susc,
                             "Infecteds": inf,
                             "Recovereds": rec}
        )

    def step(self):
        self.data_collector.collect(self)
        self.schedule.step()
