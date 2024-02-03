from typing import TYPE_CHECKING

import pandas as pd
from Melodie import Model

from core.data_collector import DatingDataCollector
from core.environment import DatingEnvironment
from core.person import Person
from core.scenario import DatingScenario

if TYPE_CHECKING:
    from Melodie import AgentList


class DatingMarketModel(Model):
    scenario: "DatingScenario"

    def create(self):
        """
        This function is automatically called by Melodie (i.e., the `simulator`).
        The model components are created here, including agent_list(s), environment, data_collector.
        For each component, the "setup" function (if exists) is also called when being created.
        """
        self.women: "AgentList[Person]" = self.create_agent_list(Person)
        self.men: "AgentList[Person]" = self.create_agent_list(Person)
        self.environment: DatingEnvironment = self.create_environment(DatingEnvironment)
        self.data_collector: DatingDataCollector = self.create_data_collector(DatingDataCollector)

    def setup(self):
        """
        This function is automatically called by Melodie (i.e., the `simulator`).
        After being created, the model components are set up in this function, especially the agents,
        meaning that the Group 1 parameters of agents are initialized with real values.
        """
        self.scenario.setup_person_params()
        self.data_collector.save_dataframe(df=self.scenario.man_params, df_name="Params_Man")
        self.men.setup_agents(agents_num=self.scenario.man_num, params_df=self.scenario.man_params)
        self.women.setup_agents(agents_num=self.scenario.woman_num, params_df=self.scenario.woman_params)
        self.environment.persons_setup_data(self.men)
        self.environment.persons_setup_data(self.women)

    def run(self):
        """
        This function is automatically called by Melodie (i.e., the `simulator`).
        """
        for period in range(0, self.scenario.period_num):
            self.environment.reset_total_assessment()
            self.environment.persons_update_time_period(self.women)
            self.environment.persons_update_time_period(self.men)
            self.environment.persons_get_income(self.women)
            self.environment.persons_get_income(self.men)
            self.environment.persons_spend_income(self.women)
            self.environment.persons_spend_income(self.men)
            self.environment.organize_dates(potential_selectors=self.women, potential_candidates=self.men, period=period)
            self.environment.organize_dates(potential_selectors=self.men, potential_candidates=self.women, period=period)
            self.data_collector.collect(period)
        self.data_collector.save()
        self.data_collector.save_dataframe(df=pd.DataFrame(self.environment.dates), df_name="Result_Dates")
