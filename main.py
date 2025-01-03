import os

from Melodie import Config
from Melodie import Simulator

from core.model import DatingMarketModel
from core.scenario import DatingScenario


def run_model(config):
    """
    By calling `simulator.run()`, we ask Melodie to run the model for all the scenarios,
    which are defined as rows in the `SimulatorScenario.xlsx` file.
    For each scenario, Melodie will run the model `run_num` times.

    More specifically, we go through the following steps:

    First, based on the rows in the `SimulatorScenario.xlsx` file, Melodie will create a list of `scenario` objects.
    At the same time, each `scenario` object also calls its `setup` and `load_data` functions for self-initialization.

    Second, when running one `scenario`, a model object will be created, as well as its components,
    including agent_list(s), environment, data_collector.
    Two functions of the `model` object are called:
     - model.create() --> the model components are created, including agent_list(s), environment, data_collector.
     For each component, its `setup` function is also called to create the parameter/variable attributes.
     - model.setup() --> the model components are filled in with data, especially the agent_list(s).

    Third, after setting up the `model` and its components for this `scenario`,
    the `simulator` will call `model.run()` to run the model under the current `scenario` and save the results.
    After finishing, the `simulator` automatically starts running the next scenario.
    """
    simulator = Simulator(
        config=config,
        model_cls=DatingMarketModel,
        scenario_cls=DatingScenario
    )
    simulator.run()


if __name__ == "__main__":
    cfg = Config(
        project_name="DatingMarket",
        project_root=os.path.dirname(__file__),
        input_folder="data/input",
        output_folder="data/output",
    )
    run_model(cfg)


