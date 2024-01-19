from typing import Optional
import random
import pandas as pd
from Melodie import DataFrameInfo
from Melodie import Scenario
from tab2dict import TabDict

from source import data_info


class DatingScenario(Scenario):

    def load(self):
        self.df = self.load_dataframe("Data_xxx")

    def setup(self):
        self.period_num: int = 0
        self.man_num: int = 0
        self.woman_num: int = 0

    def setup_scenario_data(self):

        def load_df2dict(df_info: "DataFrameInfo", col_name: Optional[str] = None):
            return TabDict.from_dataframe(
                df=self.get_dataframe(df_info),
                tdict_type="Data",
                value_column_name=col_name
            )

        self.prob_infected2infected = load_df2dict(df_info=data_info.transition_prob, col_name="infected")
        self.prob_infected2recovered = load_df2dict(df_info=data_info.transition_prob, col_name="recovered")
        self.setup_men_params()
        self.setup_women_params()

    @staticmethod
    def gen_shares_and_weights():
        random_numbers = [random.uniform(0, 1) for _ in range(3)]
        total = sum(random_numbers)
        return [num / total for num in random_numbers]

    def setup_men_params(self):
        l = []
        for id_man in range(0, self.man_num):
            s1, s2, s3 = self.gen_shares_and_weights()
            w1, w2, w3 = self.gen_shares_and_weights()
            l.append({
                "id_scenario": self.id,
                "id_run": self.id_run,
                "id": id_man,
                "id_gender": 1,
                "id_state": 1,
                "share_social": s1,
                "share_saving": s2,
                "share_quality": s3,
                "weight_age": w1,
                "weight_saving": w2,
                "weight_quality": w3
            })
        self.men_params = pd.DataFrame(l)

    def setup_women_params(self):
        l = []
        for id_woman in range(0, self.woman_num):
            s1, s2, s3 = self.gen_shares_and_weights()
            w1, w2, w3 = self.gen_shares_and_weights()
            l.append({
                "id_scenario": self.id,
                "id_run": self.id_run,
                "id": id_woman,
                "id_gender": 2,
                "id_state": 1,
                "share_social": s1,
                "share_saving": s2,
                "share_quality": s3,
                "weight_age": w1,
                "weight_saving": w2,
                "weight_quality": w3
            })
        self.women_params = pd.DataFrame(l)



