import os

from Melodie import Config
from Melodie import Simulator

from core.model import DatingMarketModel
from core.scenario import DatingScenario


def run_model(config):
    """
    By calling the `simulator.run()` function, following steps are went through:

    1. instantiate and set up the `scenario` objects
    A set of `scenario` instances are created based on the rows in the `SimulatorScenario.xlsx` file.
    Besides, each instance also calls its `setup` and `load_data` functions to initialize the scenario data.

    2. instantiate and set up the `model` object
    The `simulator` will iterate through the list of scenarios. For each scenario,
    an overall model container is created and its three functions are called:
     - model.create() --> the model components are created, including agent_list(s), environment, data_collector.
     For each component, the `setup` function is called at the same time.
     - model.setup() --> the model components are configured with data, especially the agent_list(s).

    3. run model
    After instantiating and setting up the scenario and model, the `simulator` calls `model.run()` to run the model.
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


