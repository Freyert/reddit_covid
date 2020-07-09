__version__ = "0.1.0"

from . import fetch
from . import present
from . import constants
from . import post
from . import graph


def main():

    for state in constants.stateConfig.keys():
        df = fetch.fetch(state)
        stateConf = constants.stateConfig[state]
        present.build_image(graph.graph(df), stateConf)
        post.post(stateConf)
