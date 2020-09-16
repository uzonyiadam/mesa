import matplotlib.pyplot as plt

from examples.bz_reaction.source.model import BZReactionModel


def main():
    # Grid parameters
    width = 50
    height = 50
    # Model parameters
    k_full = 3
    k_active = 3
    full_value = 200
    g = 28

    # Instantiate model
    model = BZReactionModel(width=width, height=height, k_full=k_full, k_active=k_active, full_value=full_value, g=g)

    # Time span of the simulation
    time_span = 100
    # Execute simulation
    for _ in range(time_span):
        model.step()

    # Get collected data
    states = model.data_collection.get_model_vars_dataframe()
    # Plot collected data
    states.plot()
    plt.show()


if __name__ == '__main__':
    main()
