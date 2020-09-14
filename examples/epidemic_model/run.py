import matplotlib.pyplot as plt

from examples.epidemic_model.epidemic import EpidemicAgent, EpidemicModel


def main():
    num_agents = 100
    model = EpidemicModel(num_agents=num_agents, width=100, height=100)

    timespan = 20
    for i in range(timespan):
        model.step()

    states = []
    for agent in model.schedule.agents:
        states.append(agent.state)

    # Last time point
    plt.hist(states)
    plt.show()

    # Time series
    plt.plot(range(timespan), model.time_series)
    plt.show()


if __name__ == '__main__':
    main()
