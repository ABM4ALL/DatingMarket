import os

import pandas as pd
from tab2dict import TabDict

from utils.tabkey import DatingTabKey


"""
This script shows how to use `tab2dict` package for loading data into a model.

First, `tab2dict` can automatically identifies
 - `tdict_type`: according to the prefix of file names: ID_, Relation_, Data_
 - `key_cols`: with `id_` or `time_` prefix in the column names
in an `.xlsx` or `.csv` file, and converts the input file into a `tdict`.
The two functions below show how to load an input table with `tab2dict`.
 
Second, `tdict` works together with a `tkey`:
 - a `tkey` is an instance of a class inheriting the `TabKey` class provided by the `tab2dict` package
 - with a `tkey` that knows the values of the `key_cols` of a `tdict`, one can fetch data from the `tdict`

In ABMs, each agent is assigned with a `tkey`, like an "identity" of the agent. 
With this `tkey`, the agent can get data from the `tdict`s. The advantage is, 
the agents usually know its "full identity" (i.e., values of all relevant `key_cols`).
For the agent, this is more than necessary for fetching data from individual `tdict`s.
So, users may be able to flexibly add new `id_` or `time_` columns in the input tables without changing code.
"""


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
    print(prob_age_group.get_item(tkey))
    print(prob_income_group.get_item(tkey))
    print(age_min.get_item(tkey))



