from Melodie import DataCollector
import pandas as pd


class DatingDataCollector(DataCollector):
    def setup(self):
        self.add_agent_property(container_name="men", property_name="id_state")
        self.add_agent_property(container_name="women", property_name="id_state")
        self.add_environment_property(property_name="s1")

    def save_dataframe(self, table_name: str, df: pd.DataFrame):
        self.db.write_dataframe(table_name=table_name, data_frame=df)
