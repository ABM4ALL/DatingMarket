import os.path
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
        self.scenario.setup_data()
        self.data_collector.save_dataframe(df=self.scenario.man_params, df_name="man_params", if_exists="append")
        self.data_collector.save_dataframe(df=self.scenario.woman_params, df_name="woman_params", if_exists="append")
        self.men.setup_agents(
            agents_num=self.scenario.man_num,
            params_df=self.scenario.man_params,
        )
        self.women.setup_agents(
            agents_num=self.scenario.woman_num,
            params_df=self.scenario.woman_params,
        )

    def run(self):
        self.environment.persons_setup_tkey(self.men)
        self.environment.persons_setup_tkey(self.women)
        # for period in range(0, self.scenario.period_num):
        #     self.data_collector.collect(period)
        # self.data_collector.save()
