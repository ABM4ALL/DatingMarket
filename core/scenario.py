import random
from typing import Optional

import pandas as pd
from Melodie import Scenario
from tab2dict import TabDict


class DatingScenario(Scenario):

    def setup(self):
        self.man_num: int = 0
        self.woman_num: int = 0
        self.selector_num: int = 0
        self.candidate_num: int = 0

    def load_data(self):

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
        l = []
        for id_woman in range(0, self.woman_num):
            share_social, share_saving = self.gen_shares()
            weight_age, weight_saving = self.gen_weights()
            l.append({
                "id_scenario": self.id,
                "id_run": self.id_run,
                "id": id_woman,
                "id_gender": 2,
                "share_social": share_social,
                "share_saving": share_saving,
                "weight_age": weight_age,
                "weight_saving": weight_saving
            })
        self.woman_params = pd.DataFrame(l)



