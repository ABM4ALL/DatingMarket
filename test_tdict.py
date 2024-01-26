from tab2dict import TabDict
from utils.tabkey import DatingTabKey
import os
import pandas as pd


def load_tdict_file(file_name: str, col: str = "value"):
    file_path = os.path.join("data", "input", file_name)
    return TabDict.from_file(file_path=file_path, value_column_name=col)


def load_tdict_df(file_name: str, col: str = "value"):
    df = pd.read_excel(os.path.join("data", "input", file_name))
    return TabDict.from_dataframe(
        df=df,
        tdict_type=file_name.split("_")[0],
        value_column_name=col
    )


if __name__ == "__main__":
    prob_age_group = load_tdict_file("Data_Prob_AgeGroup.xlsx")
    prob_income_group = load_tdict_file("Data_Prob_IncomeGroup.xlsx")
    age_min = load_tdict_df("Data_Age.xlsx", col="min")
    tkey = DatingTabKey(id_age_group=3, id_gender=1, id_income_group=2)
    print(prob_age_group.to_dataframe())
    print(prob_age_group.get_item(tkey))
    print(prob_income_group.to_dataframe())
    print(prob_income_group.get_item(tkey))
    print(age_min.to_dataframe())
    print(age_min.get_item(tkey))



