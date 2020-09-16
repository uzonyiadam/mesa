from mesa import Agent


class MoleculeCell(Agent):
    """
    A cell is
    - inactive, if its state is 0
    - full, if its state reaches the maximal value (defined by the model)
    - active, if it is not inactive and not full
    """
    def __init__(self, pos, model):
        # Input arguments: pos, model
        super().__init__(pos, model)

        ### TO BE DONE
        # State - initialized by a random number between 0 and full value
        full_value = None
        self.state = model.random.randint(0, full_value)
        # Position of the cell
        self.pos = None
        ### TO BE DONE

        # New state - store update value first and update state after all cells are considered
        self.new_state = None

    def step(self):
        # Number of active neighbors
        n_active_neighbors = 0
        # Number of full neighbors
        n_full_neighbors = 0
        # Collected neighbor states
        neighbors_state = []

        # Loop through all neighbors
        for neighbor in self.model.grid.neighbor_iter(self.pos, moore=True):

            ### TO BE DONE
            # Append state of considered cell to the neighbors_state list
            pass
            # Increment n_full_neighbors, if state of the neighbor is at full
            if None:
                n_full_neighbors += 1
            # Increment n_active_neighbors, if state of the neighbor is between 0 and full value
            # Hint: you can write chain of inequalities in Python, i.e. a < b < c
            elif None:
                n_active_neighbors += 1
            ### TO BE DONE

        ### TO BE DONE
        # Set new_state to 0, if state is at full
        if None:
            self.new_state = 0
        # Set state to int(n_full_neighbors/k_full) + int(n_active_neighbors/k_active)
        # where k_full and k_active are parameters of the model, if the molecule is inactive
        elif None:
            self.new_state = int(None) + int(None)
        # Set state to
        # int( (sum(states of neighbors) + own state) / (n_active_neighbors + n_full_neighbors + 1) ) + g
        # where g is a parameter of the model
        else:
            self.new_state = int((sum(None) + None) / (None + 1)) + None
        # Corect new state, if it gets larger, than full value from the model
        if None:
            pass
        ### TO BE DONE
