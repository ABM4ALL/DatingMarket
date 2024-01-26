import os

from Melodie import Config
from Melodie import Simulator

from core.model import DatingMarketModel
from core.scenario import DatingScenario


def run_model(config):
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


