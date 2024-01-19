from typing import TYPE_CHECKING

from Melodie import Model
from source.person import Person
from source.data_collector import DatingDataCollector
from source.environment import DatingEnvironment
from source.scenario import DatingScenario

if TYPE_CHECKING:
    from Melodie import AgentList


class DatingMarketModel(Model):
    scenario: "DatingScenario"

    def create(self):
        self.men: "AgentList[Person]" = self.create_agent_list(Person)
        self.women: "AgentList[Person]" = self.create_agent_list(Person)
        self.environment: DatingEnvironment = self.create_environment(DatingEnvironment)
        self.data_collector: DatingDataCollector = self.create_data_collector(DatingDataCollector)

    def setup(self):
        self.scenario.setup_scenario_data()
        self.men.setup_agents(
            agents_num=self.scenario.man_num,
            params_df=self.scenario.men_params,
        )
        self.women.setup_agents(
            agents_num=self.scenario.woman_num,
            params_df=self.scenario.women_params,
        )

    def run(self):
        self.environment.agents_setup_tkey(self.men)
        for period in range(0, self.scenario.period_num):
            self.data_collector.collect(period)
        self.data_collector.save()
