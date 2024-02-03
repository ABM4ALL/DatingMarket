import random
from typing import Optional

import pandas as pd
from Melodie import Scenario
from tab2dict import TabDict


class DatingScenario(Scenario):

    def setup(self):
        """
        This function is automatically called. The model-wide parameters are defined here.
        The names must be same with the columns names defined in the "SimulatorScenario.xlsx" table.
        Three columns must be included in the "SimulatorScenario.xlsx" table but not necessarily defined here:
         - `id` --> the `id` of the `scenario`;
         - `run_num` --> for one `scenario`, Melodie supports running the model multiple times for robustness check;
         - `period_num` --> number of periods in one simulation.
        These three parameters of the scenario are already defined in Melodie.
        Their names in the "SimulatorScenario.xlsx" table must be the same.
        """
        self.man_num: int = 0
        self.woman_num: int = 0
        self.selector_num: int = 0
        self.candidate_num: int = 0

    def load_data(self):
        """
        This function is automatically called. Users can use `self.load_dataframe()` to import data from `data/input`.
        The `scenario` object holds all the data loaded into the model and can be accessed in all model components.
        In this example, the `tab2dict` package is used to further convert loaded dataframes to `tdict`s.
        """
        def load_tdict(file_name, col_name: Optional[str] = "value"):
            return TabDict.from_dataframe(
                df=self.load_dataframe(file_name),
                tdict_type=file_name.split("_")[0],
                value_column_name=col_name
            )

        self.genders = load_tdict("ID_Gender.xlsx")
        self.age_groups = load_tdict("ID_AgeGroup.xlsx")
        self.income_groups = load_tdict("ID_IncomeGroup.xlsx")
        self.rel_age_group_income_group = load_tdict("Relation_AgeGroup_IncomeGroup.xlsx")
        self.age_min = load_tdict("Data_Age.xlsx", col_name="min")
        self.age_max = load_tdict("Data_Age.xlsx", col_name="max")
        self.income_min = load_tdict("Data_Income.xlsx", col_name="min")
        self.income_max = load_tdict("Data_Income.xlsx", col_name="max")
        self.prob_age_group = load_tdict("Data_Prob_AgeGroup.xlsx")
        self.prob_income_group = load_tdict("Data_Prob_IncomeGroup.xlsx")
        self.income_shock = load_tdict("Data_IncomeShock.xlsx")

    def setup_person_params(self):
        self.setup_man_params()
        self.setup_woman_params()

    @staticmethod
    def gen_shares():
        random_numbers = [random.uniform(0, 1) for _ in range(0, 2)]
        total = sum(random_numbers)
        return [num / total for num in random_numbers]

    @staticmethod
    def gen_weights():
        weight_age = random.uniform(-1, 0)
        weight_saving = random.uniform(0, 1)
        return weight_age, weight_saving

    def setup_man_params(self):
        l = []
        for id_man in range(0, self.man_num):
            share_social, share_saving = self.gen_shares()
            weight_age, weight_saving = self.gen_weights()
            l.append({
                "id_scenario": self.id,
                "id_run": self.id_run,
                "id": id_man,
                "id_gender": 1,
                "share_social": share_social,
                "share_saving": share_saving,
                "weight_age": weight_age,
                "weight_saving": weight_saving
            })
        self.man_params = pd.DataFrame(l)

    def setup_woman_params(self):
        """
        To compare with the generation and use of `man_params`, we prepared `Params_Woman.csv` to show
        how agent-level initialization data can be imported and used. When agents' initialization data are
        neither scenario-dependent nor necessary-to-be randomized, we suggest using such approach.
        Besides, users can also adapt the imported exogenous table by adding scenario-dependent columns.
        In that case, we suggest to add also `id_scenario` and `id_run` columns as in the `man_params` above.
        """
        self.woman_params = self.load_dataframe("Params_Woman.csv")



