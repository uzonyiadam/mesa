from examples.bz_reaction.source.agent import MoleculeCell
from mesa import Model
from mesa.datacollection import DataCollector
from mesa.space import Grid
from mesa.time import RandomActivation


class BZReactionModel(Model):
    def __init__(self, width=50, height=50, k_full=3, k_active=3, full_value=200, g=28):
        # scheduler
        self.schedule = RandomActivation(self)
        # grid: instance of Grid with specified width, height and torus=False
        self.grid = Grid(width=width, height=height, torus=False)

        ### TO BE DONE
        # Model parameters
        # Full value: maximum value can be reached by a cell
        self.full_value = None
        # k_full: how many neighbors with full state is needed for changing state of an inactive cell
        self.k_full = None
        # k_active: how many neighbors with active state is needed for changing state of an inactive cell
        self.k_active = None
        # g: accelerates activation of a cell, added to the change of state for an active cell
        self.g = None
        ### TO BE DONE

        # running: needed for interactive visualization
        self.running = True

        # Create molecules and place them in a grid cell
        # Looping through all rows of the grid
        for x in range(height):
            # Looping through all columns of the grid
            for y in range(width):

                ### TO BE DONE
                # Instantiate molecule
                molecule = MoleculeCell(pos=None, model=None)
                # Add molecule to the scheduler
                pass
                # Place molecule in the grid
                self.grid.place_agent(pos=None, agent=molecule)
                ### TO BE DONE

        # data collector for plotting
        self.data_collection = DataCollector(
            # collect number of inactive and full molecules at each step
            model_reporters={"Inactives": count_inactive, "Fulls": count_full},
            agent_reporters={"State": "state"}
        )

    def step(self):
        # Collect data
        self.data_collection.collect(self)
        # Execute step of each molecules
        self.schedule.step()

        # Update state of molecules by the calculated new states
        # Looping through all molecules

        ### TO BE DONE
        molecules = None
        for molecule in molecules:
            # Set new state to state
            pass
        ### TO BE DONE


def count(model):
    # Number of inactive molecules
    n_inactive = 0
    # Number of full molecules
    n_full = 0
    # Looping through all molecules from model.schedule

    ### TO BE DONE
    molecules = None
    for molecule in molecules:
        # Increment n_inactive, if state of the molecule is 0
        if None:
            n_inactive += 1
        # Increment n_inactive, if state of the molecule is at full value
        elif None:
            n_full += 1
    ### TO BE DONE

    # return with a list of n_inactive and n_full
    return [n_inactive, n_full]


def count_inactive(model):
    # return number of inactive molecules, which is the first element of the output of count() function
    return count(model)[0]


def count_full(model):
    # return number of inactive molecules, which is the second element of the output of count() function
    return count(model)[1]
