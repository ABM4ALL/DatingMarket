import os

from Melodie import Config
from Melodie import Simulator

from utils.analyzer import DatingAnalyzer
from core.model import DatingMarketModel
from core.scenario import DatingScenario


def run_model(config):
    simulator = Simulator(
        config=config,
        model_cls=DatingMarketModel,
        scenario_cls=DatingScenario
    )
    simulator.run()


def run_analyzer(config):
    analyzer = DatingAnalyzer(config)
    analyzer.plot_health_state_share(id_scenario=0)
    analyzer.plot_health_state_share(id_scenario=1)


if __name__ == "__main__":
    cfg = Config(
        project_name="DatingMarket",
        project_root=os.path.dirname(__file__),
        input_folder="data/input",
        output_folder="data/output",
    )
    run_model(cfg)
    # run_analyzer(cfg)


