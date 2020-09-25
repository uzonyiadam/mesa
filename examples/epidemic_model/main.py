import matplotlib.pyplot as plt

from examples.epidemic_model.source.model import EpidemicModel


def main():
    num_agent = 100
    width = 15
    height = 15
    model = EpidemicModel(num_agent=num_agent,
                          width=width,
                          height=height)
    timespan = 100
    for t in range(0, timespan):
        model.step()

    states = model.data_collector.get_model_vars_dataframe()
    states.plot()
    plt.show()


if __name__ == '__main__':
    main()
