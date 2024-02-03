import random
from typing import TYPE_CHECKING

from Melodie import Agent

from utils.funcs import dict_sample
from utils.tabkey import DatingTabKey

if TYPE_CHECKING:
    from core.scenario import DatingScenario


class Person(Agent):
    scenario: "DatingScenario"

    def setup(self):
        """
        This function must be written to create the parameters and variables of the agent.
        These parameters and variables are created with values of 0. The real values are initialized in the second step.

        The parameters can include two groups:
         - Group 1: these parameters are initialized by `agent_list.setup_agents(agents_num, params_df)` in the model.
         - Group 2: these parameters are usually initialized in the next step, e.g., based on Group 1 parameters.

        The variables of agents are also created here. Their values will be updated when running the model.
        """
        # Group 1 parameters --> initialized with the `man_params` or `women_params` dataframes from `scenario`.
        self.id_gender: int = 0
        self.share_social: float = 0.0
        self.share_saving: float = 0.0
        self.weight_age: float = 0.0
        self.weight_saving: float = 0.0
        # Group 2 parameters --> initialized by environment calling `persons_setup_data`.
        self.age: int = 0
        # Variables --> changed in every period and also saved by the `data_collector`.
        self.income_before_shock: float = 0.0
        self.income: float = 0.0
        self.social: float = 0.0
        self.saving: float = 0.0

    def setup_tkey(self):

        def setup_id_age_group():
            d = {}
            for id_age_group in range(1, len(self.scenario.age_groups) + 1):
                self.tkey.id_age_group = id_age_group
                d[id_age_group] = self.scenario.prob_age_group.get_item(self.tkey)
            return dict_sample(d)

        def setup_id_income_group():
            d = {}
            l = self.scenario.rel_age_group_income_group.get_item(self.tkey)
            for id_income_group in l:
                self.tkey.id_income_group = id_income_group
                d[id_income_group] = self.scenario.prob_income_group.get_item(self.tkey)
            return dict_sample(d)

        self.tkey = DatingTabKey(id_gender=self.id_gender, time_period=-1)  # model.run updates time_period to 0, 1, ...
        self.tkey.id_age_group = setup_id_age_group()
        self.tkey.id_income_group = setup_id_income_group()

    def setup_age(self):
        self.age = random.randint(
            self.scenario.age_min.get_item(self.tkey),
            self.scenario.age_max.get_item(self.tkey),
        )

    def get_income(self):
        self.income_before_shock = random.uniform(
            self.scenario.income_min.get_item(self.tkey),
            self.scenario.income_max.get_item(self.tkey),
        )
        self.income = self.income_before_shock * self.scenario.income_shock.get_item(self.tkey)

    def spend_income(self):
        self.social = self.income * self.share_social
        self.saving = self.income * self.share_saving

    def assess_candidate(self, candidate_age: int, candidate_saving: float):
        return (self.weight_age * abs(candidate_age - self.age)/self.age +
                self.weight_saving * (candidate_saving - self.saving)/self.saving)

