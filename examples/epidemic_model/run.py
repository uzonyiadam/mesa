import matplotlib.pyplot as plt

from examples.epidemic_model.epidemic import EpidemicModel


def main():
    num_agents = 100
    model = EpidemicModel(num_agents=num_agents, width=12, height=12)

    timespan = 100
    for i in range(timespan):
        model.step()

    states = []
    for agent in model.schedule.agents:
        states.append(agent.state)

    states = model.data_collection.get_model_vars_dataframe()
    states.plot()
    plt.show()


if __name__ == '__main__':
    main()
