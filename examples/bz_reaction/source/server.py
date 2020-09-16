from matplotlib import cm
from matplotlib.colors import to_hex

from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer

from examples.bz_reaction.source.model import BZReactionModel


def bz_model_portrayal(molecule):
    if molecule is None:
        return
    portrayal = {"Shape": "rect", "w": 1, "h": 1, "Filled": "true", "Layer": 0}
    (x, y) = molecule.pos
    portrayal["x"] = x
    portrayal["y"] = y
    portrayal["Color"] = to_hex(cm.get_cmap('Reds')(1 - molecule.state/molecule.model.full_value))
    return portrayal


canvas_element = CanvasGrid(bz_model_portrayal, 50, 50, 500, 500)

server = ModularServer(
    BZReactionModel, [canvas_element], "Belousov–Zhabotinsky reaction"
)
