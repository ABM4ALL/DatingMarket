import os

from Melodie import Config
from Melodie import Simulator

from source.analyzer import DatingAnalyzer
from source.data_loader import CovidDataLoader
from source.model import DatingMarketModel
from source.scenario import DatingScenario


def run_model(config):
    simulator = Simulator(
        config=config,
        model_cls=DatingMarketModel,
        scenario_cls=DatingScenario,
        data_loader_cls=CovidDataLoader
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
    run_analyzer(cfg)


