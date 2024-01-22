import os

import pandas as pd
from Melodie import DataCollector


class DatingDataCollector(DataCollector):
    def setup(self):
        self.add_agent_property(container_name="men", property_name="id_state")
        self.add_agent_property(container_name="women", property_name="id_state")
        self.add_environment_property(property_name="s1")

    def save_dataframe(self, df: pd.DataFrame, df_name: str, if_exists: str = 'replace'):
        path = os.path.join(self.config.output_folder, f'{df_name}.csv')
        if os.path.isfile(path):
            if if_exists == "replace":
                df.to_csv(path, mode='w', index=False)
            elif if_exists == "append":
                df.to_csv(path, mode='a', header=False, index=False)
        else:
            df.to_csv(path, index=False)